meta:
  id: srpgperson
  file-extension: bin
  imports:
    - file_ptr
    - file_tag
    - obj_list
  endian: le
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
        type: obj_list('hero_definition',[0xe1,0xb9,0x3a,0x3c,0x79,0xab,0x51,0xde])
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