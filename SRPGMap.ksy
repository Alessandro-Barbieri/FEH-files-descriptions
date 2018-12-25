meta:
  id: srpgmap
  file-extension: bin
  imports:
    - map_definition
    - file_ptr
    - file_tag
  endian: le
doc: |
  The contents of an HSDArc archive. 
seq:
  - id: hsdarcbuffer
    type: hsdarc_buffer
types:
  hsdarc_buffer:
    seq:
      - id: archive_size
        type: u4
        doc: |
          Size of the HSDArc archive in bytes.
      - id: ptr_list_offset
        type: u4
        doc: |
          Absolute file offset pointer into the relocatable pointer list. Like
          `file_ptr`, the actual pointed-to file offset is
          `ptr_list_offset + 0x20`
      - id: ptr_list_length
        type: u4
        doc: |
          Number of entries of the relocatable pointer list.
      - id: tag_list_length
        type: u4
        doc: |
          Number of tag strings present in `tag_list`.
      - id: unknown1
        type: u4
      - id: unknown2
        type: u4
      - id: magic
#        type: u8
        contents: [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
        doc: |
           `0` on HSDArc archive files, `48 53 44 41 72 63 00 00`
           (`"HSDArc\0\0"`) once the archive is loaded into memory.
      - id: mapdefinition
        type: map_definition
    instances:
      ptr_list:
        type: file_ptr
        pos: ptr_list_offset + 0x20
        repeat: expr
        repeat-expr: ptr_list_length
        doc: |
          The relocatable pointer list. Each entry on this table points to
          another file offset pointer, which may point to anything depending on
          interpretation. While loading the archive into memory, pointers
          referred to by this table are converted into absolute memory pointers,
          by adding the address of hsdarc_buffer::data to their values; pointers
          on this list itself remain unaltered. (Note that this allows archive
          files to be restored from raw memory.)
      tag_list:
        type: file_tag
        pos: ptr_list_length + ptr_list_offset + 0x20
        repeat: expr
        repeat-expr: tag_list_length
        doc: |
          A list of objects with tag strings associated to them.
#       tags:
#        pos:
#        type: strz
#        encoding: UTF-8
#        repeat: eos
#        doc: |
#          Null-terminated tag strings. It is possible that some of the tag
#          strings are not associated with any object.