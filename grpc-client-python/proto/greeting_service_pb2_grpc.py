# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import proto.greeting_service_pb2 as greeting__service__pb2


class GreetingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.greeting = channel.unary_stream(
                '/com.example.grpc.GreetingService/greeting',
                request_serializer=greeting__service__pb2.HelloRequest.SerializeToString,
                response_deserializer=greeting__service__pb2.HelloResponse.FromString,
                )


class GreetingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def greeting(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'greeting': grpc.unary_stream_rpc_method_handler(
                    servicer.greeting,
                    request_deserializer=greeting__service__pb2.HelloRequest.FromString,
                    response_serializer=greeting__service__pb2.HelloResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.example.grpc.GreetingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def greeting(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/com.example.grpc.GreetingService/greeting',
            greeting__service__pb2.HelloRequest.SerializeToString,
            greeting__service__pb2.HelloResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
