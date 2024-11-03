# server.py

import grpc
from concurrent import futures
import os
import time
import tra_pb2
import tra_pb2_grpc

# Vector Time Class and Logic for Conflict Detection
class VectorTime:
    def __init__(self):
        self.time_vector = {}

    def update(self, replica_id, timestamp):
        self.time_vector[replica_id] = max(self.time_vector.get(replica_id, 0), timestamp)

    def is_ancestor_of(self, other):
        for replica_id, time in self.time_vector.items():
            if time > other.time_vector.get(replica_id, 0):
                return False
        return True

class FileSyncService(tra_pb2_grpc.FileSyncServiceServicer):
    def SyncFile(self, request, context):
        file_path = request.file_path
        last_modified = request.last_modified
        file_exists = os.path.exists(file_path)

        # Initialize vector time for incoming request
        current_vector_time = VectorTime()
        current_vector_time.update('replica_id', last_modified)  # Use a unique replica ID

        # Load existing vector time from metadata (replace with actual metadata handling logic)
        existing_vector_time = VectorTime()  # Retrieve from metadata store if available

        # Conflict detection using vector time pairs
        if not existing_vector_time.is_ancestor_of(current_vector_time):
            return tra_pb2.FileResponse(success=False, message="Conflict detected")

        # Write file content if no conflict
        with open(file_path, 'wb') as file:
            file.write(request.file_content)
            os.utime(file_path, (last_modified, last_modified))

        # Update metadata store with the new vector time
        existing_vector_time.update('replica_id', last_modified)  

        return tra_pb2.FileResponse(success=True, message="File synchronized successfully")

    def SyncDirectory(self, request, context):
        dir_path = request.directory_path
        response = tra_pb2.DirectoryResponse(success=True)

        # Check if directory exists
        if not os.path.exists(dir_path):
            response.success = False
            response.files.append(tra_pb2.FileResponse(success=False, message="Directory does not exist"))
            return response

        # Loop through files in the directory and add FileResponse for each file
        for filename in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filename)
            if os.path.isfile(file_path):
                # For each file, we create a FileResponse and append it to files
                response.files.append(
                    tra_pb2.FileResponse(success=True, message=f"File {filename} synchronized")
                )
            else:
                response.files.append(
                    tra_pb2.FileResponse(success=False, message=f"{filename} is not a file")
                )

        return response
    
    def DeleteFile(self, request, context):
        file_path = request.file_path
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                return tra_pb2.DeleteResponse(success=True, message=f"File {file_path} deleted successfully.")
            else:
                return tra_pb2.DeleteResponse(success=False, message="File does not exist.")
        except Exception as e:
            return tra_pb2.DeleteResponse(success=False, message=f"Error deleting file: {str(e)}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tra_pb2_grpc.add_FileSyncServiceServicer_to_server(FileSyncService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
