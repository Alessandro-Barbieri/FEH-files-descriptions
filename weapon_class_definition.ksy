meta:
  id: weapon_class_definition
  imports:
    - crypt_string
    - xoru1
    - xorb1
    - weapon_index
  endian: le
  license:	CC-BY-NC-SA-3.0
seq:
  - id: id_tag
    type: crypt_string('ID')
  - id:  sprite_base
    type: crypt_string('NONE')
    repeat: expr
    repeat-expr:  2
  - id: base_weapon
    type: crypt_string('ID')
  - id: index
    size: 4
    type: weapon_index
    process:  xor([0x0c,0x41,0xd3,0x90])
  - id: color
    type: u1
    enum: color_enum
  - id: range
    size: 1
    type: xoru1
    process:  xor([0x8b])
  - id: unknown1
    size: 1
    type: xoru1
    process:  xor([0xd0])
  - id: equip_group
    size: 1
    type: xoru1
    process:  xor([0xb7])
  - id: res_damage
    size: 1
    type: xorb1
    process:  xor([0x07])
  - id: is_staff
    size: 1
    type: xorb1
    process:  xor([0x78])
  - id: is_dagger
    size: 1
    type: xorb1
    process:  xor([0xd7])
  - id: is_breath
    size: 1
    type: xorb1
    process:  xor([0x11])
  - id: padding
    size: 4
enums:
  color_enum:
    0x2c:  colorless
    0x2d:  red
    0x2e:  blue
    0x2f:  green