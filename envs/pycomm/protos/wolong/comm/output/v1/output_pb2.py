
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....wolong.comm.input.v1 import comm_pb2 as wolong_dot_comm_dot_input_dot_v1_dot_comm__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"wolong/comm/output/v1/output.proto\x12\x15wolong.comm.output.v1\x1a\x1fwolong/comm/input/v1/comm.proto"\xea\x03\n\x0bBaseStation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bdemand_flow\x18\x02 \x01(\x01\x12\x13\n\x0bactual_flow\x18\x03 \x01(\x01\x12\x12\n\nnum_agents\x18\x04 \x01(\x05\x12\x17\n\x0funsatisfied_num\x18\x05 \x01(\x05\x12\x15\n\rsatisfied_num\x18\x06 \x01(\x05\x12\x12\n\noutage_num\x18\x07 \x01(\x05\x12\x16\n\x0etransmit_power\x18\x08 \x01(\x01\x12\x1c\n\x14resource_block_ratio\x18\t \x01(\x01\x12\x19\n\x11energy_efficiency\x18\n \x01(\x01\x12A\n\x0bload_status\x18\x0b \x01(\x0e2,.wolong.comm.output.v1.BaseStationLoadStatus\x12\x11\n\trate_comm\x18\x0c \x01(\x01\x12\x15\n\rfreq_range_id\x18\r \x01(\x05\x12\x19\n\x11power_consumption\x18\x0e \x01(\x01\x12@\n\x11base_station_type\x18\x0f \x01(\x0e2%.wolong.comm.input.v1.BaseStationType\x12\x11\n\tmax_power\x18\x10 \x01(\x01\x12\x0e\n\x06bs_azi\x18\x11 \x01(\x01\x12\x0f\n\x07bs_tilt\x18\x12 \x01(\x01"\xac\x01\n\x03Aoi\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bdemand_flow\x18\x02 \x01(\x01\x12\x13\n\x0bactual_flow\x18\x03 \x01(\x01\x12\x12\n\nnum_agents\x18\x04 \x01(\x05\x12\x12\n\noutage_num\x18\x05 \x01(\x05\x12\x15\n\rsatisfied_num\x18\x06 \x01(\x05\x12\x17\n\x0funsatisfied_num\x18\x07 \x01(\x05\x12\x17\n\x0factive_user_num\x18\x08 \x01(\x05"\xb0\x01\n\x07Heatmap\x12\x10\n\x08num_rows\x18\x01 \x01(\x05\x12\x13\n\x0bnum_columns\x18\x02 \x01(\x05\x12\x10\n\x08strength\x18\x03 \x03(\x01\x12\x17\n\x0fbase_station_id\x18\x04 \x03(\x05\x12\x15\n\rfreq_range_id\x18\x05 \x03(\x05\x12\x0c\n\x04rate\x18\x06 \x03(\x01\x12\x19\n\x11unsatisfied_ratio\x18\x07 \x03(\x01\x12\x13\n\x0bstrength_3d\x18\x08 \x03(\x01"\xb1\x03\n\x06Person\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0bdemand_rate\x18\x02 \x01(\x01\x12\x13\n\x0bactual_rate\x18\x03 \x01(\x01\x12B\n\x0econnect_status\x18\x04 \x01(\x0e2*.wolong.comm.output.v1.PersonConnectStatus\x12@\n\rdemand_status\x18\x05 \x01(\x0e2).wolong.comm.output.v1.PersonDemandStatus\x12\x10\n\x08strength\x18\x06 \x01(\x01\x12\x17\n\x0fbase_station_id\x18\x07 \x01(\x05\x12\x16\n\x0efreq_range_ids\x18\x08 \x03(\x05\x12\x16\n\x0ereceived_power\x18\t \x01(\x01\x12\x14\n\x0cnum_channels\x18\n \x01(\x05\x12\x13\n\x0bdemand_flow\x18\x0b \x01(\x01\x12\x13\n\x0bactual_flow\x18\x0c \x01(\x01\x126\n\x0bperson_type\x18\r \x01(\x0e2!.wolong.comm.output.v1.PersonType\x12\x0b\n\x03lng\x18\x0e \x01(\x01\x12\x0b\n\x03lat\x18\x0f \x01(\x01"\xa3\x03\n\nStatistics\x12\x11\n\tnum_agent\x18\x01 \x01(\x05\x12\x1b\n\x13num_satisfied_agent\x18\x02 \x01(\x05\x12\x1d\n\x15num_unsatisfied_agent\x18\x03 \x01(\x05\x12\x18\n\x10num_outage_agent\x18\x04 \x01(\x05\x12\x18\n\x10num_active_agent\x18\x05 \x01(\x05\x12\x19\n\x11num_connect_agent\x18\x06 \x01(\x05\x12\x13\n\x0bdemand_flow\x18\x07 \x01(\x01\x12\x13\n\x0bactual_flow\x18\x08 \x01(\x01\x12\x18\n\x10num_base_station\x18\t \x01(\x05\x12"\n\x1anum_high_load_base_station\x18\n \x01(\x05\x12 \n\x18num_ok_load_base_station\x18\x0b \x01(\x05\x12!\n\x19num_low_load_base_station\x18\x0c \x01(\x05\x12\x19\n\x11power_consumption\x18\r \x01(\x01\x12\x15\n\rcoverage_rate\x18\x0e \x01(\x01\x12\x18\n\x10power_save_ratio\x18\x0f \x01(\x01*\xa7\x01\n\x15BaseStationLoadStatus\x12(\n$BASE_STATION_LOAD_STATUS_UNSPECIFIED\x10\x00\x12!\n\x1dBASE_STATION_LOAD_STATUS_HIGH\x10\x01\x12\x1f\n\x1bBASE_STATION_LOAD_STATUS_OK\x10\x02\x12 \n\x1cBASE_STATION_LOAD_STATUS_LOW\x10\x03*^\n\nPersonType\x12\x1b\n\x17PERSON_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13PERSON_TYPE_VEHICLE\x10\x01\x12\x1a\n\x16PERSON_TYPE_PEDESTRIAN\x10\x02*|\n\x13PersonConnectStatus\x12%\n!PERSON_CONNECT_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERSON_CONNECT_STATUS_OK\x10\x01\x12 \n\x1cPERSON_CONNECT_STATUS_OUTAGE\x10\x02*\xa1\x01\n\x12PersonDemandStatus\x12$\n PERSON_DEMAND_STATUS_UNSPECIFIED\x10\x00\x12"\n\x1ePERSON_DEMAND_STATUS_SATISFIED\x10\x01\x12$\n PERSON_DEMAND_STATUS_UNSATISFIED\x10\x02\x12\x1b\n\x17PERSON_DEMAND_STATUS_NO\x10\x03b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.output.v1.output_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _BASESTATIONLOADSTATUS._serialized_start = 1800
    _BASESTATIONLOADSTATUS._serialized_end = 1967
    _PERSONTYPE._serialized_start = 1969
    _PERSONTYPE._serialized_end = 2063
    _PERSONCONNECTSTATUS._serialized_start = 2065
    _PERSONCONNECTSTATUS._serialized_end = 2189
    _PERSONDEMANDSTATUS._serialized_start = 2192
    _PERSONDEMANDSTATUS._serialized_end = 2353
    _BASESTATION._serialized_start = 95
    _BASESTATION._serialized_end = 585
    _AOI._serialized_start = 588
    _AOI._serialized_end = 760
    _HEATMAP._serialized_start = 763
    _HEATMAP._serialized_end = 939
    _PERSON._serialized_start = 942
    _PERSON._serialized_end = 1375
    _STATISTICS._serialized_start = 1378
    _STATISTICS._serialized_end = 1797
