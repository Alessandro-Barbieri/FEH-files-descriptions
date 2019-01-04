meta:
  id: stats_tuple
  imports:
    - encrypted
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  A tuple representing the five stat values. The meaning of the tuple depends
  on the context.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#stats_tuple
seq:
  - id: hp
    size: 2
    type: encrypted('xors2')
    process: xor([0x32,0xD6])
  - id: attack
    size: 2
    type: encrypted('xors2')
    process: xor([0xA0,0x14])
  - id: speed
    size: 2
    type: encrypted('xors2')
    process: xor([0x5E,0xA5])
  - id: defense
    size: 2
    type: encrypted('xors2')
    process: xor([0x66,0x85])
  - id: resistance
    size: 2
    type: encrypted('xors2')
    process: xor([0xE5,0xAE])
  - id: unknown1
    type: s2
  - id: unknown2
    type: s2
  - id: unknown3
    type: s2
