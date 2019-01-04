meta:
  id: map_position
  imports:
    - encrypted
  endian: le
  license: CC-BY-NC-SA-3.0ù
doc: Coordinates representing a point on a map.
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#map_position
seq:
  - id: x
    size: 2
    type: encrypted('xoru2')
    process: xor([0x32,0xB3])
    doc: X position, 0 for the leftmost column.
  - id: y
    size: 2
    type: encrypted('xoru2')
    process: xor([0xB2,0x28])
    doc: Y position, 0 for the bottom-most row.
  - id: padding
    size: 4
