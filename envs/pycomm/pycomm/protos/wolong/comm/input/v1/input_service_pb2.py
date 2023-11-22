
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....wolong.map.v2 import map_pb2 as wolong_dot_map_dot_v2_dot_map__pb2
from .....wolong.comm.input.v1 import config_pb2 as wolong_dot_comm_dot_input_dot_v1_dot_config__pb2
from .....wolong.comm.input.v1 import comm_pb2 as wolong_dot_comm_dot_input_dot_v1_dot_comm__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(wolong/comm/input/v1/input_service.proto\x12\x14wolong.comm.input.v1\x1a\x17wolong/map/v2/map.proto\x1a!wolong/comm/input/v1/config.proto\x1a\x1fwolong/comm/input/v1/comm.proto"\r\n\x0bInitRequest"\x84\x03\n\x0cInitResponse\x12&\n\x03log\x18\x01 \x01(\x0b2\x19.wolong.comm.input.v1.Log\x12.\n\x07control\x18\x02 \x01(\x0b2\x1d.wolong.comm.input.v1.Control\x12\x13\n\x0bsim_address\x18\x03 \x01(\t\x12\x1f\n\x03map\x18\x04 \x01(\x0b2\x12.wolong.map.v2.Map\x12.\n\tcomm_topo\x18\x05 \x01(\x0b2\x1b.wolong.comm.input.v1.Nodes\x127\n\x0ccomm_demands\x18\x06 \x01(\x0b2!.wolong.comm.input.v1.CommDemands\x12B\n\x12ray_tracing_losses\x18\x07 \x01(\x0b2&.wolong.comm.input.v1.RayTracingLosses\x129\n\routput_switch\x18\x08 \x01(\x0b2".wolong.comm.input.v1.OutputSwitch2_\n\x0cInputService\x12O\n\x04Init\x12!.wolong.comm.input.v1.InitRequest\x1a".wolong.comm.input.v1.InitResponse"\x00b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.input.v1.input_service_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _INITREQUEST._serialized_start = 159
    _INITREQUEST._serialized_end = 172
    _INITRESPONSE._serialized_start = 175
    _INITRESPONSE._serialized_end = 563
    _INPUTSERVICE._serialized_start = 565
    _INPUTSERVICE._serialized_end = 660
