# Tra - Distributed File Synchronization System

Tra is a distributed file synchronization system designed to synchronize files across multiple replicas without requiring a specific synchronization order. The system efficiently handles conflicts, minimizes storage for file metadata, and reduces bandwidth usage by transferring only changes.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Creating the Protobuf File](#creating-the-protobuf-file)
- [Generating Python Code from Protobuf](#generating-python-code-from-protobuf)
- [Implementation](#implementation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [License](#license)

## Prerequisites
- Python 3.x
- gRPC and Protocol Buffers for Python
- Install the necessary packages:
```bash
pip install grpcio grpcio-tools
```
## Creating the Protobuf File
Create a file named tra.proto in the root directory of your project.

## Generating Python Code from Protobuf
Run the following command to generate the necessary Python files from the tra.proto file:

```bash
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. tra.proto
```
This command will generate tra_pb2.py and tra_pb2_grpc.py, which contain the necessary classes and methods for implementing gRPC communication.

## Implementation
The implementation consists of two main components:

Server: Handles file synchronization requests.
Client: Sends requests to the server to sync files and directories.

```bash
python server.py
```
Run the Client: Open another terminal and run:
```bash
python client.py
```
## Usage
Place the file example.txt in the same directory as client.py.
Create a directory named example_dir and populate it with some test files.
Run the server and client to synchronize files and directories.

