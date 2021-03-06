import grpc

from proto import greeting_service_pb2_grpc, greeting_service_pb2


def run():
    with grpc.insecure_channel("localhost:8080") as channel:
        stub = greeting_service_pb2_grpc.GreetingServiceStub(channel)
        for response in stub.greeting(greeting_service_pb2.HelloRequest(name='test')):
            print(f"Greeting from server: " + response.greeting)


if __name__ == '__main__':
    run()
