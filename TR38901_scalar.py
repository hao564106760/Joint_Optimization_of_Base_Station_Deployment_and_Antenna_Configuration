from pyproj import Geod
import numpy as np
import random
import math
import sys


# This is to calculate the overall path loss based on the 3GPP TR 38.901 standard
# inputs:
# scenario:  indicate the scenario 'umi' or 'uma'
# fc:        carrier frequency (Hz)
# bs_lon:    base station longitude (degree)
# bs_lat:    base station latitude (degree)
# usr_lon:   user longitude (degree)
# usr_lat:   user latitude (degree)
# usr_h:     user height (m) 2
# is_indoor: whether user is indoor (0 or 1) 随机
# bs_azi:    antenna azimuth (degree)
# bs_tilt:   antenna tilt (degree)
# bw_azi:    azimuth beamwidth (degree)
# bw_tilt:   tilt beamwidth (degree)
# output:    PL (dB)
def calculate_path_loss(bs_lon, bs_lat, usr_lon, usr_lat, bs_azi, bs_tilt, usr_h=2, scenario='umi', fc=28e9,
                        is_indoor=0,
                        bw_azi=63, bw_tilt=6.5):
    g = Geod(ellps='WGS84')
    c = 3e8  # light speed

    # Step 1 calculate the path loss
    if scenario == 'umi':
        bs_h = 10
    elif scenario == 'uma':
        bs_h = 25
    else:
        print('Please select a valid scenario.')
        sys.exit()

    az, _, dis2D = g.inv(bs_lon, bs_lat, usr_lon, usr_lat)
    dis3D = math.sqrt(pow(dis2D, 2) + pow((bs_h - usr_h), 2))

    if is_indoor == 1:
        d2D_in = 25 * min(random.random(), random.random())
        if d2D_in > dis2D:
            d2D_in = dis2D
    else:
        d2D_in = 0
    d2D_out = dis2D - d2D_in

    # Determine LoS condition
    # Refer to Table 7.4.2-1
    if scenario == 'umi':
        if d2D_out <= 18:
            PRL = 1
        else:
            PRL = 18 / d2D_out + math.exp(- d2D_out / 36) * (1 - 18 / d2D_out)
    else:
        if d2D_out <= 18:
            PRL = 1
        else:
            if usr_h <= 13:
                cht = 0
            else:
                cht = pow((usr_h - 13) / 10, 1.5)
            PRL = (18 / d2D_out + math.exp(- d2D_out / 63) * (1 - 18 / d2D_out)) * (
                    1 + cht * 5 / 4 * pow(d2D_out / 100, 3) * math.exp(- d2D_out / 150))
    hasLOS = np.random.binomial(1, PRL, size=None)

    # Calculate path loss
    # Refer to Table 7.4.1-1
    if scenario == 'umi':
        a1 = 32.4
        b1 = 21
        a2 = 32.4
        b2 = 40
        c2 = 9.5
        p1 = 22.4
        q1 = 35.3
        r1 = 21.3
        s1 = 0.3
        sigma1 = 4
        sigma2 = 7.82
    else:
        a1 = 28
        b1 = 22
        a2 = 28
        b2 = 40
        c2 = 9
        p1 = 13.54
        q1 = 39.08
        r1 = 20
        s1 = 0.6
        sigma1 = 4
        sigma2 = 6

    if scenario == 'umi':
        hE = 1
    else:
        if dis2D <= 18:
            gg = 0
        else:
            gg = 5 / 4 * pow(dis2D / 100, 3) * math.exp(- dis2D / 150)
        if usr_h < 13:
            cc = 0
        else:
            cc = gg * pow((usr_h - 13) / 10, 1.5)
        prob1 = 1 / (1 + cc)
        hEtemp = np.random.binomial(1, prob1, size=None)
        if hEtemp == 0:
            hE = usr_h - 1.5
        else:
            hE = hEtemp
    dBP = 4 * (bs_h - hE) * (usr_h - hE) * fc / c

    PL1 = a1 + b1 * np.log10(dis3D) + 20 * np.log10(fc * 1e-9)
    PL2 = a2 + b2 * np.log10(dis3D) + 20 * np.log10(fc * 1e-9) - c2 * np.log10(pow(dBP, 2) + pow(bs_h - usr_h, 2))

    if dis2D <= dBP:
        PL_LOS = PL1
    else:
        PL_LOS = PL2
    PL_NLOS = p1 + q1 * np.log10(dis3D) + r1 * np.log10(fc * 1e-9) - s1 * (usr_h - 1.5)

    if hasLOS == 1:
        PLdB = PL_LOS + np.random.normal(loc=0.0, scale=sigma1, size=None)
    else:
        PLdB = max(PL_LOS, PL_NLOS) + np.random.normal(loc=0.0, scale=sigma2, size=None)

    # O2I penetration loss
    # Refer to Table 7.4.3-1 and 7.4.3-2
    Lglass = 2 + 0.2 * (fc * 1e-9)
    Lconcrete = 5 + 4 * (fc * 1e-9)
    PL_tw = 5 - 10 * np.log10(0.3 * pow(10, - 0.1 * Lglass) + 0.7 * pow(10, - 0.1 * Lconcrete))
    PL_in = 0.5 * d2D_in
    PL_O2I = PL_tw + PL_in + np.random.normal(loc=0.0, scale=4.4, size=None)

    if is_indoor == 1:
        PLdB = PLdB + PL_O2I

    # Step 2 calculate the antenna gain
    # Refer to Table 7.3-1
    AHm = 25
    AH = - min(12 * pow((bs_azi - az) / bw_azi, 2), AHm)
    AVm = 18
    tilt = np.degrees(np.arcsin(dis2D / dis3D))
    AV = - min(12 * pow((bs_tilt - tilt) / bw_tilt, 2), AVm)
    gain = 8 - min(- (AH + AV), AHm)

    # Step 3 combine path loss and antenna gain
    PL = PLdB - gain

    return PL


# For test

if __name__ == '__main__':
    g = Geod(ellps='WGS84')

    bs_lon = 116
    bs_lat = 32

    usr_h = 2
    bs_azi = 0
    bs_tilt = 90

    usr_lon = 116
    usr_lat = 32
    PL = calculate_path_loss(scenario='umi', bs_lon=bs_lon, bs_lat=bs_lat,
                             usr_lon=usr_lon, usr_lat=usr_lat, usr_h=usr_h,
                             bs_azi=bs_azi, bs_tilt=bs_tilt)
    _, _, d = g.inv(bs_lon, bs_lat, usr_lon, usr_lat)
    print(PL, d)
