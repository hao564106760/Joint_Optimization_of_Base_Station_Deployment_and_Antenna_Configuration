
'Generated protocol buffer code.'
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ......wolong.comm.input.v1 import config_pb2 as wolong_dot_comm_dot_input_dot_v1_dot_config__pb2
from ......wolong.comm.interaction.sim.v1 import coverage_pb2 as wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_coverage__pb2
from ......wolong.comm.interaction.sim.v1 import dynamic_pb2 as wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_dynamic__pb2
from ......wolong.comm.interaction.sim.v1 import energy_pb2 as wolong_dot_comm_dot_interaction_dot_sim_dot_v1_dot_energy__pb2
from ......wolong.comm.output.v1 import output_service_pb2 as wolong_dot_comm_dot_output_dot_v1_dot_output__service__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0wolong/comm/interaction/sim/v1/sim_service.proto\x12\x1ewolong.comm.interaction.sim.v1\x1a!wolong/comm/input/v1/config.proto\x1a-wolong/comm/interaction/sim/v1/coverage.proto\x1a,wolong/comm/interaction/sim/v1/dynamic.proto\x1a+wolong/comm/interaction/sim/v1/energy.proto\x1a*wolong/comm/output/v1/output_service.proto"\xad\x02\n\x07Control\x12/\n\x04step\x18\x01 \x01(\x0b2!.wolong.comm.input.v1.ControlStep\x12\x1e\n\x11optimize_interval\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\x0edisplay_guomao\x18\x03 \x01(\x08\x12\x16\n\x0ecoverage_range\x18\x04 \x01(\x01\x12\x19\n\x11handover_interval\x18\x05 \x01(\x05\x127\n\x0cchannel_type\x18\x06 \x01(\x0e2!.wolong.comm.input.v1.ChannelType\x127\n\x0cantenna_type\x18\x07 \x01(\x0e2!.wolong.comm.input.v1.AntennaTypeB\x14\n\x12_optimize_interval"\xb5\x02\n\nSimRequest\x12\x0b\n\x03job\x18\x01 \x01(\t\x12\x12\n\nstore_keep\x18\x02 \x01(\x08\x12C\n\roptimize_type\x18\x03 \x01(\x0e2,.wolong.comm.interaction.sim.v1.OptimizeType\x128\n\x07control\x18\x04 \x01(\x0b2\'.wolong.comm.interaction.sim.v1.Control\x121\n\x06output\x18\x05 \x01(\x0b2\x1c.wolong.comm.input.v1.OutputH\x00\x88\x01\x01\x126\n\x06action\x18\x06 \x01(\x0b2&.wolong.comm.interaction.sim.v1.Action\x12\x11\n\tis_output\x18\x08 \x01(\x08B\t\n\x07_output"\xf9\x01\n\x0bSimResponse\x127\n\x05grids\x18\x01 \x03(\x0b2(.wolong.comm.interaction.sim.v1.GridInfo\x12;\n\x07persons\x18\x02 \x03(\x0b2*.wolong.comm.interaction.sim.v1.PersonInfo\x12>\n\x08conserve\x18\x03 \x01(\x0b2,.wolong.comm.interaction.sim.v1.ConserveInfo\x124\n\x06output\x18\x04 \x03(\x0b2$.wolong.comm.output.v1.OutputRequest"\xba\x01\n\tBsControl\x12\x0f\n\x07base_id\x18\x01 \x01(\x05\x12\x16\n\tmax_power\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x1a\n\rfreq_range_id\x18\x03 \x01(\x05H\x01\x88\x01\x01\x12\x14\n\x07azimuth\x18\x04 \x01(\x01H\x02\x88\x01\x01\x12\x17\n\ndown_angle\x18\x05 \x01(\x01H\x03\x88\x01\x01B\x0c\n\n_max_powerB\x10\n\x0e_freq_range_idB\n\n\x08_azimuthB\r\n\x0b_down_angle"\x95\x02\n\x06Action\x12A\n\tcoverages\x18\x01 \x03(\x0b2..wolong.comm.interaction.sim.v1.CoverageAction\x12?\n\x08dynamics\x18\x02 \x03(\x0b2-.wolong.comm.interaction.sim.v1.DynamicAction\x12E\n\rconservations\x18\x03 \x01(\x0b2..wolong.comm.interaction.sim.v1.ConserveAction\x12@\n\rbase_controls\x18\x04 \x03(\x0b2).wolong.comm.interaction.sim.v1.BsControl"\xba\x02\n\x0fStartSimRequest\x12\x0b\n\x03job\x18\x02 \x01(\t\x12\x12\n\nstore_keep\x18\x07 \x01(\x08\x12C\n\roptimize_type\x18\x03 \x01(\x0e2,.wolong.comm.interaction.sim.v1.OptimizeType\x128\n\x07control\x18\x04 \x01(\x0b2\'.wolong.comm.interaction.sim.v1.Control\x121\n\x06output\x18\x05 \x01(\x0b2\x1c.wolong.comm.input.v1.OutputH\x00\x88\x01\x01\x126\n\x06action\x18\x06 \x01(\x0b2&.wolong.comm.interaction.sim.v1.Action\x12\x11\n\tis_output\x18\x08 \x01(\x08B\t\n\x07_output"\x12\n\x10StartSimResponse""\n\x13GetJobStatusRequest\x12\x0b\n\x03job\x18\x01 \x01(\t"A\n\x14GetJobStatusResponse\x12\r\n\x05start\x18\x01 \x01(\x05\x12\r\n\x05total\x18\x02 \x01(\x05\x12\x0b\n\x03now\x18\x03 \x01(\x05*~\n\x0cOptimizeType\x12\x1d\n\x19OPTIMIZE_TYPE_UNSPECIFIED\x10\x00\x12\x19\n\x15OPTIMIZE_TYPE_DYNAMIC\x10\x01\x12\x1a\n\x16OPTIMIZE_TYPE_COVERAGE\x10\x02\x12\x18\n\x14OPTIMIZE_TYPE_ENERGE\x10\x032\xd6\x02\n\nSimService\x12^\n\x03Sim\x12*.wolong.comm.interaction.sim.v1.SimRequest\x1a+.wolong.comm.interaction.sim.v1.SimResponse\x12m\n\x08StartSim\x12/.wolong.comm.interaction.sim.v1.StartSimRequest\x1a0.wolong.comm.interaction.sim.v1.StartSimResponse\x12y\n\x0cGetJobStatus\x123.wolong.comm.interaction.sim.v1.GetJobStatusRequest\x1a4.wolong.comm.interaction.sim.v1.GetJobStatusResponseb\x06proto3')
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'wolong.comm.interaction.sim.v1.sim_service_pb2', globals())
if (_descriptor._USE_C_DESCRIPTORS == False):
    DESCRIPTOR._options = None
    _OPTIMIZETYPE._serialized_start = 2078
    _OPTIMIZETYPE._serialized_end = 2204
    _CONTROL._serialized_start = 302
    _CONTROL._serialized_end = 603
    _SIMREQUEST._serialized_start = 606
    _SIMREQUEST._serialized_end = 915
    _SIMRESPONSE._serialized_start = 918
    _SIMRESPONSE._serialized_end = 1167
    _BSCONTROL._serialized_start = 1170
    _BSCONTROL._serialized_end = 1356
    _ACTION._serialized_start = 1359
    _ACTION._serialized_end = 1636
    _STARTSIMREQUEST._serialized_start = 1639
    _STARTSIMREQUEST._serialized_end = 1953
    _STARTSIMRESPONSE._serialized_start = 1955
    _STARTSIMRESPONSE._serialized_end = 1973
    _GETJOBSTATUSREQUEST._serialized_start = 1975
    _GETJOBSTATUSREQUEST._serialized_end = 2009
    _GETJOBSTATUSRESPONSE._serialized_start = 2011
    _GETJOBSTATUSRESPONSE._serialized_end = 2076
    _SIMSERVICE._serialized_start = 2207
    _SIMSERVICE._serialized_end = 2549
