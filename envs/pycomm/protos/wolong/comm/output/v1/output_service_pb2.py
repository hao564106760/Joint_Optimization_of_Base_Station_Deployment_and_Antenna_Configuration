
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....wolong.comm.output.v1 import output_pb2 as wolong_dot_comm_dot_output_dot_v1_dot_output__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*wolong/comm/output/v1/output_service.proto\x12\x15wolong.comm.output.v1\x1a"wolong/comm/output/v1/output.proto"\xd1\x02\n\rOutputRequest\x12\x0c\n\x04step\x18\x01 \x01(\x05\x129\n\rbase_stations\x18\x02 \x03(\x0b2".wolong.comm.output.v1.BaseStation\x12(\n\x04aois\x18\x07 \x03(\x0b2\x1a.wolong.comm.output.v1.Aoi\x12/\n\x07heatmap\x18\x03 \x01(\x0b2\x1e.wolong.comm.output.v1.Heatmap\x125\n\rsmall_heatmap\x18\x04 \x01(\x0b2\x1e.wolong.comm.output.v1.Heatmap\x12.\n\x07persons\x18\x05 \x03(\x0b2\x1d.wolong.comm.output.v1.Person\x125\n\nstatistics\x18\x06 \x01(\x0b2!.wolong.comm.output.v1.Statistics"\x10\n\x0eOutputResponse2f\n\rOutputService\x12U\n\x06Output\x12$.wolong.comm.output.v1.OutputRequest\x1a%.wolong.comm.output.v1.OutputResponseb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.output.v1.output_service_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _OUTPUTREQUEST._serialized_start = 106
    _OUTPUTREQUEST._serialized_end = 443
    _OUTPUTRESPONSE._serialized_start = 445
    _OUTPUTRESPONSE._serialized_end = 461
    _OUTPUTSERVICE._serialized_start = 463
    _OUTPUTSERVICE._serialized_end = 565
