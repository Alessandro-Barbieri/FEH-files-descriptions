meta:
  id: srpgmap
  file-extension: bin
  imports:
    - map_definition
    - file_ptr
    - file_tag
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
      - id: mapdefinition
        type: map_definition
    instances:
      ptr_list:
        type: file_ptr
        pos: ptr_list_offset + 0x20
        repeat: expr
        repeat-expr: ptr_list_length
        if: ptr_list_offset != 0
      tag_list:
        type: file_tag
        pos: ptr_list_length + ptr_list_offset + 0x20
        repeat: expr
        repeat-expr: tag_list_length
#      tags:
#        pos:
#        type: strz
#        encoding: UTF-8
#        repeat: eos