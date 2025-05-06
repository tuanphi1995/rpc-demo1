import grpc
import calculator_pb2
import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = calculator_pb2_grpc.CalculatorStub(channel)

response = stub.Add(calculator_pb2.AddRequest(a=10, b=5))
print("Result:", response.result)
