# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/combat/combat_quest_update.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/combat/combat_quest_update.proto',
  package='pogoprotos.data.combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n0pogoprotos/data/combat/combat_quest_update.proto\x12\x16pogoprotos.data.combat\"C\n\x11\x43ombatQuestUpdate\x12.\n&super_effective_charged_attacks_update\x18\x01 \x01(\x05\x62\x06proto3')
)




_COMBATQUESTUPDATE = _descriptor.Descriptor(
  name='CombatQuestUpdate',
  full_name='pogoprotos.data.combat.CombatQuestUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='super_effective_charged_attacks_update', full_name='pogoprotos.data.combat.CombatQuestUpdate.super_effective_charged_attacks_update', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['CombatQuestUpdate'] = _COMBATQUESTUPDATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatQuestUpdate = _reflection.GeneratedProtocolMessageType('CombatQuestUpdate', (_message.Message,), dict(
  DESCRIPTOR = _COMBATQUESTUPDATE,
  __module__ = 'pogoprotos.data.combat.combat_quest_update_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.combat.CombatQuestUpdate)
  ))
_sym_db.RegisterMessage(CombatQuestUpdate)


# @@protoc_insertion_point(module_scope)