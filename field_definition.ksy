meta:
  id: field_definition
  imports:
    - crypt_string
    - encrypted
  endian: le
  license: CC-BY-NC-SA-3.0
doc: Terrain data of a map. Graphical information is stored outside map files.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#field_definition
seq:
  - id: id
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the map. For permanent maps this is just
      the filename without the extension and the difficulty (e.g. S2115).
  - id: width
    size: 4
    type: encrypted('xoru4')
    process: xor([0x5F,0xD7,0x7C,0x6B])
    doc: Width of the map.
  - id: height
    size: 4
    type: encrypted('xoru4')
    process: xor([0xd5,0x12,0xaa,0x2b])
    doc: Height of the map.
  - id: base_terrain
    size: 1
    type: encrypted('xoru1')
    process: xor([0x41])
    doc: |
      Default terrain index of the map. If this is not `-1`, special defaults
      (`CHIP0` and `CHIP1`) for field graphics representing this terrain are
      used, otherwise the map would have its own entry in the files under
      `Common/SRPG/Field/`. Used in maps for Rival Domains and Tactics Drills.
  - id: padding
    size: 7
  - id: terrain
    size: height.data * width.data
    process: xor([0xA1])
    doc: |
      Terrain indices, starting from the bottom to the top, then from left to
      right within each row. This ordering is consistent with `map_position`.
