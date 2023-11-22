
'Client and server classes corresponding to protobuf-defined services.'
import grpc
from .....wolong.comm.input.v1 import input_service_pb2 as wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2

class InputServiceStub(object):
    'Missing associated documentation comment in .proto file.'

    def __init__(self, channel):
        'Constructor.\n\n        Args:\n            channel: A grpc.Channel.\n        '
        self.Init = channel.unary_unary('/wolong.comm.input.v1.InputService/Init', request_serializer=wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2.InitRequest.SerializeToString, response_deserializer=wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2.InitResponse.FromString)

class InputServiceServicer(object):
    'Missing associated documentation comment in .proto file.'

    def Init(self, request, context):
        'Missing associated documentation comment in .proto file.'
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_InputServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Init': grpc.unary_unary_rpc_method_handler(servicer.Init, request_deserializer=wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2.InitRequest.FromString, response_serializer=wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2.InitResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('wolong.comm.input.v1.InputService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class InputService(object):
    'Missing associated documentation comment in .proto file.'

    @staticmethod
    def Init(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/wolong.comm.input.v1.InputService/Init', wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2.InitRequest.SerializeToString, wolong_dot_comm_dot_input_dot_v1_dot_input__service__pb2.InitResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
