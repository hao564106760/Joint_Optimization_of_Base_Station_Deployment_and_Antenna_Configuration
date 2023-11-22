
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+wolong/comm/interaction/sim/v1/common.proto\x12\x1ewolong.comm.interaction.sim.v1*\x8d\x01\n\x10CellControlState\x12"\n\x1eCELL_CONTROL_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x17CELL_CONTROL_STATE_OPEN\x10\x01\x12\x1c\n\x18CELL_CONTROL_STATE_SLEEP\x10\x02\x12\x1a\n\x16CELL_CONTROL_STATE_OFF\x10\x03*i\n\x0eBsControlState\x12 \n\x1cBS_CONTROL_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15BS_CONTROL_STATE_OPEN\x10\x01\x12\x1a\n\x16BS_CONTROL_STATE_CLOSE\x10\x02b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.interaction.sim.v1.common_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _CELLCONTROLSTATE._serialized_start = 80
    _CELLCONTROLSTATE._serialized_end = 221
    _BSCONTROLSTATE._serialized_start = 223
    _BSCONTROLSTATE._serialized_end = 328
