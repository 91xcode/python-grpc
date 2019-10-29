# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ticket.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ticket.proto',
  package='ticket',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0cticket.proto\x12\x06ticket\"\x07\n\x05\x45mpty\"0\n\nLoginQuery\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x1f\n\x0b\x43ommonQuery\x12\x10\n\x08username\x18\x01 \x01(\t\"+\n\x0e\x43ommonResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\":\n\tPassenger\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tid_number\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"T\n\x10UserInfoResponse\x12%\n\npassengers\x18\x01 \x03(\x0b\x32\x11.ticket.Passenger\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0b\n\x03msg\x18\x03 \x01(\t\"\x99\x01\n\nTrainQuery\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x15\n\rstart_station\x18\x02 \x01(\t\x12\x13\n\x0b\x65nd_station\x18\x03 \x01(\t\x12\x13\n\x0bpage_number\x18\x04 \x01(\x05\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12)\n\x0c\x63ommon_query\x18\x06 \x01(\x0b\x32\x13.ticket.CommonQuery\"\xde\x02\n\tTrainInfo\x12\x14\n\x0ctrain_number\x18\x01 \x01(\t\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\t\x12\x15\n\rstart_station\x18\x04 \x01(\t\x12\x13\n\x0b\x65nd_station\x18\x05 \x01(\t\x12:\n\rticket_remain\x18\x06 \x03(\x0b\x32#.ticket.TrainInfo.TicketRemainEntry\x12@\n\x10ticket_alternate\x18\x07 \x03(\x0b\x32&.ticket.TrainInfo.TicketAlternateEntry\x1a\x33\n\x11TicketRemainEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14TicketAlternateEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"K\n\rTrainResponse\x12\x1f\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x11.ticket.TrainInfo\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0b\n\x03msg\x18\x03 \x01(\t\"\xc7\x01\n\x0bOrderParams\x12\x15\n\rstart_station\x18\x01 \x01(\t\x12\x13\n\x0b\x65nd_station\x18\x02 \x01(\t\x12\r\n\x05\x64\x61tes\x18\x03 \x03(\t\x12\x15\n\rtrain_numbers\x18\x04 \x03(\t\x12\x14\n\x0cticket_types\x18\x05 \x03(\t\x12%\n\npassengers\x18\x06 \x03(\x0b\x32\x11.ticket.Passenger\x12)\n\x0c\x63ommon_query\x18\x07 \x01(\x0b\x32\x13.ticket.CommonQuery\"s\n\tOrderInfo\x12\x15\n\rstart_station\x18\x01 \x01(\t\x12\x13\n\x0b\x65nd_station\x18\x02 \x01(\t\x12\r\n\x05\x64\x61tes\x18\x03 \x03(\t\x12\x15\n\rtrain_numbers\x18\x04 \x03(\t\x12\x14\n\x0cticket_types\x18\x05 \x03(\t\"M\n\rOrderResponse\x12!\n\x06orders\x18\x01 \x03(\x0b\x32\x11.ticket.OrderInfo\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x05\x12\x0b\n\x03msg\x18\x03 \x01(\t2\xbb\x02\n\x0bTrainServer\x12>\n\x0cLoginRequest\x12\x12.ticket.LoginQuery\x1a\x18.ticket.UserInfoResponse\"\x00\x12\x38\n\x0bGetUserInfo\x12\r.ticket.Empty\x1a\x18.ticket.UserInfoResponse\"\x00\x12;\n\x0cGetTrainInfo\x12\x12.ticket.TrainQuery\x1a\x15.ticket.TrainResponse\"\x00\x12\x39\n\x08\x41\x64\x64Order\x12\x13.ticket.OrderParams\x1a\x16.ticket.CommonResponse\"\x00\x12:\n\nQueryOrder\x12\x13.ticket.CommonQuery\x1a\x15.ticket.OrderResponse\"\x00\x62\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='ticket.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=24,
  serialized_end=31,
)


_LOGINQUERY = _descriptor.Descriptor(
  name='LoginQuery',
  full_name='ticket.LoginQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='ticket.LoginQuery.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='ticket.LoginQuery.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=33,
  serialized_end=81,
)


_COMMONQUERY = _descriptor.Descriptor(
  name='CommonQuery',
  full_name='ticket.CommonQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='ticket.CommonQuery.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=83,
  serialized_end=114,
)


_COMMONRESPONSE = _descriptor.Descriptor(
  name='CommonResponse',
  full_name='ticket.CommonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='ticket.CommonResponse.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ticket.CommonResponse.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=116,
  serialized_end=159,
)


_PASSENGER = _descriptor.Descriptor(
  name='Passenger',
  full_name='ticket.Passenger',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='ticket.Passenger.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id_number', full_name='ticket.Passenger.id_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='ticket.Passenger.type', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=161,
  serialized_end=219,
)


_USERINFORESPONSE = _descriptor.Descriptor(
  name='UserInfoResponse',
  full_name='ticket.UserInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='passengers', full_name='ticket.UserInfoResponse.passengers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='ticket.UserInfoResponse.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ticket.UserInfoResponse.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=221,
  serialized_end=305,
)


_TRAINQUERY = _descriptor.Descriptor(
  name='TrainQuery',
  full_name='ticket.TrainQuery',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='ticket.TrainQuery.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_station', full_name='ticket.TrainQuery.start_station', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_station', full_name='ticket.TrainQuery.end_station', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_number', full_name='ticket.TrainQuery.page_number', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='ticket.TrainQuery.page_size', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_query', full_name='ticket.TrainQuery.common_query', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=308,
  serialized_end=461,
)


_TRAININFO_TICKETREMAINENTRY = _descriptor.Descriptor(
  name='TicketRemainEntry',
  full_name='ticket.TrainInfo.TicketRemainEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ticket.TrainInfo.TicketRemainEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ticket.TrainInfo.TicketRemainEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=707,
  serialized_end=758,
)

_TRAININFO_TICKETALTERNATEENTRY = _descriptor.Descriptor(
  name='TicketAlternateEntry',
  full_name='ticket.TrainInfo.TicketAlternateEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ticket.TrainInfo.TicketAlternateEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ticket.TrainInfo.TicketAlternateEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=760,
  serialized_end=814,
)

_TRAININFO = _descriptor.Descriptor(
  name='TrainInfo',
  full_name='ticket.TrainInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='train_number', full_name='ticket.TrainInfo.train_number', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='ticket.TrainInfo.start_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='ticket.TrainInfo.end_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_station', full_name='ticket.TrainInfo.start_station', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_station', full_name='ticket.TrainInfo.end_station', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticket_remain', full_name='ticket.TrainInfo.ticket_remain', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticket_alternate', full_name='ticket.TrainInfo.ticket_alternate', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRAININFO_TICKETREMAINENTRY, _TRAININFO_TICKETALTERNATEENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=464,
  serialized_end=814,
)


_TRAINRESPONSE = _descriptor.Descriptor(
  name='TrainResponse',
  full_name='ticket.TrainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ticket.TrainResponse.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='ticket.TrainResponse.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ticket.TrainResponse.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=816,
  serialized_end=891,
)


_ORDERPARAMS = _descriptor.Descriptor(
  name='OrderParams',
  full_name='ticket.OrderParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_station', full_name='ticket.OrderParams.start_station', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_station', full_name='ticket.OrderParams.end_station', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dates', full_name='ticket.OrderParams.dates', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_numbers', full_name='ticket.OrderParams.train_numbers', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticket_types', full_name='ticket.OrderParams.ticket_types', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='passengers', full_name='ticket.OrderParams.passengers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_query', full_name='ticket.OrderParams.common_query', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=894,
  serialized_end=1093,
)


_ORDERINFO = _descriptor.Descriptor(
  name='OrderInfo',
  full_name='ticket.OrderInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_station', full_name='ticket.OrderInfo.start_station', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_station', full_name='ticket.OrderInfo.end_station', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dates', full_name='ticket.OrderInfo.dates', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='train_numbers', full_name='ticket.OrderInfo.train_numbers', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticket_types', full_name='ticket.OrderInfo.ticket_types', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1095,
  serialized_end=1210,
)


_ORDERRESPONSE = _descriptor.Descriptor(
  name='OrderResponse',
  full_name='ticket.OrderResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orders', full_name='ticket.OrderResponse.orders', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='ticket.OrderResponse.code', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='msg', full_name='ticket.OrderResponse.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1212,
  serialized_end=1289,
)

_USERINFORESPONSE.fields_by_name['passengers'].message_type = _PASSENGER
_TRAINQUERY.fields_by_name['common_query'].message_type = _COMMONQUERY
_TRAININFO_TICKETREMAINENTRY.containing_type = _TRAININFO
_TRAININFO_TICKETALTERNATEENTRY.containing_type = _TRAININFO
_TRAININFO.fields_by_name['ticket_remain'].message_type = _TRAININFO_TICKETREMAINENTRY
_TRAININFO.fields_by_name['ticket_alternate'].message_type = _TRAININFO_TICKETALTERNATEENTRY
_TRAINRESPONSE.fields_by_name['data'].message_type = _TRAININFO
_ORDERPARAMS.fields_by_name['passengers'].message_type = _PASSENGER
_ORDERPARAMS.fields_by_name['common_query'].message_type = _COMMONQUERY
_ORDERRESPONSE.fields_by_name['orders'].message_type = _ORDERINFO
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['LoginQuery'] = _LOGINQUERY
DESCRIPTOR.message_types_by_name['CommonQuery'] = _COMMONQUERY
DESCRIPTOR.message_types_by_name['CommonResponse'] = _COMMONRESPONSE
DESCRIPTOR.message_types_by_name['Passenger'] = _PASSENGER
DESCRIPTOR.message_types_by_name['UserInfoResponse'] = _USERINFORESPONSE
DESCRIPTOR.message_types_by_name['TrainQuery'] = _TRAINQUERY
DESCRIPTOR.message_types_by_name['TrainInfo'] = _TRAININFO
DESCRIPTOR.message_types_by_name['TrainResponse'] = _TRAINRESPONSE
DESCRIPTOR.message_types_by_name['OrderParams'] = _ORDERPARAMS
DESCRIPTOR.message_types_by_name['OrderInfo'] = _ORDERINFO
DESCRIPTOR.message_types_by_name['OrderResponse'] = _ORDERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.Empty)
  })
