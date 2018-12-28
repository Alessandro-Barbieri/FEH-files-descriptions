meta:
  id: field_definition
  imports:
    - crypt_string
    - xoru1
    - xoru4
  endian: le
  license:	CC-BY-NC-SA-3.0
doc-ref:	https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#field_definition
seq:
  - id: id
    type: crypt_string('ID')
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