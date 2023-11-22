
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......wolong.comm.interaction.sim.v1 import common_pb2 as wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+wolong/comm/interaction/sim/v1/energy.proto\x12\x1ewolong.comm.interaction.sim.v1\x1a+wolong/comm/interaction/sim/v1/common.proto"\xe6\x03\n\rConserveState\x12\x0e\n\x06bs_num\x18\x01 \x01(\x05\x12\x11\n\tbbu_power\x18\x02 \x03(\x01\x12\x10\n\x08cell_num\x18\x03 \x01(\x05\x12\x15\n\rcell_capacity\x18\x04 \x03(\x01\x12\x18\n\x10cell_sleep_power\x18\x05 \x03(\x01\x12F\n\x0fcell_power_coef\x18\x06 \x03(\x0b2-.wolong.comm.interaction.sim.v1.CellPowerCoef\x12F\n\x0fbigraph_cell_bs\x18\x07 \x03(\x0b2-.wolong.comm.interaction.sim.v1.BigraphCellBs\x12N\n\x13bigraph_demand_cell\x18\x08 \x03(\x0b21.wolong.comm.interaction.sim.v1.BigraphDemandCell\x126\n\x06demand\x18\t \x03(\x0b2&.wolong.comm.interaction.sim.v1.Demand\x12W\n\x18air_condition_power_coef\x18\n \x03(\x0b25.wolong.comm.interaction.sim.v1.AirConditionPowerCoef")\n\x06Demand\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0e\n\x06demand\x18\x02 \x01(\x01"\xca\x01\n\x0eConserveAction\x12@\n\x0ccell_actions\x18\x01 \x03(\x0b2*.wolong.comm.interaction.sim.v1.CellAction\x12<\n\nbs_actions\x18\x02 \x03(\x0b2(.wolong.comm.interaction.sim.v1.BsAction\x128\n\x07traffic\x18\x03 \x03(\x0b2\'.wolong.comm.interaction.sim.v1.Traffic"k\n\nCellAction\x12\x0f\n\x07cell_id\x18\x01 \x01(\x05\x12L\n\x12cell_control_state\x18\x02 \x01(\x0e20.wolong.comm.interaction.sim.v1.CellControlState"c\n\x08BsAction\x12\r\n\x05bs_id\x18\x01 \x01(\x05\x12H\n\x10bs_control_state\x18\x02 \x01(\x0e2..wolong.comm.interaction.sim.v1.BsControlState">\n\x0eConserveReward\x12\x18\n\x10power_save_ratio\x18\x01 \x01(\x01\x12\x12\n\npower_save\x18\x02 \x01(\x01",\n\rCellPowerCoef\x12\r\n\x05slope\x18\x01 \x01(\x01\x12\x0c\n\x04bias\x18\x02 \x01(\x01"/\n\rBigraphCellBs\x12\x0f\n\x07cell_id\x18\x01 \x01(\x05\x12\r\n\x05bs_id\x18\x02 \x01(\x05"5\n\x11BigraphDemandCell\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07cell_id\x18\x02 \x01(\x05"4\n\x15AirConditionPowerCoef\x12\r\n\x05slope\x18\x01 \x01(\x01\x12\x0c\n\x04bias\x18\x02 \x01(\x01"<\n\x07Traffic\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07cell_id\x18\x02 \x01(\x05\x12\x0f\n\x07traffic\x18\x03 \x01(\x01"\x8c\x01\n\x0cConserveInfo\x12<\n\x05state\x18\x01 \x01(\x0b2-.wolong.comm.interaction.sim.v1.ConserveState\x12>\n\x06reward\x18\x03 \x01(\x0b2..wolong.comm.interaction.sim.v1.ConserveRewardb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.interaction.sim.v1.energy_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _CONSERVESTATE._serialized_start = 125
    _CONSERVESTATE._serialized_end = 611
    _DEMAND._serialized_start = 613
    _DEMAND._serialized_end = 654
    _CONSERVEACTION._serialized_start = 657
    _CONSERVEACTION._serialized_end = 859
    _CELLACTION._serialized_start = 861
    _CELLACTION._serialized_end = 968
    _BSACTION._serialized_start = 970
    _BSACTION._serialized_end = 1069
    _CONSERVEREWARD._serialized_start = 1071
    _CONSERVEREWARD._serialized_end = 1133
    _CELLPOWERCOEF._serialized_start = 1135
    _CELLPOWERCOEF._serialized_end = 1179
    _BIGRAPHCELLBS._serialized_start = 1181
    _BIGRAPHCELLBS._serialized_end = 1228
    _BIGRAPHDEMANDCELL._serialized_start = 1230
    _BIGRAPHDEMANDCELL._serialized_end = 1283
    _AIRCONDITIONPOWERCOEF._serialized_start = 1285
    _AIRCONDITIONPOWERCOEF._serialized_end = 1337
    _TRAFFIC._serialized_start = 1339
    _TRAFFIC._serialized_end = 1399
    _CONSERVEINFO._serialized_start = 1402
    _CONSERVEINFO._serialized_end = 1542
