meta:
  id: field_gfx_definition
  imports:
    - crypt_string
  endian: le
  license: CC-BY-NC-SA-3.0
doc: The files at `Common/SRPG/Field/` define the graphical assets maps use.
doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#field_gfx_definition
seq:
  - id: map_id
    type: crypt_string('ID')
    doc: |
      The internal identifier of the map. Additionally, `CHIP0` is used for all
      generic outdoor maps, and `CHIP1` for indoor maps.
  - id: wall_ptr
    type: file_ptr
  - id: backdrop_ptr
    type: file_ptr
  - id: overlay_ptr
    type: file_ptr
  - id: anim
    type: crypt_string('NONE')
instances:
  wall:
    type: gfx_resource
    pos: wall_ptr.offset+ 0x20
    if: wall_ptr.offset != 0
    repeat: expr
    repeat-expr: 1
    doc: |
      The sprites for wall terrains. Walls are only drawn if at least one wall
      tile is breakable; otherwise, wall graphics are directly embedded in the
      map image.
  backdrop:
    type: gfx_resource
    pos: backdrop_ptr.offset+ 0x20
    if: backdrop_ptr.offset != 0
    repeat: expr
    repeat-expr: 1
    doc: The sprite for the map's backdrop.
  overlay:
    type: gfx_resource
    pos: overlay_ptr.offset+ 0x20
    if: overlay_ptr.offset != 0
    repeat: expr
    repeat-expr: 2
    doc: The sprites for the map's overlays. Up to 2 can be defined.
types:
  gfx_resource:
    seq:
      - id: kind
        type: crypt_string('ID')
        doc: A descriptive string for the asset.          
      - id: filename
        type: crypt_string('NONE')
        doc: |
          If non-null, points to the asset's filename relative to
          `Common/Field/Common`. Otherwise this asset has no visible sprites.
    doc: A single graphical asset. 
    doc-ref: https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#gfx_resource_t
