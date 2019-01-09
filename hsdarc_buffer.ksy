meta:
  id: hsdarc_buffer
  file-extension: bin
  imports:
    - encrypted
    - enemy_definition
    - field_gfx_definition
    - file_ptr
    - file_tag
    - hero_definition
    - map_definition
    - skill_definition
    - terrain_definition
    - weapon_class_definition
  license:  CC-BY-NC-SA-3.0
  endian: le
doc: |
  The contents of an HSDArc archive.
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#hsdarc_buffer
params:
  - id: type
    type: str
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
  - id: magic_bytes
    contents: [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
    doc: |
       `0` on HSDArc archive files, `48 53 44 41 72 63 00 00` (`"HSDArc\0\0"`)
       once the archive is loaded into memory.
  - id: data
    type:
      switch-on: type
      cases:
        '"enemy"': obj_list('enemy_definition',[0x5c,0x34,0xc5,0x9c,0x11,0x95,0xca,0x62])
        '"field"': obj_list('field_gfx_definition',[0x58,0xbc,0xdf,0xca,0x3c,0x08,0x90,0x1d])
        '"map"': map_definition
        '"person"': obj_list('hero_definition',[0xe1,0xb9,0x3a,0x3c,0x79,0xab,0x51,0xde])
        '"skill"': obj_list('skill_definition',[0xad,0xe9,0xde,0x4a,0x07,0xc7,0xec,0x7f])
        '"terrain"': obj_list('terrain_definition',[0x3c,0x93,0x7c,0xa8,0xa3,0x2d,0x25,0x22])
        '"weapon"': obj_list('weapon_class_definition',[0x4f,0x4c,0x66,0x6d,0xeb,0x17,0xba,0xa7])
instances:
  ptr_list:
    type: file_ptr
    pos: ptr_list_offset + 0x20
    repeat: expr
    repeat-expr: ptr_list_length
    doc: |
      The relocatable pointer list. Each entry on this table points to another
      file offset pointer, which may point to anything depending on
      interpretation. While loading the archive into memory, pointers referred
      to by this table are converted into absolute memory pointers, by adding
      the address of hsdarc_buffer::data to their values; pointers on this list
      itself remain unaltered. (Note that this allows archive files to be
      restored from raw memory.)
  tag_list:
    type: file_tag
    pos: ptr_list_length + ptr_list_offset + 0x20
    repeat: expr
    repeat-expr: tag_list_length
    doc: |
      A list of objects with tag strings associated to them.
# tags:
#   pos:
#   type: strz
#   encoding: UTF-8
#   repeat: eos
#   doc: |
#     Null-terminated tag strings. It is possible that some of the tag strings
#     are not associated with any object.
types:
  obj_list:
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
        type: encrypted('xoru8')
        size: 8
        process: xor(key)
        doc: Number of objects on the list.
    instances:
      object_list:
        type:
          switch-on: type
          cases:
            '"enemy_definition"': enemy_definition
            '"field_gfx_definition"': field_gfx_definition
            '"hero_definition"': hero_definition
            '"skill_definition"': skill_definition
            '"terrain_definition"': terrain_definition
            '"weapon_class_definition"': weapon_class_definition
        pos: list_ptr.offset + 0x20
        repeat: expr
        repeat-expr: size.data
        if: list_ptr.offset != 0
        doc: Pointer to the array of objects. Usually `0x10` (points to `$30`).
