# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import json_pb2 as json__pb2


class jsonServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.JsonFunc = channel.unary_unary(
                '/hello.jsonService/JsonFunc',
                request_serializer=json__pb2.jsonRequest.SerializeToString,
                response_deserializer=json__pb2.jsonResponse.FromString,
                )


class jsonServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def JsonFunc(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_jsonServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'JsonFunc': grpc.unary_unary_rpc_method_handler(
                    servicer.JsonFunc,
                    request_deserializer=json__pb2.jsonRequest.FromString,
                    response_serializer=json__pb2.jsonResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'hello.jsonService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class jsonService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def JsonFunc(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/hello.jsonService/JsonFunc',
            json__pb2.jsonRequest.SerializeToString,
            json__pb2.jsonResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)