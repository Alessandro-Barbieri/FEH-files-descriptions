meta:
  id: map_position
  imports:
    - xoru2
  endian: le
seq:
  - id: x
    size: 2
    type: xoru2
    process:  xor([0x32,0xB3])
  - id: y
    size: 2
    type: xoru2
    process:  xor([0xB2,0x28])
#      - id: padding
#        size: 4