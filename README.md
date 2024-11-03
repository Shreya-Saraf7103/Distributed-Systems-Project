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
