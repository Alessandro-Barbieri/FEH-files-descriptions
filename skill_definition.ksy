meta:
  id: skill_definition
  imports:
    - badge_color
    - crypt_string
    - encrypted
    - magic_element
    - stats_tuple
    - xorb1
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  All skills, including refined weapons and exclusive skill refinements, are
  defined in the files at Common/SRPG/Skill/.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Skill_definitions
seq:
  - id: id_tag
    type: crypt_string('ID')
    doc: |
      Full internal string identifier of the skill, e.g. SID_ジークリンデ_共 for
      Sieglinde.
  - id: refine_base
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the unrefined version of the weapon, e.g.
      SID_ジークリンデ.
  - id: name_id
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the skill name resource, e.g. MSID_ジークリンデ.
  - id: desc_id
    type: crypt_string('ID')
    doc: |
       Internal string identifier of the skill description resource, e.g.
       MSID_H_ジークリンデ改.
  - id: refine_id
    type: crypt_string('ID')
    doc: |
        Internal string identifier of the skill that gives rise to the refined
        skill effect, e.g. SID_強化共有R.
  - id: prerequisites
    type: crypt_string('ID')
    repeat: expr
    repeat-expr:  2
    doc: |
        Internal string identifiers of skills required to learn the current
        skill.
  - id: next_skill
    type: crypt_string('ID')
    doc: |
        Internal string identifier of the canonical upgrade of the current
        skill. It is defined if and only if `promotion_rarity` is not zero.
  - id: sprites
    type: crypt_string('NONE')
    repeat: expr
    repeat-expr: 4
    doc: |
        Filenames of the sprites used by the weapon, in this order: bow,
        weapon / arrow, map animation, AoE Special map animation.
  - id: stats
    type: stats_tuple
    doc: |
      Permanent stat bonuses of the skill. For weapons this does not include
      might.
  - id: class_params
    type: stats_tuple
    doc: |
      A set of extra parameters that are used only for skill effects common to
      weapon classes for which `weapon_class_definition::is_staff`,
      `is_dagger`, or `is_breath` is true:
      * `is_staff`: If `class_params.hp = 1`, damage from unit's staff will be
         calculated the same as other weapons If `class_params.hp = 2`, foe
         cannot counterattack.
      * `is_dagger`: After combat, if unit attacked, inflicts
        `stat+class_params` on target and foes within `class_params.hp` spaces
        of target through their next actions.
      * `is_breath`: If `class_params.hp = 1`, and if `target_mov` foe uses
        `target_wep`, calculates damage using the lower of foe's Def or Res.
  - id: skill_params
    type: stats_tuple
    doc: |
      Various skill parameters packed into a stat tuple. These do not
      necessarily represent stat values. Their meanings depend on the skill
      abilities.
  - id: refine_stats
    type: stats_tuple
    doc: |
      Stat bonuses of the skill's refinement, as shown on the weapon
      description.
  - id: num_id
    size: 4
    type: encrypted('xoru4')
    process: xor([0x0c,0x41,0xd3,0x90])
    doc: |
      A unique increasing index for every skill, added to `0x10000000` for
      refined weapons.
  - id: sort_id
    size: 4
    type: encrypted('xoru4')
    process: xor([0x23,0x3a,0xa5,0xc6])
    doc: |
      The internal sort value used in places such as the skill inheritance menu
      to order skills within the same category according to their skill
      families.
  - id: icon_id
    size: 4
    type: encrypted('xoru4')
    process: xor([0xac,0xf8,0xdb,0x8d])
    doc: |
      The icon index of the skill, referring to the files
      `UI/Skill_Passive*.png`.
  - id: wep_equip
    size: 4
    type: encrypted('xoru4')
    process: xor([0x73,0x21,0xdf,0xc6])
    doc: |
      A bitmask indexed by `weapon_index`, with bits set for weapon classes
      that can equip the current skill.
  - id: mov_equip
    size: 4
    type: encrypted('xoru4')
    process: xor([0xeb,0x18,0x28,0xab])
    doc: |
      A bitmask indexed by `move_index`, with bits set for movement classes
      that can equip the current skill.
  - id: sp_cost
    size: 4
    type: encrypted('xoru4')
    process: xor([0x69,0xf6,0x31,0xc0])
    doc: SP required to learn the given skill.
  - id: category
    size: 1
    type: encrypted('xoru1')
    process: xor([0xbc])
    doc: Category of the skill.
  - id: tome_class
    size: 1
    type: magic_element
    process: xor([0xf1])
    doc: The element type for tome weapon skills.
  - id: exclusive
    size: 1
    type: xorb1
    process: xor([0xcc])
    doc: True if the skill cannot be inherited.
  - id: enemy_only
    size: 1
    type: xorb1
    process: xor([0x4f])
    doc: True if the skill can only be equipped by enemies.
  - id: range
    size: 1
    type: encrypted('xoru1')
    process: xor([0x56])
    doc: Range of the skill for weapons and Assists, 0 for other skills.
  - id: might
    size: 1
    type: encrypted('xoru1')
    process: xor([0xd2])
    doc: |
      Might for weapon skills, including bonuses that come from refinements, 0
      for other skills.
  - id: cooldown_count
    size: 1
    type: encrypted('xors1')
    process: xor([0x56])
    doc: |
      Cooldown count of the skill. The total cooldown count of a unit is the
      sum of `cooldown_count` for all equipped skills. Skills that accelerate
      Special trigger have a negative value.
  - id: assist_cd
    size: 1
    type: xorb1
    process: xor([0xf2])
    doc: |
      True if the skill grants Special cooldown count-1 to the unit after this
      Assist is used.
  - id: healing
    size: 1
    type: xorb1
    process: xor([0x95])
    doc: True if the skill is a healing Assist skill.
  - id: skill_range
    size: 1
    type: encrypted('xoru1')
    process: xor([0x09])
    doc: |
      Range of the skill effect that comes with the given skill, e.g. 1 for
      Hone skills and weapons that give equivalent skill effects.
  - id: score
    type: encrypted('xoru2')
    size: 2
    process: xor([0x32 ,0xA2])
    doc: A value that roughly corresponds to the SP cost of the skill.
  - id: promotion_tier
    type: encrypted('xoru1')
    size: 1
    process: xor([0xE0])
    doc: |
      `2` for a few low-tier Specials and staff weapons / Assists, `0` for
      highest-tier skills, and `1` for everything else. Used by derived maps to
      determine how far skills are allowed to promote.
  - id: promotion_rarity
    type: encrypted('xoru1')
    size: 1
    process: xor([0x75])
    doc: |
      If non-zero, this skill would be promoted on derived maps if the unit's
      rarity is greater than or equal to this value.
  - id: refined
    type: xorb1
    size: 1
    process: xor([0x02])
    doc: |
      True if the skill is a refined weapon.
  - id: refine_sort_id
    type: encrypted('xoru1')
    size: 1
    process: xor([0xFC])
    doc: |
      Internal sort value for refined weapons: `1` and `2` for skills,
      `101` – `104` for Atk/Spd/Def/Res refinements, `0` otherwise.
  - id: wep_effective
    type: encrypted('xoru4')
    size: 4
    process: xor([0x43 ,0x3D ,0xBE ,0x23])
    doc: |
      A bitmask indexed by `weapon_index`, representing weapon class
      effectivenesses this skill grants. Only meaningful on weapon skills.
  - id: mov_effective
    type: encrypted('xoru4')
    size: 4
    process: xor([0xEB ,0xDA ,0x3F ,0x82])
    doc: |
      A bitmask indexed by `move_index`, representing movement class
      effectivenesses this skill grants. Only meaningful on weapon skills.
  - id: wep_shield
    type: encrypted('xoru4')
    size: 4
    process: xor([0x43 ,0xB7 ,0xBA ,0xAA])
    doc: |
      A bitmask indexed by `weapon_index`, representing weapon class
      effectivenesses this skill protects from. Used by Breath of Blight.
  - id: mov_shield
    type: encrypted('xoru4')
    size: 4
    process: xor([0x5B ,0xF2 ,0xBE ,0x0E])
    doc: |
      A bitmask indexed by `move_index`, representing movement class
      effectivenesses this skill protects from.
  - id: wep_weakness
    type: encrypted('xoru4')
    size: 4
    process: xor([0xAF ,0x02 ,0x5A ,0x00])
    doc: |
       A bitmask indexed by `weapon_index`, representing weapon class
       weaknesses this skill grants. Used by Loptous.
  - id: mov_weakness
    type: encrypted('xoru4')
    size: 4
    process: xor([0x19 ,0xB8 ,0x69 ,0xB2])
    doc: |
      A bitmask indexed by `move_index`, representing movement class
      weaknesses this skill grants.
  - id: wep_adaptive
    type: encrypted('xoru4')
    size: 4
    process: xor([0x29 ,0x26 ,0x4E ,0x49])
    doc: |
      A bitmask indexed by `weapon_index`, representing weapon classes that
      receive damage from this skill calculated using the lower of Def or Res.
      Used by breaths. Only meaningful on weapon skills.
  - id: mov_adaptive
    type: encrypted('xoru4')
    size: 4
    process: xor([0x2E ,0xEF ,0x6C ,0xEE])
    doc: |
      A bitmask indexed by `move_index`, representing movement classes that
      receive damage from this skill calculated using the lower of Def or Res.
      Currently unused. Only meaningful on weapon skills.
  - id: timing_id
    type: encrypted('xoru4')
    size: 4
    process: xor([0x48 ,0x66 ,0x77 ,0x9C])
    doc: |
      An index into the string table in `Common/SRPG/SkillTiming.bin`
      indicating the moment where the skill triggers.
  - id: ability_id
    type: encrypted('xoru4')
    size: 4
    process: xor([0x25 ,0x73 ,0xB0 ,0x72])
    doc: |
      An index into the string table in `Common/SRPG/SkillAbility.bin`
      indicating the skill effect type. A skill can only contain one skill
      effect (refined weapons have an extra skill effect if `refine_id` is
      non-null).
  - id: limit1_id
    type: encrypted('xoru4')
    size: 4
    process: xor([0x32 ,0xB8 ,0xBD ,0x0E])
    doc: |
      An index into the string table in `Common/SRPG/SkillTiming.bin`
      indicating the skill's activation restriction.
  - id: limit1_params
    size: 2
    type: encrypted('xors2')
    repeat: expr
    repeat-expr: 2
    process: xor([0x90 ,0xA5])
    doc: Restriction-dependent parameters.
  - id: limit2_id
    type: encrypted('xoru4')
    size: 4
    process: xor([0x32 ,0xB8 ,0xBD ,0x0E])
    doc: |
      An additional activation restriction on the given skill. Both must be
      satisfied for the skill to activate.
  - id: limit2_params
    size: 2
    type: encrypted('xors2')
    process: xor([0x90 ,0xA5])
    repeat: expr
    repeat-expr: 2
    doc: |
      An additional activation restriction on the given skill. Both must be
      satisfied for the skill to activate.
  - id: target_wep
    type: encrypted('xoru4')
    size: 4
    process: xor([0xD7 ,0xC9 ,0x9F ,0x40])
    doc: |
      A bitmask indexed by `weapon_index`, representing the target's weapon
      classes required for the skill's effect to activate. If zero, works on
      all weapon classes.
  - id: target_mov
    type: encrypted('xoru4')
    size: 4
    process: xor([0x22 ,0xD1 ,0x64 ,0x6C])
    doc: |
      A bitmask indexed by `move_index`, representing the target's movement
      classes required for the skill's effect to activate. If zero, works on
      all movement classes.
  - id: passive_next
    type: crypt_string('ID')
    doc: |
       Like `next_skill`, except that this field is null for weapons,
       Spur Atk 2 does not point to Spur Atk 3, and similarly for the three
       other Spur passives.
  - id: timestamp
    type: encrypted('xors8')
    size: 8
    process: xor([0x51 ,0x9F ,0xFE ,0x3B ,0xF9 ,0x39 ,0x3F ,0xED])
    doc: |
      A POSIX timestamp relative to the skill's release date; half a month into
      the future for skills released before Version 2.0.0, 1 month into the
      future for skills released since Version 2.0.0. This skill would appear
      in the Training Tower if timestamp is not -1 and the current time is past
      timestamp.
  - id: unknown1
    type: encrypted('xoru1')
    size: 1
    process: xor([0x10])
  - id: min_lv
    type: encrypted('xoru1')
    size: 1
    process: xor([0x90])
    doc: |
      If non-zero, represent the lowest level that allow random units to equip
      the given skill.
  - id: max_lv
    type: encrypted('xoru1')
    size: 1
    process: xor([0x24])
    doc: |
      If non-zero, represent the highest levelthat allow random units to equip
      the given skill.
  - id: unknown2
    type: encrypted('xoru1')
    size: 1
    process: xor([0x19])
  - id: unknown3
    type: encrypted('xoru1')
    size: 1
    process: xor([0xBD])
  - id: padding
    size: 3
  - id: id_tag2
    type: crypt_string('ID')
    doc: Identical to id_tag.
  - id: next_seal
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the Sacred Seal a tier above the given
      skill, if it exists. Does not branch into compound skills
      (e.g. Attack +1 goes to Attack +2).
  - id: prev_seal
    type: crypt_string('ID')
    doc: |
      Internal string identifier of the Sacred Seal a tier below the given
      skill, if it exists. Inverse of next_seal; for compound skills, does not
      merge into their base skills (e.g. HP Res 1.png HP/Res 1 does not have a
      prev_seal).
  - id: ss_coin
    type: encrypted('xoru2')
    size: 2
    process: xor([0x40 ,0xC5])
    doc: |
       Number of Sacred Coins required to create the Sacred Seal or enhance
       from prev_seal. Whether a skill is available as a Sacred Seal depends on
       the files in `Common/SRPG/SkillAccessory/`.
  - id: ss_badge_type
    size: 2
    type: badge_color
    process: xor([0x0F ,0xD5])
    doc: |
      The Badge type used for Sacred Seal creation / enhancement.
  - id: ss_badge
    type: encrypted('xoru2')
    size: 2
    process: xor([0xEC ,0x8C])
    doc: |
      Number of Badges required to create the Sacred Seal or enhance from
      `prev_seal`.
  - id: ss_great_badge
    type: encrypted('xoru2')
    size: 2
    process: xor([0xFF ,0xCC])
    doc: |
      Number of Great Badges required to create the Sacred Seal or enhance from
      `prev_seal`.