_sym_db.RegisterMessage(Empty)

LoginQuery = _reflection.GeneratedProtocolMessageType('LoginQuery', (_message.Message,), {
  'DESCRIPTOR' : _LOGINQUERY,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.LoginQuery)
  })
_sym_db.RegisterMessage(LoginQuery)

CommonQuery = _reflection.GeneratedProtocolMessageType('CommonQuery', (_message.Message,), {
  'DESCRIPTOR' : _COMMONQUERY,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.CommonQuery)
  })
_sym_db.RegisterMessage(CommonQuery)

CommonResponse = _reflection.GeneratedProtocolMessageType('CommonResponse', (_message.Message,), {
  'DESCRIPTOR' : _COMMONRESPONSE,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.CommonResponse)
  })
_sym_db.RegisterMessage(CommonResponse)

Passenger = _reflection.GeneratedProtocolMessageType('Passenger', (_message.Message,), {
  'DESCRIPTOR' : _PASSENGER,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.Passenger)
  })
_sym_db.RegisterMessage(Passenger)

UserInfoResponse = _reflection.GeneratedProtocolMessageType('UserInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _USERINFORESPONSE,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.UserInfoResponse)
  })
_sym_db.RegisterMessage(UserInfoResponse)

TrainQuery = _reflection.GeneratedProtocolMessageType('TrainQuery', (_message.Message,), {
  'DESCRIPTOR' : _TRAINQUERY,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.TrainQuery)
  })
