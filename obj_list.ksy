meta:
  id: obj_list
  endian: le
  imports:
    - file_ptr
    - xoru8
    - weapon_class_definition
    - hero_definition
  license:	CC-BY-NC-SA-3.0
doc-ref:	https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#obj_list.3CT.2C_xor.3E
params:
  - id: type
    type: str
  - id: key
    repeat: expr
    repeat-expr: 8
seq:
  - id: list_ptr
    type: file_ptr
  - id:  size
    type: xoru8
    size: 8
    process:  xor(key)
instances:
  object_list:
    type:
      switch-on: type
      cases:
        '"hero_definition"': hero_definition
        '"weapon_class_definition"': weapon_class_definition
    pos: list_ptr.offset + 0x20
    repeat: expr
    repeat-expr: size.data
    if: list_ptr.offset != 0