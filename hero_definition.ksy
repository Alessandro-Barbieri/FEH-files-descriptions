meta:
  id: hero_definition
  imports:
    - crypt_string
    - encrypted
    - legendary_info
    - file_ptr
    - magic_element
    - move_index
    - stats_tuple
    - weapon_index
  endian: le
  license: CC-BY-NC-SA-3.0
doc: Complete definition of a hero.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#hero_definition
seq:
  - id: id_tag
    type: crypt_string('ID')
    doc: Internal string identifier of the hero. Begins with `PID_`.
  - id: roman
    type: crypt_string('ID')
    doc: |
      Internal Romanized name of the hero. Used for example to derive file
      names of voice files.
  - id: face_name
    type: crypt_string('ID')
    doc: |
      The directory name at `Common/Face/` that contains portraits for the
      hero.
  - id: face_name_2
    type: crypt_string('ID')
    doc: Appears to be always identical to `face_name`.
  - id: legendary_ptr
    type: file_ptr
    doc: |
      If non-null, this hero is a Legendary Hero and has the element / effects
      given in the pointed-to struct.
  - id: timestamp
    type: encrypted('xors8')
    size: 8
    process: xor([0x9b,0x48,0xb6,0xe9,0x42,0xe7,0xc1,0xbd])
    doc: |
      A POSIX timestamp relative to the hero's release date; half a month into
      the future for heroes released before Version `2.0.0`, 1 month into the
      future for heroes released since Version `2.0.0`. This hero would appear
      in the Training Tower if `timestamp` is not -1 and the current time is
      past `timestamp`.
  - id: id_num
    size: 4
    type: encrypted('xoru4')
    process: xor([0x18,0x4e,0x6e,0x5f])
    doc: The internal `ID` of the hero.
  - id: sort_value
    size: 4
    type: encrypted('xoru4')
    process: xor([0x9b,0x34,0x80,0x2a])
    doc: |
      A decimal value used to order characters within the same series. The main
      character has a value of `100100`. The largest one or two digits usually
      indicate which in-game region / part the character comes from.

      Examples:
      1     Askr, Altea, Echoes Act 1, Chalphy, Lenster (Thracia 776), Pherae (Binding Blade), main characters (Blazing Blade), Renais
      2     Talys, Echoes Act 2, Ostia (Binding Blade), Frelia
      3     Archanea, Echoes Act 3, Velthomer, Araphen, Ostia (Blazing Blade), Grado
      4     Macedon, Etruria, Jehanna
  - id: weapon_type
    type: weapon_index
    size: 1
    process: xor([0x06])
    doc: The color / weapon class of the hero
  - id: tome_class
    size: 1
    type: magic_element
    process: xor([0x35])
    doc: The element type for tome users.
  - id: move_type
    size: 1
    type: move_index
    process: xor([0x2a])
    doc: Move type of the hero.
  - id: series
    size: 1
    type: encrypted('xoru1')
    process: xor([0x43])
    doc: |
      The game the character originates from.
      0     0x43    Heroes
      1     0x42    Shadow Dragon and the Blade of Light / Mystery of the Emblem / Shadow Dragon / New Mystery of the Emblem
      2     0x41    Gaiden / Echoes
      3     0x40    Genealogy of the Holy War
      4     0x47    Thracia 776
      5     0x46    The Binding Blade
      6     0x45    The Blazing Blade
      7     0x44    The Sacred Stones
      8     0x4B    Path of Radiance
      9     0x4A    Radiant Dawn
      10    0x49    Awakening
      11    0x48    Fates
  - id: regular_hero
    size: 1
    type: xorb1
    process: xor([0xa1])
    doc: True if the hero is available in the random pool.
  - id: permanent_hero
    size: 1
    type: xorb1
    process: xor([0xc7])
    doc: True if the hero cannot be sent home nor merged.
  - id: base_vector_id
    size: 1
    type: encrypted('xoru1')
    process: xor([0x3d])
    doc: |
      The byte that determines where to start counting the growth vectors of
      the hero.
  - id: refresher
    size: 1
    type: xorb1
    process: xor([0xff])
    doc: |
      True if the hero can learn Sing or Dance. At most one such unit can be
      present in a brigade, even when Sing or Dance is not equipped.
  - id: unknown2
    type: u1
  - id: padding
    size: 7
  - id: base_stats
    type: stats_tuple
    doc: Level 1 neutral stats at 3★.
  - id: growth_rates
    type: stats_tuple
    doc: |
      Neutral growth rates as percentages at 3★. Equivalent to `GP × 5 + 20`.
  - id: max_stats
    type: stats_tuple
    doc: |
      Internal level 40 neutral stats, very often different from true neutral
      stats at level 40.
  - id: skills
    type: crypt_string('ID')
    repeat: expr
    repeat-expr: 5 * 14
    doc: |
      A two-dimensional array where non-null entries point to internal skill
      identifiers (ones that begin with `SID_`). The n-th row of the array
      represents learnable skills of the hero at rarity n. The column index
      indicates the skill category:
      0     Default Weapon
      1     Default Assist
      2     Default Special
      6     Unlocked Weapon
      7     Unlocked Assist
      8     Unlocked Special
      9     Unlocked Passive A
      10    Unlocked Passive B
      11    Unlocked Passive C
      3, 4, 5, 12, 13   Unknown
      Unlocked skills do not always match their categories, but this only
      occurs on 5 of the launch heroes.
instances:
  legendary:
    type: legendary_info
    pos: legendary_ptr.offset+ 0x20
    if: legendary_ptr.offset != 0
    repeat: expr
    repeat-expr: 1
