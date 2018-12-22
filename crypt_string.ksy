meta:
  id: crypt_string
  endian: le
seq:
  - id: buffer
    type: strz
    encoding: UTF-8
  - id: padding
    size: (8 - _io.pos) % 8