_sym_db.RegisterMessage(TrainQuery)

TrainInfo = _reflection.GeneratedProtocolMessageType('TrainInfo', (_message.Message,), {

  'TicketRemainEntry' : _reflection.GeneratedProtocolMessageType('TicketRemainEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRAININFO_TICKETREMAINENTRY,
    '__module__' : 'ticket_pb2'
    # @@protoc_insertion_point(class_scope:ticket.TrainInfo.TicketRemainEntry)
    })
  ,

  'TicketAlternateEntry' : _reflection.GeneratedProtocolMessageType('TicketAlternateEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRAININFO_TICKETALTERNATEENTRY,
    '__module__' : 'ticket_pb2'
    # @@protoc_insertion_point(class_scope:ticket.TrainInfo.TicketAlternateEntry)
    })
  ,
  'DESCRIPTOR' : _TRAININFO,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.TrainInfo)
  })
_sym_db.RegisterMessage(TrainInfo)
_sym_db.RegisterMessage(TrainInfo.TicketRemainEntry)
_sym_db.RegisterMessage(TrainInfo.TicketAlternateEntry)

TrainResponse = _reflection.GeneratedProtocolMessageType('TrainResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRAINRESPONSE,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.TrainResponse)
  })
_sym_db.RegisterMessage(TrainResponse)

