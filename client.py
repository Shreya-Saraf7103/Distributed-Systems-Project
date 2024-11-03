import grpc
import tra_pb2
import tra_pb2_grpc
import os

def sync_file(stub, file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist")
        return

    with open(file_path, 'rb') as file:
        content = file.read()
    last_modified = int(os.path.getmtime(file_path))

    request = tra_pb2.FileRequest(file_path=file_path, file_content=content, last_modified=last_modified)
    response = stub.SyncFile(request)
    print(f"SyncFile response: success={response.success}, message={response.message}")

def sync_directory_client(stub, directory_path):
    request = tra_pb2.DirectoryRequest(directory_path=directory_path)
    response = stub.SyncDirectory(request)
    print(f"SyncDirectory response: success={response.success}")
    for file_response in response.files:
        print(f"  File sync result: success={file_response.success}, message={file_response.message}")

def delete_file(stub, file_path):
    request = tra_pb2.DeleteRequest(file_path=file_path)
    response = stub.DeleteFile(request)
    print(f"DeleteFile response: success={response.success}, message={response.message}")

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tra_pb2_grpc.FileSyncServiceStub(channel)
        
        # Sync a file
        sync_file(stub, 'example.txt')

        # Sync a directory
        sync_directory_client(stub, 'example_dir')
        
        # Delete a file
        delete_file(stub, 'example.txt')  


if __name__ == '__main__':
    run()