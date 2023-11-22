
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......wolong.geo.v2 import geo_pb2 as wolong_dot_geo_dot_v2_dot_geo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,wolong/comm/interaction/sim/v1/dynamic.proto\x12\x1ewolong.comm.interaction.sim.v1\x1a\x17wolong/geo/v2/geo.proto"H\n\nAllocation\x12\x17\n\x0fbase_station_id\x18\x01 \x01(\x05\x12\x12\n\nchannel_id\x18\x02 \x01(\x05\x12\r\n\x05power\x18\x03 \x01(\x01"l\n\rDynamicAction\x12\n\n\x02id\x18\x01 \x01(\x05\x12;\n\x07actions\x18\x02 \x03(\x0b2*.wolong.comm.interaction.sim.v1.Allocation\x12\x12\n\nsteps_next\x18\x03 \x01(\x05"5\n\rDynamicReward\x12\x0c\n\x04flow\x18\x01 \x01(\x01\x12\x16\n\x0esatisfied_flow\x18\x02 \x01(\x01"\x8f\x01\n\x0bPersonState\x12.\n\x0bxy_position\x18\x01 \x01(\x0b2\x19.wolong.geo.v2.XYPosition\x12\x0e\n\x06demand\x18\x02 \x01(\x01\x12\x13\n\x0bremain_time\x18\x03 \x01(\x01\x12\x16\n\x0esatisfied_flow\x18\x04 \x01(\x01\x12\x13\n\x0bnext_demand\x18\x05 \x01(\x01"\x93\x01\n\nPersonInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12:\n\x05state\x18\x02 \x01(\x0b2+.wolong.comm.interaction.sim.v1.PersonState\x12=\n\x06reward\x18\x03 \x01(\x0b2-.wolong.comm.interaction.sim.v1.DynamicRewardb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.interaction.sim.v1.dynamic_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _ALLOCATION._serialized_start = 105
    _ALLOCATION._serialized_end = 177
    _DYNAMICACTION._serialized_start = 179
    _DYNAMICACTION._serialized_end = 287
    _DYNAMICREWARD._serialized_start = 289
    _DYNAMICREWARD._serialized_end = 342
    _PERSONSTATE._serialized_start = 345
    _PERSONSTATE._serialized_end = 488
    _PERSONINFO._serialized_start = 491
    _PERSONINFO._serialized_end = 638
