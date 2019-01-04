meta:
  id: terrain_definition
  imports:
    - encrypted
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  The file `Common/SRPG/Terrain.bin` defines all 31 terrains used in the game.
  These only handle the gameplay aspects; animation background is defined
  elsewhere. Movement costs are defined in `Common/SRPG/Move.bin.lz`.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#terrain_definition
seq:
  - id: index
    size: 4
    type: encrypted('xoru4')
    process: xor([0xab,0xa1,0xe0,0xda])
    doc: The index of the terrain.
  - id: base_terrain
    size: 4
    type: encrypted('xors4')
    process: xor([0xd2,0x7d,0xd0,0x6f])
    doc: |
      The terrain index to use when this terrain is destroyed by an ally, or
      `-1` if this terrain is not breakable by allies.
  - id: foe_base_terrain
    size: 4
    type: encrypted('xors4')
    process: xor([0xd2,0x7d,0xd0,0x6f])
    doc: |
      The terrain index to use when this terrain is destroyed by a foe, or `-1`
      if this terrain is not breakable by foes. Used in Rival Domains and
      Grand Conquests.
  - id: side
    size: 1
    type: encrypted('xors1')
    process: xor([0x21])
    doc: |
      `0` if the terrain belongs to the player, `1` if enemy, `-1` otherwise.
  - id: terrain_group
    size: 1
    type: encrypted('xoru1')
    process: xor([0xcb])
  - id: inaccessible
    size: 1
    type: encrypted('xorb1')
    process: xor([0x16])
    doc: |
      True if the terrain cannot be entered by any unit. Certain tiles such as
      the banners from Tactics Drills are inaccessible but not wall terrains.
  - id: hp
    size: 1
    type: encrypted('xoru1')
    process: xor([0xba])
    doc: Number of hits the terrain can take before it is destroyed.
  - id: is_wall
    size: 1
    type: encrypted('xorb1')
    process: xor([0xa8])
    doc: |
      True for wall terrains, false otherwise. Wall terrains use different tile
      graphics depending on whether adjacent tiles are also walls (except
      breakable ice and crates because these tilemaps have identical graphics
      for all directions).
  - id: is_liquid
    size: 1
    type: encrypted('xorb1')
    process: xor([0x7c])
    doc: |
      `True` for water bodies and lava, `false` otherwise.
  - id: is_bridge
    size: 1
    type: encrypted('xorb1')
    process: xor([0x08])
    doc: |
      `True` for bridge terrains, `false` otherwise.
  - id: is_trench
    size: 1
    type: encrypted('xorb1')
    process: xor([0x30])
    doc: |
      `True` for trench terrains, `false` otherwise.
  - id: is_fortress
    size: 1
    type: encrypted('xorb1')
    process: xor([0xda])
    doc: |
      Whether destroying this terrain causes a victory or loss. Used for playe
      and enemy fortresses.
  - id: is_rd_terrain
    size: 1
    type: encrypted('xorb1')
    process: xor([0xcd])
    doc: |
      True for the special terrains used in Rival Domains and Grand Conquests,
      false otherwise.
  - id: mit_mod
    size: 1
    type: encrypted('xoru1')
    process: xor([0xaa])
    doc: |
      Mitigation modifier as a percentage; `30` for defensive terrain, `0`
      otherwise.
  - id: regen_hp
    size: 1
    type: encrypted('xoru1')
    process: xor([0x7d])
    doc: |
      Amount of HP regenerated on each turn; `10` for fortresses and camps, `0`
      otherwise.
