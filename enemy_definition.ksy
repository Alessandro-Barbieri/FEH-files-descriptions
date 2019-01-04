meta:
  id: enemy_definition
  imports:
    - crypt_string
    - encrypted
    - stats_tuple
    - xorb1
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  The files at `Common/SRPG/Enemy/` define data for enemy-only units. This
  means enemies have base stats and GPs too.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Enemy_definitions
seq:
  - id: id_tag
    type: crypt_string('ID')
    doc: Internal string identifier of the enemy. Begins with `PID_`.
  - id: roman
    type: crypt_string('ID')
    doc: |
      Internal Romanized name of the enemy. Used for example to derive file
      names of voice files.
  - id: face_name
    type: crypt_string('ID')
    doc: |
      The directory name at `Common/Face/` that contains portraits for the
      enemy.
  - id: face_name_2
    type: crypt_string('ID')
    doc: Appears to be always identical to `face_name`.
  - id: top_weapon
    type: crypt_string('ID')
    doc: |
      If non-null, points to the identifier for the weapon equipped by this
      unit when promoted to 5★ in derived maps. For example Veronica's points
      to Élivágar, and all generic enemies have this field null.
  - id: timestamp
    type: encrypted('xors8')
    size: 8
    process: xor([0x9b,0x48,0xb6,0xe9,0x42,0xe7,0xc1,0xbd])
    doc: |
      A POSIX timestamp relative to the enemy's release date; half a month into
      the future for heroes released before Version `2.0.0`, 1 month into the
      future for heroes released since Version `2.0.0`. This enemy would appear
      in the Training Tower if `timestamp` is not -1 and the current time is
      past `timestamp`.
  - id: id_num
    size: 4
    type: encrypted('xoru4')
    process: xor([0xd4,0x41,0x2f,0x42])
    doc: The internal `ID` of the enemy.
  - id: weapon_type
    type: weapon_index
    size: 1
    process: xor([0xe4])
    doc: The color / weapon class of the enemy
  - id: tome_class
    size: 1
    type: magic_element
    process: xor([0x81])
    doc: The element type for tome users.
  - id: move_type
    size: 1
    type: move_index
    process: xor([0x0d])
    doc: Move type of the enemy.
  - id: unknown1
    size: 1
    type: xorb1
    process: xor([0xc5])
  - id: is_boss
    size: 1
    type: xorb1
    process: xor([0x6a])
    doc: |
      True if this unit is an enemy boss, false if this unit is a generic unit.
  - id: padding
    size: 7
  - id: base_stats
    type: stats_tuple
    doc: |
      Hypothetical base stats for the enemy at 3★. Used in derived maps for
      rarity promotion.
  - id: growth_rates
    type: stats_tuple
    doc: |
      Hypothetical growth rates for the enemy at 3★. Used in derived maps for
      leveling up.
