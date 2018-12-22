meta:
  id: field_definition
  imports:
    - crypt_string
    - xoru1
    - xoru4
  endian: le
seq:
  - id: id
    type: crypt_string
  - id:  width
    size: 4
    type: xoru4
    process:  xor([0x5F,0xD7,0x7C,0x6B])
  - id:  height
    size: 4
    type: xoru4
    process:  xor([0xd5,0x12,0xaa,0x2b])
  - id:  base_terrain
    size: 1
    type: xoru1
    process:  xor([0x41])
  - id: padding
    size: 7
  - id:  terrain
    size: height.data * width.data
    process:  xor([0xA1])