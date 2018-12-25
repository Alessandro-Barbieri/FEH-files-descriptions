meta:
  id: crypt_string
  endian: le
params:
  - id: cipher
    type: str
seq:
  - id: buffer
    type: strz
    encoding: UTF-8
  - id: padding
    size: (8 - _io.pos) % 8