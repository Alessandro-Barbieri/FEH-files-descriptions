meta:
  id: weapon_class_definition
  imports:
    - crypt_string
    - encrypted
    - weapon_index
    - xorb1
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  The file `assets/Common/SRPG/Weapon.bin` defines the weapon classes used by
  units. Weapon skills only indicate which weapon classes can equip them;
  common weapon attributes are defined in the weapon classes rather than the
  weapon skills.

  Only one of `is_staff`, `is_dagger`, and `is_breath` can be used by skills,
  in that order of precedence.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Weapon_class_definitions
seq:
  - id: id_tag
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the weapon class, e.g. `WID_赤弓` for
      Red bow.
  - id: sprite_base
    type: crypt_string('NONE')
    repeat: expr
    repeat-expr:  2
    doc: |
      Filename prefixes of the weapon sprites used for this weapon class, e.g.
      `wep_bw` and `wep_ar` for bow classes.
  - id: base_weapon
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the base weapon skill, e.g. `SID_鉄の弓`
      Iron Bow for all bow classes.
  - id: index
    size: 4
    type: weapon_index
    process: xor([0x0c,0x41,0xd3,0x90])
    doc: Internal index of the weapon class.
  - id: color
    type: u1
    enum: color_enum
    doc: Color of the weapon class.
  - id: range
    size: 1
    type: encrypted('xoru1')
    process: xor([0x8b])
    doc: |
      Default attack range of the weapon class. Only `SLID_周囲戦闘_敵射程`, used by
      Close Guard 3 and Distant Guard 3, check this value.
  - id: unknown1
    size: 1
    type: encrypted('xoru1')
    process: xor([0xd0])
  - id: equip_group
    size: 1
    type: encrypted('xoru1')
    process: xor([0xb7])
    doc: |
      Group index of the weapon class as classified according to the skill menu
      used during skill inheritance.
  - id: res_damage
    size: 1
    type: xorb1
    process: xor([0x07])
    doc: Uses the foe's Res to calculate damage if true, uses Def otherwise.
  - id: is_staff
    size: 1
    type: xorb1
    process: xor([0x78])
    doc: |
      If true, allows `skill_definition.class_params` to grant the effect of
      Wrathful Staff 3 or Dazzling Staff 3.
  - id: is_dagger
    size: 1
    type: xorb1
    process: xor([0xd7])
    doc: |
      If true, allows `skill_definition.class_params` to inflict stat penalties
      on foes.
  - id: is_breath
    size: 1
    type: xorb1
    process: xor([0x11])
    doc: |
      If true, allows `skill_definition.class_params` to calculate damage using
      the lower of foe's Def or Res.
  - id: padding
    size: 4
enums:
  color_enum:
    0x2c: colorless
    0x2d: red
    0x2e: blue
    0x2f: green
