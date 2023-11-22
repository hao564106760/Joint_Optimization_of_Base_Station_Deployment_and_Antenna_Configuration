
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from .....wolong.geo.v2 import geo_pb2 as wolong_dot_geo_dot_v2_dot_geo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwolong/comm/input/v1/comm.proto\x12\x14wolong.comm.input.v1\x1a\x17wolong/geo/v2/geo.proto"\xf1\x02\n\x04Node\x12\n\n\x02id\x18\x01 \x01(\x05\x12,\n\x04type\x18\x02 \x01(\x0e2\x1e.wolong.comm.input.v1.NodeType\x12\x11\n\tparent_id\x18\x03 \x01(\x05\x12\x14\n\x0cchildren_ids\x18\x04 \x03(\x05\x12.\n\x08position\x18\x05 \x01(\x0b2\x17.wolong.geo.v2.PositionH\x00\x88\x01\x01\x12\x13\n\x06aoi_id\x18\x06 \x01(\x05H\x01\x88\x01\x01\x12\x1a\n\rfreq_range_id\x18\x07 \x01(\x05H\x02\x88\x01\x01\x12E\n\x11base_station_type\x18\x08 \x01(\x0e2%.wolong.comm.input.v1.BaseStationTypeH\x03\x88\x01\x01\x12\x13\n\x06height\x18\t \x01(\x01H\x04\x88\x01\x01B\x0b\n\t_positionB\t\n\x07_aoi_idB\x10\n\x0e_freq_range_idB\x14\n\x12_base_station_typeB\t\n\x07_height"V\n\rRepairStation\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0e\n\x06aoi_id\x18\x02 \x01(\x05\x12)\n\x08position\x18\x03 \x01(\x0b2\x17.wolong.geo.v2.Position"=\n\x04Pump\x12\n\n\x02id\x18\x01 \x01(\x05\x12)\n\x08position\x18\x02 \x01(\x0b2\x17.wolong.geo.v2.Position")\n\nCommDemand\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07demands\x18\x02 \x03(\x01"\x9b\x01\n\x05Nodes\x12)\n\x05nodes\x18\x01 \x03(\x0b2\x1a.wolong.comm.input.v1.Node\x12<\n\x0frepair_stations\x18\x02 \x03(\x0b2#.wolong.comm.input.v1.RepairStation\x12)\n\x05pumps\x18\x03 \x03(\x0b2\x1a.wolong.comm.input.v1.Pump"6\n\x08PathLoss\x12\x17\n\x0fbase_station_id\x18\x01 \x01(\x05\x12\x11\n\tpath_loss\x18\x02 \x01(\x01"Q\n\x0eRayTracingLoss\x12\n\n\x02id\x18\x01 \x01(\x05\x123\n\x0bpath_losses\x18\x02 \x03(\x0b2\x1e.wolong.comm.input.v1.PathLoss"E\n\x0bCommDemands\x126\n\x0ccomm_demands\x18\x01 \x03(\x0b2 .wolong.comm.input.v1.CommDemand"T\n\x10RayTracingLosses\x12@\n\x12ray_tracing_losses\x18\x01 \x03(\x0b2$.wolong.comm.input.v1.RayTracingLoss"\x1f\n\x08LossGrid\x12\x13\n\x0bgrid_losses\x18\x01 \x03(\x01"\xa7\x01\n\tLossBlock\x12F\n\x0cblock_losses\x18\x01 \x03(\x0b20.wolong.comm.input.v1.LossBlock.BlockLossesEntry\x1aR\n\x10BlockLossesEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12-\n\x05value\x18\x02 \x01(\x0b2\x1e.wolong.comm.input.v1.LossGrid:\x028\x01"O\n\x10RayTracingBlocks\x12;\n\x12ray_tracing_blocks\x18\x01 \x03(\x0b2\x1f.wolong.comm.input.v1.LossBlock*p\n\x08NodeType\x12\x19\n\x15NODE_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12NODE_TYPE_INTERNET\x10\x01\x12\x15\n\x11NODE_TYPE_GATEWAY\x10\x02\x12\x1a\n\x16NODE_TYPE_BASE_STATION\x10\x03*q\n\x0fBaseStationType\x12!\n\x1dBASE_STATION_TYPE_UNSPECIFIED\x10\x00\x12\x1c\n\x18BASE_STATION_TYPE_INDOOR\x10\x01\x12\x1d\n\x19BASE_STATION_TYPE_OUTDOOR\x10\x02b\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.input.v1.comm_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _LOSSBLOCK_BLOCKLOSSESENTRY._options = None
    _LOSSBLOCK_BLOCKLOSSESENTRY._serialized_options = b'8\x01'
    _NODETYPE._serialized_start = 1386
    _NODETYPE._serialized_end = 1498
    _BASESTATIONTYPE._serialized_start = 1500
    _BASESTATIONTYPE._serialized_end = 1613
    _NODE._serialized_start = 83
    _NODE._serialized_end = 452
    _REPAIRSTATION._serialized_start = 454
    _REPAIRSTATION._serialized_end = 540
    _PUMP._serialized_start = 542
    _PUMP._serialized_end = 603
    _COMMDEMAND._serialized_start = 605
    _COMMDEMAND._serialized_end = 646
    _NODES._serialized_start = 649
    _NODES._serialized_end = 804
    _PATHLOSS._serialized_start = 806
    _PATHLOSS._serialized_end = 860
    _RAYTRACINGLOSS._serialized_start = 862
    _RAYTRACINGLOSS._serialized_end = 943
    _COMMDEMANDS._serialized_start = 945
    _COMMDEMANDS._serialized_end = 1014
    _RAYTRACINGLOSSES._serialized_start = 1016
    _RAYTRACINGLOSSES._serialized_end = 1100
    _LOSSGRID._serialized_start = 1102
    _LOSSGRID._serialized_end = 1133
    _LOSSBLOCK._serialized_start = 1136
    _LOSSBLOCK._serialized_end = 1303
    _LOSSBLOCK_BLOCKLOSSESENTRY._serialized_start = 1221
    _LOSSBLOCK_BLOCKLOSSESENTRY._serialized_end = 1303
    _RAYTRACINGBLOCKS._serialized_start = 1305
    _RAYTRACINGBLOCKS._serialized_end = 1384
