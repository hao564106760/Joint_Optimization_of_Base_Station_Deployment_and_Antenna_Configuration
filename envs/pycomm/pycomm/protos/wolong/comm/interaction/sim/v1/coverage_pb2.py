
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......wolong.comm.interaction.sim.v1 import common_pb2 as wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-wolong/comm/interaction/sim/v1/coverage.proto\x12\x1ewolong.comm.interaction.sim.v1\x1a+wolong/comm/interaction/sim/v1/common.proto"\xc2\x01\n\x0eCoverageAction\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06bs_azi\x18\x02 \x01(\x01\x12\x0f\n\x07bs_tilt\x18\x03 \x01(\x01\x12\x0e\n\x06bw_azi\x18\x04 \x01(\x01\x12\x0f\n\x07bw_tilt\x18\x05 \x01(\x01\x12M\n\x10bs_control_state\x18\x06 \x01(\x0e2..wolong.comm.interaction.sim.v1.BsControlStateH\x00\x88\x01\x01B\x13\n\x11_bs_control_state"C\n\x0eCoverageReward\x12\x10\n\x08coverage\x18\x01 \x01(\x08\x12\x11\n\tmean_rate\x18\x02 \x01(\x01\x12\x0c\n\x04open\x18\x03 \x01(\x08"B\n\x07BsState\x12\x0f\n\x07signals\x18\x01 \x03(\x01\x12\x13\n\x0buser_number\x18\x02 \x01(\x05\x12\x11\n\tis_indoor\x18\x03 \x01(\x08"\x8e\x01\n\x08GridInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x126\n\x05state\x18\x02 \x01(\x0b2\'.wolong.comm.interaction.sim.v1.BsState\x12>\n\x06reward\x18\x03 \x01(\x0b2..wolong.comm.interaction.sim.v1.CoverageRewardb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.interaction.sim.v1.coverage_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _COVERAGEACTION._serialized_start = 127
    _COVERAGEACTION._serialized_end = 321
    _COVERAGEREWARD._serialized_start = 323
    _COVERAGEREWARD._serialized_end = 390
    _BSSTATE._serialized_start = 392
    _BSSTATE._serialized_end = 458
    _GRIDINFO._serialized_start = 461
    _GRIDINFO._serialized_end = 603
