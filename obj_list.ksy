meta:
  id: obj_list
  endian: le
  imports:
    - xoru8
    - file_ptr
    - encrypted
    - weapon_class_definition
    - hero_definition
    - terrain_definition
    - enemy_definition
  license: CC-BY-NC-SA-3.0
doc: |
  Generic object list. A variety of files consist of a single list, pointed
  from the first relocatable pointer (always to `$20`).
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#obj_list.3CT.2C_xor.3E
params:
  - id: type
    type: str
  - id: key
    repeat: expr
    repeat-expr: 8
seq:
  - id: list_ptr
    type: file_ptr
  - id: size
    type: xoru8
    size: 8
    process: xor(key)
    doc: Number of objects on the list.
instances:
  object_list:
    type:
      switch-on: type
      cases:
        '"enemy_definition"': enemy_definition
        '"hero_definition"': hero_definition
        '"terrain_definition"': terrain_definition
        '"weapon_class_definition"': weapon_class_definition
    pos: list_ptr.offset + 0x20
    repeat: expr
    repeat-expr: size.data
    if: list_ptr.offset != 0
    doc: Pointer to the array of objects. Usually `0x10` (points to `$30`).
