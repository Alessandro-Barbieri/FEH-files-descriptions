meta:
  id: srpgweapon
  file-extension: bin
  imports:
    - file_ptr
    - file_tag
    - obj_list
  endian: le
  license:	CC-BY-NC-SA-3.0
doc-ref:	https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#hsdarc_buffer
seq:
  - id: hsdarcbuffer
    type: hsdarc_buffer
types:
  hsdarc_buffer:
    seq:
      - id: archive_size
        type: u4
      - id: ptr_list_offset
        type: u4
      - id: ptr_list_length
        type: u4
      - id: tag_list_length
        type: u4
      - id: unknown1
        type: u4
      - id: unknown2
        type: u4
      - id: magic
        type: u8
      - id: skill_list
        type: obj_list('weapon_class_definition',[0x4f,0x4c,0x66,0x6d,0xeb,0x17,0xba,0xa7])
		doc-ref:	https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Weapon_class_definitions
    instances:
      ptr_list:
        type: file_ptr
        pos: ptr_list_offset + 0x20
        repeat: expr
        repeat-expr: ptr_list_length
      tag_list:
        type: file_tag
        pos: ptr_list_length + ptr_list_offset + 0x20
        repeat: expr
        repeat-expr: tag_list_length
#      tags:
#        type: strz
#        encoding: UTF-8
#        repeat: eos