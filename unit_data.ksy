meta:
  id: unit_data
  imports:
    - xoru1
    - xors1
    - xorb1
    - crypt_string
    - stats_tuple
    - field_definition
    - map_position
  endian: le
seq:
  - id: id_tag
    type: crypt_string
  - id: skills
    type: crypt_string
    repeat: expr
    repeat-expr:  7
  - id: accessory
    type: crypt_string
  - id: pos
    type: map_position
  - id: rarity
    size: 1
    type: xoru1
    process:  xor([0x61])
  - id: lv
    size: 1
    type: xoru1
    process:  xor([0x2a])
  - id: cooldown_count
    size: 1
    type: xors1
    process:  xor([0x1e])
  - id: unknown1
    type: u1
  - id: stats
    type: stats_tuple
  - id: start_turn
    size: 1
    type: xors1
    process:  xor([0xcf])
  - id: movement_group
    size: 1
    type: xors1
    process:  xor([0xf4])
  - id: movement_delay
    size: 1
    type: xors1
    process:  xor([0x95])
  - id: break_terrain
    size: 1
    type: xorb1
    process:  xor([0x71])
  - id: tether
    size: 1
    type: xorb1
    process:  xor([0xb8])
  - id: true_lv
    size: 1
    type: xoru1
    process:  xor([0x85])
  - id: is_enemy
    size: 1
    type: xorb1
    process:  xor([0xd0])
  - id: padding
    size: 1
  - id: spawn_check
    type: crypt_string
  - id: spawn_count
    size: 1
    type: xors1
    process:  xor([0x0A])
  - id: spawn_turns
    size: 1
    type: xors1
    process:  xor([0x0A])
  - id: spawn_target_remain
    size: 1
    type: xors1
    process:  xor([0x2d])
  - id: spawn_target_kills
    size: 1
    type: xors1
    process:  xor([0x5b])