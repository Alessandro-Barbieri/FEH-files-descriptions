meta:
  id: stats_tuple
  imports:
    - xors2
  endian: le
seq:
  - id: hp
    size: 2
    type: xors2
    process:  xor([0x32,0xD6])
  - id: atk
    size: 2
    type: xors2
    process:  xor([0xA0,0x14])
  - id: spd
    size: 2
    type: xors2
    process:  xor([0x5E,0xA5])
  - id: def
    size: 2
    type: xors2
    process:  xor([0x66,0x85])
  - id: res
    size: 2
    type: xors2
    process:  xor([0xE5,0xAE])
  - id: unknown1
    type: s2
  - id: unknown2
    type: s2
  - id: unknown3
    type: s2