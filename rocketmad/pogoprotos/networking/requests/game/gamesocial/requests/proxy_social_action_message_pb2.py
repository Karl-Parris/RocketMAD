# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/game/gamesocial/requests/proxy_social_action_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/game/gamesocial/requests/proxy_social_action_message.proto',
  package='pogoprotos.networking.requests.game.gamesocial.requests',
  syntax='proto3',
  serialized_pb=_b('\nYpogoprotos/networking/requests/game/gamesocial/requests/proxy_social_action_message.proto\x12\x37pogoprotos.networking.requests.game.gamesocial.requests\"I\n\x18ProxySocialActionMessage\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PROXYSOCIALACTIONMESSAGE = _descriptor.Descriptor(
  name='ProxySocialActionMessage',
  full_name='pogoprotos.networking.requests.game.gamesocial.requests.ProxySocialActionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='pogoprotos.networking.requests.game.gamesocial.requests.ProxySocialActionMessage.action', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='host', full_name='pogoprotos.networking.requests.game.gamesocial.requests.ProxySocialActionMessage.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload', full_name='pogoprotos.networking.requests.game.gamesocial.requests.ProxySocialActionMessage.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=223,
)

DESCRIPTOR.message_types_by_name['ProxySocialActionMessage'] = _PROXYSOCIALACTIONMESSAGE

ProxySocialActionMessage = _reflection.GeneratedProtocolMessageType('ProxySocialActionMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROXYSOCIALACTIONMESSAGE,
  __module__ = 'pogoprotos.networking.requests.game.gamesocial.requests.proxy_social_action_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.game.gamesocial.requests.ProxySocialActionMessage)
  ))
_sym_db.RegisterMessage(ProxySocialActionMessage)


# @@protoc_insertion_point(module_scope)