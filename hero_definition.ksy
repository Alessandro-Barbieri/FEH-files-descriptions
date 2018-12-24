meta:
  id: hero_definition
  imports:
    - crypt_string
    - xoru4
    - xoru1
    - xorb1
    - xors8
    - weapon_index
    - stats_tuple
    - file_ptr
    - magic_element
    - move_index
    - legendary_info
  endian: le
seq:
  - id: id_tag
    type: crypt_string
  - id: roman
    type: crypt_string
  - id:  face_name
    type: crypt_string
  - id: face_name_2
    type: crypt_string
  - id: legendary_ptr
    type: file_ptr
  - id: timestamp
    type: xors8
    size: 8
    process:  xor([0x9b,0x48,0xb6,0xe9,0x42,0xe7,0xc1,0xbd])
  - id: id_num
    size: 4
    type: xoru4
    process:  xor([0x18,0x4e,0x6e,0x5f])
  - id: sort_value
    size: 4
    type: xoru4
    process:  xor([0x18,0x4e,0x6e,0x5f])
  - id: weapon_type
    type: weapon_index
    size: 1
    process:  xor([0x06])
  - id: tome_class
    size: 1
    type: magic_element
    process:  xor([0x35])
  - id: move_type
    size: 1
    type: move_index
    process:  xor([0x2a])
  - id: series
    size: 1
    type: xoru1
    process:  xor([0x43])
  - id: regular_hero
    size: 1
    type: xorb1
    process:  xor([0xa1])
  - id: permanent_hero
    size: 1
    type: xorb1
    process:  xor([0xc7])
  - id: base_vector_id
    size: 1
    type: xoru1
    process:  xor([0x3d])
  - id: refresher
    size: 1
    type: xorb1
    process:  xor([0xff])
  - id: unknown2
    type: u1
  - id: padding
    size: 7
  - id: base_stats
    type: stats_tuple
  - id: growth_rates
    type: stats_tuple
  - id: max_stats
    type: stats_tuple
  - id: skills
    type: crypt_string
    repeat: expr
    repeat-expr: 8 * 14
#instances:
#  legendary:
#    type: legendary_info
#    pos: legendary_ptr.offset+ 0x20
#    if: legendary_ptr.offset != 0
#    repeat: expr
#    repeat-expr: 1