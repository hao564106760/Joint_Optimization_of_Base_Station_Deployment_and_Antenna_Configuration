
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from ......wolong.comm.interaction.compute.v1 import compute_service_pb2 as wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2

class ComputeServiceStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.ComputeFacilityPower = channel.unary_unary('/wolong.comm.interaction.compute.v1.ComputeService/ComputeFacilityPower', request_serializer=wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2.ComputeFacilityPowerRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2.ComputeFacilityPowerResponse.FromString)

class ComputeServiceServicer(object):
    'Missing associated documentation comment in .proto file.'

    def ComputeFacilityPower(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ComputeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ComputeFacilityPower': grpc.unary_unary_rpc_method_handler(servicer.ComputeFacilityPower, request_deserializer=wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2.ComputeFacilityPowerRequest.FromString, response_serializer=wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2.ComputeFacilityPowerResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('wolong.comm.interaction.compute.v1.ComputeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class ComputeService(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def ComputeFacilityPower(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.interaction.compute.v1.ComputeService/ComputeFacilityPower', wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2.ComputeFacilityPowerRequest.SerializeToString, wolong_dot_comm_dot_interaction_dot_compute_dot_v1_dot_compute__service__pb2.ComputeFacilityPowerResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
