# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tra.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'tra.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttra.proto\"M\n\x0b\x46ileRequest\x12\x11\n\tfile_path\x18\x01 \x01(\t\x12\x14\n\x0c\x66ile_content\x18\x02 \x01(\x0c\x12\x15\n\rlast_modified\x18\x03 \x01(\x03\"0\n\x0c\x46ileResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\"*\n\x10\x44irectoryRequest\x12\x16\n\x0e\x64irectory_path\x18\x01 \x01(\t\"B\n\x11\x44irectoryResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x1c\n\x05\x66iles\x18\x02 \x03(\x0b\x32\r.FileResponse\"\"\n\rDeleteRequest\x12\x11\n\tfile_path\x18\x01 \x01(\t\"2\n\x0e\x44\x65leteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t2\xa1\x01\n\x0f\x46ileSyncService\x12\'\n\x08SyncFile\x12\x0c.FileRequest\x1a\r.FileResponse\x12\x36\n\rSyncDirectory\x12\x11.DirectoryRequest\x1a\x12.DirectoryResponse\x12-\n\nDeleteFile\x12\x0e.DeleteRequest\x1a\x0f.DeleteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tra_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_FILEREQUEST']._serialized_start=13
  _globals['_FILEREQUEST']._serialized_end=90
  _globals['_FILERESPONSE']._serialized_start=92
  _globals['_FILERESPONSE']._serialized_end=140
  _globals['_DIRECTORYREQUEST']._serialized_start=142
  _globals['_DIRECTORYREQUEST']._serialized_end=184
  _globals['_DIRECTORYRESPONSE']._serialized_start=186
  _globals['_DIRECTORYRESPONSE']._serialized_end=252
  _globals['_DELETEREQUEST']._serialized_start=254
  _globals['_DELETEREQUEST']._serialized_end=288
  _globals['_DELETERESPONSE']._serialized_start=290
  _globals['_DELETERESPONSE']._serialized_end=340
  _globals['_FILESYNCSERVICE']._serialized_start=343
  _globals['_FILESYNCSERVICE']._serialized_end=504
# @@protoc_insertion_point(module_scope)
