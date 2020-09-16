# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/spatial_transformer.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import convnet_pb2 as protos_dot_convnet__pb2
from protos import hyperparams_pb2 as protos_dot_hyperparams__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/spatial_transformer.proto',
  package='protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n protos/spatial_transformer.proto\x12\x06protos\x1a\x14protos/convnet.proto\x1a\x18protos/hyperparams.proto\"\xfc\x02\n\x12SpatialTransformer\x12 \n\x07\x63onvnet\x18\x01 \x01(\x0b\x32\x0f.protos.Convnet\x12+\n\x0e\x66\x63_hyperparams\x18\x02 \x01(\x0b\x32\x13.protos.Hyperparams\x12\x1a\n\x0elocalization_h\x18\x03 \x01(\x05:\x02\x36\x34\x12\x1b\n\x0elocalization_w\x18\x04 \x01(\x05:\x03\x31\x32\x38\x12\x14\n\x08output_h\x18\x05 \x01(\x05:\x02\x33\x32\x12\x15\n\x08output_w\x18\x06 \x01(\x05:\x03\x31\x30\x30\x12\x15\n\x08margin_x\x18\x07 \x01(\x02:\x03\x30.1\x12\x15\n\x08margin_y\x18\x08 \x01(\x02:\x03\x30.1\x12\x1e\n\x12num_control_points\x18\t \x01(\x05:\x02\x32\x30\x12#\n\x11init_bias_pattern\x18\n \x01(\t:\x08identity\x12\x18\n\nactivation\x18\x0b \x01(\t:\x04none\x12$\n\x15summarize_activations\x18\x0c \x01(\x08:\x05\x66\x61lse'
  ,
  dependencies=[protos_dot_convnet__pb2.DESCRIPTOR,protos_dot_hyperparams__pb2.DESCRIPTOR,])




_SPATIALTRANSFORMER = _descriptor.Descriptor(
  name='SpatialTransformer',
  full_name='protos.SpatialTransformer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='convnet', full_name='protos.SpatialTransformer.convnet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fc_hyperparams', full_name='protos.SpatialTransformer.fc_hyperparams', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localization_h', full_name='protos.SpatialTransformer.localization_h', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=64,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='localization_w', full_name='protos.SpatialTransformer.localization_w', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=128,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_h', full_name='protos.SpatialTransformer.output_h', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_w', full_name='protos.SpatialTransformer.output_w', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin_x', full_name='protos.SpatialTransformer.margin_x', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='margin_y', full_name='protos.SpatialTransformer.margin_y', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0.1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num_control_points', full_name='protos.SpatialTransformer.num_control_points', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='init_bias_pattern', full_name='protos.SpatialTransformer.init_bias_pattern', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"identity".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='activation', full_name='protos.SpatialTransformer.activation', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"none".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summarize_activations', full_name='protos.SpatialTransformer.summarize_activations', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=473,
)

_SPATIALTRANSFORMER.fields_by_name['convnet'].message_type = protos_dot_convnet__pb2._CONVNET
_SPATIALTRANSFORMER.fields_by_name['fc_hyperparams'].message_type = protos_dot_hyperparams__pb2._HYPERPARAMS
DESCRIPTOR.message_types_by_name['SpatialTransformer'] = _SPATIALTRANSFORMER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpatialTransformer = _reflection.GeneratedProtocolMessageType('SpatialTransformer', (_message.Message,), {
  'DESCRIPTOR' : _SPATIALTRANSFORMER,
  '__module__' : 'protos.spatial_transformer_pb2'
  # @@protoc_insertion_point(class_scope:protos.SpatialTransformer)
  })
_sym_db.RegisterMessage(SpatialTransformer)


# @@protoc_insertion_point(module_scope)