OrderParams = _reflection.GeneratedProtocolMessageType('OrderParams', (_message.Message,), {
  'DESCRIPTOR' : _ORDERPARAMS,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.OrderParams)
  })
_sym_db.RegisterMessage(OrderParams)

OrderInfo = _reflection.GeneratedProtocolMessageType('OrderInfo', (_message.Message,), {
  'DESCRIPTOR' : _ORDERINFO,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.OrderInfo)
  })
_sym_db.RegisterMessage(OrderInfo)

OrderResponse = _reflection.GeneratedProtocolMessageType('OrderResponse', (_message.Message,), {
  'DESCRIPTOR' : _ORDERRESPONSE,
  '__module__' : 'ticket_pb2'
  # @@protoc_insertion_point(class_scope:ticket.OrderResponse)
  })
_sym_db.RegisterMessage(OrderResponse)


_TRAININFO_TICKETREMAINENTRY._options = None
_TRAININFO_TICKETALTERNATEENTRY._options = None

_TRAINSERVER = _descriptor.ServiceDescriptor(
  name='TrainServer',
  full_name='ticket.TrainServer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1292,
  serialized_end=1607,
  methods=[
  _descriptor.MethodDescriptor(
    name='LoginRequest',
    full_name='ticket.TrainServer.LoginRequest',
    index=0,
    containing_service=None,
    input_type=_LOGINQUERY,
    output_type=_USERINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserInfo',
    full_name='ticket.TrainServer.GetUserInfo',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_USERINFORESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTrainInfo',
    full_name='ticket.TrainServer.GetTrainInfo',
    index=2,
    containing_service=None,
    input_type=_TRAINQUERY,
    output_type=_TRAINRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddOrder',
    full_name='ticket.TrainServer.AddOrder',
    index=3,
    containing_service=None,
    input_type=_ORDERPARAMS,
    output_type=_COMMONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QueryOrder',
    full_name='ticket.TrainServer.QueryOrder',
    index=4,
    containing_service=None,
    input_type=_COMMONQUERY,
    output_type=_ORDERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRAINSERVER)

DESCRIPTOR.services_by_name['TrainServer'] = _TRAINSERVER

# @@protoc_insertion_point(module_scope)
