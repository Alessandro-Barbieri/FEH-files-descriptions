meta:
  id: map_definition
  imports:
    - xoru1
    - xoru4
    - xorb1
    - file_ptr
    - field_definition
    - map_position
    - unit_data
  endian: le
seq:
  - id: unknown1
    type: u4
  - id: highest_score
    size: 4
    type: xoru4
    process: xor([0xB1,0x50,0xE2,0xA9])
  - id: field_ptr
    type: file_ptr
  - id: player_pos_ptr
    type: file_ptr
  - id: units_ptr
    type: file_ptr
  - id: player_count
    size: 4
    type: xoru4
    process: xor([0x9A,0xC7,0x63,0x9D])
  - id: unit_count
    size: 4
    type: xoru4
    process: xor([0xEE,0x10,0x67,0xAC])
  - id: turns_to_win
    size: 1
    type: xoru1
    process: xor([0xFD])
  - id: last_enemy_phase
    size: 1
    type: xorb1
    process: xor([0xC7])
  - id: turns_to_defend
    size: 1
    type: xoru1
    process: xor([0xEC])
#      - id: padding
#        size: 5
instances:
  field:
    pos: field_ptr.offset + 0x20
    type: field_definition
  player_pos:
    pos:  player_pos_ptr.offset + 0x20
    type: map_position
    repeat: expr
    repeat-expr:  player_count.data
  units:
    pos:  units_ptr.offset + 0x20
    type: unit_data
    repeat: expr
    repeat-expr:  unit_count.data