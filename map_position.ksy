meta:
  id: map_position
  imports:
    - xoru2
  endian: le
  license:	CC-BY-NC-SA-3.0
doc-ref:	https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#map_position
seq:
  - id: x
    size: 2
    type: xoru2
    process:  xor([0x32,0xB3])
  - id: y
    size: 2
    type: xoru2
    process:  xor([0xB2,0x28])
  - id: padding
    size: 4