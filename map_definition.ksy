meta:
  id: map_definition
  imports:
    - crypt_string
    - encrypted
    - file_ptr
    - map_position
    - unit_data
    - xorb1
  endian: le
  license: CC-BY-NC-SA-3.0
doc: Top-level definition of a map. One instance appears in each map file at `$20`.
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#map_definition
seq:
  - id: unknown1
    type: u4
  - id: highest_score
    size: 4
    type: encrypted('xoru4')
    process: xor([0xB1,0x50,0xE2,0xA9])
    doc: |
      What appears to be the maximum score among all units where the score
      matches the displayed stat sum only for the few easiest maps.
  - id: field_ptr
    type: file_ptr
  - id: player_pos_ptr
    type: file_ptr
  - id: units_ptr
    type: file_ptr
  - id: player_count
    size: 4
    type: encrypted('xoru4')
    process: xor([0x9A,0xC7,0x63,0x9D])
    doc: Length of the `player_pos` array.
  - id: unit_count
    size: 4
    type: encrypted('xoru4')
    process: xor([0xEE,0x10,0x67,0xAC])
    doc: Length of the `units` array.
  - id: turns_to_win
    size: 1
    type: encrypted('xoru1')
    process: xor([0xFD])
    doc: |
      If non-zero, the maximum number of turns under which the player must win
      the map.
  - id: last_enemy_phase
    size: 1
    type: xorb1
    process: xor([0xC7])
    doc: |
      Whether the enemy phase occurs on the last turn if `turns_to_win` is
      given. Only used for Tactics Drills maps.
  - id: turns_to_defend
    size: 1
    type: encrypted('xoru1')
    process: xor([0xEC])
    doc: |
      If non-zero, the number of turns the player must defend in order to win
      the map.
#      - id: padding
#        size: 5
instances:
  field:
    pos: field_ptr.offset + 0x20
    type: field_definition
    if: field_ptr.offset != 0
    doc: Terrain definition of this map.
  player_pos:
    pos:  player_pos_ptr.offset + 0x20
    type: map_position
    repeat: expr
    repeat-expr:  player_count.data
    if: player_pos_ptr.offset != 0
    doc: |
      List of coordinates for the player's team, in the order they are placed.
      Each element is followed by 4 bytes of padding. For Tactics Drills maps
      this list is empty.
  units:
    pos:  units_ptr.offset + 0x20
    type: unit_data
    repeat: expr
    repeat-expr:  unit_count.data
    if: units_ptr.offset != 0
    doc: List of units on the map, including all reinforcements.
types:
  field_definition:
    doc: Terrain data of a map. Graphical information is stored outside map files.
    doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#field_definition
    seq:
      - id: id
        type: crypt_string('ID')
        doc: |
          Internal string identifier of the map. For permanent maps this is
          just the filename without the extension and the difficulty
          (e.g. S2115).
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
          Default terrain index of the map. If this is not `-1`, special
          defaults (`CHIP0` and `CHIP1`) for field graphics representing this
          terrain are used, otherwise the map would have its own entry in the
          files under `Common/SRPG/Field/`. Used in maps for Rival Domains and
          Tactics Drills.
      - id: padding
        size: 7
      - id: terrain
        size: height.data * width.data
        process: xor([0xA1])
        doc: |
          Terrain indices, starting from the bottom to the top, then from left
          to right within each row. This ordering is consistent with
          `map_position`.
