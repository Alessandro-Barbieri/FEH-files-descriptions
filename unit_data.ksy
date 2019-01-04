meta:
  id: unit_data
  imports:
    - encrypted
    - crypt_string
    - stats_tuple
    - field_definition
    - map_position
  endian: le
  license: CC-BY-NC-SA-3.0
doc: Definition of a single unit placed on the map.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#unit_data
seq:
  - id: id_tag
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the unit. Begins with `PID_` for heroes,
      and `EID_` for enemy-only units.
  - id: skills
    type: crypt_string('ID')
    repeat: expr
    repeat-expr:  7
    doc: |
      If non-null, the entries point to the internal skill identifiers for the
      following slots respectively, in that order: Weapon, Assist, Special,
      Passive A, Passive B, Passive C, Sacred Seal.
  - id: accessory
    type: crypt_string('ID')
    doc: |
      If non-null, points to the internal string identifier of the accessory
      equipped by the unit (begins with `DAID_`).
  - id: pos
    type: map_position
    doc: Initial coordinates of the unit.
  - id: rarity
    size: 1
    type: encrypted('xoru1')
    process: xor([0x61])
    doc: Rarity of the unit.
  - id: lv
    size: 1
    type: encrypted('xoru1')
    process: xor([0x2a])
    doc: Displayed level of the unit.
  - id: cooldown_count
    size: 1
    type: encrypted('xors1')
    process: xor([0x1e])
    doc: |
      The initial Special cooldown count of the unit, or `-1` to use the
      default value.
  - id: unknown1
    type: u1
  - id: stats
    type: stats_tuple
    doc: Base stats of the unit when all skills are unequipped.
  - id: start_turn
    size: 1
    type: encrypted('xors1')
    process: xor([0xcf])
    doc: |
     The first turn by which the unit starts moving regardless of the movement
     group it belongs to, or `-1` if the unit does not move until an opponent
     engages any unit of the unit's movement group.
  - id: movement_group
    size: 1
    type: encrypted('xors1')
    process: xor([0xf4])
    doc: |
     An index shared between units which start moving together; engaging any
     unit causes all units with the same `movement_group` value to start moving
     (unless `movement_delay` is set and that particular unit is not engaged).
     A value of `-1` means the unit belongs to its own group.
  - id: movement_delay
    size: 1
    type: encrypted('xors1')
    process: xor([0x95])
    doc: |
      Once the unit's movement group starts moving, waits for up to
      `movement_delay` turns until this unit is engaged, or moves immediately
      if this value is equal to `-1`.
  - id: break_terrain
    size: 1
    type: encrypted('xorb1')
    process: xor([0x71])
    doc: Whether the unit considers breakable terrain as breakable.
  - id: tether
    size: 1
    type: encrypted('xorb1')
    process: xor([0xb8])
    doc: |
      Whether the unit returns to its initial position if it cannot find any
      moves to make.
  - id: true_lv
    size: 1
    type: encrypted('xoru1')
    process: xor([0x85])
    doc: |
      Internal level of the unit. The `+` is shown if this is higher than the
      displayed level.
  - id: is_enemy
    size: 1
    type: encrypted('xorb1')
    process: xor([0xd0])
    doc: |
      True if the unit is a foe, false if ally. For permanent maps this
      remained unused until the introduction of Tactics Drills.
  - id: padding
    size: 1
  - id: spawn_check
    type: crypt_string('ID')
    doc: |
      If non-null, points to an internal unit string identifier used to check
      whether a reinforcement should be spawned.
  - id: spawn_count
    size: 1
    type: encrypted('xors1')
    process: xor([0x0A])
    doc: |
      If this unit appears as a reinforcement, the number of units that can be
      spawned; otherwise this field is `-1` and the unit appears initially.
  - id: spawn_turns
    size: 1
    type: encrypted('xors1')
    process: xor([0x0A])
    doc: |
      Number of turns to wait before the unit is allowed to spawn (i.e. the
      unit will spawn as early as the end of Turn `spawn_turns` enemy phase or
      the start of Turn (`spawn_turns + 1`) player phase), or `-1` if the unit
      can spawn on any turn.
  - id: spawn_target_remain
    size: 1
    type: encrypted('xors1')
    process: xor([0x2d])
    doc: |
      If not `-1`, this unit spawns only when the number of units with internal
      identifier `spawn_check` is equal to `spawn_target_remain`. (Existing map
      files only use `0` so far.)
  - id: spawn_target_kills
    size: 1
    type: encrypted('xors1')
    process: xor([0x5b])
    doc: |
      If not -`1`, this unit spawns only when at least `spawn_target_kills`
      units with internal identifier `spawn_check` are defeated.
