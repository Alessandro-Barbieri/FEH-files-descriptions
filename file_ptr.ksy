meta:
  id: file_ptr
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  Generic absolute file offset pointer. The actual pointed-to file offset is the
  value of the pointer + `0x20`, since the archives have a 32-byte header. As a
  special case, `0` points to nowhere, and is used to indicate absence of
  pointed-to data (much like the real nullptr).
  File offsets inside the data section of each archive are replaced with
  absolute pointers to raw memory when the archives are loaded into memory. File
  pointers on the relocatable pointer list (`hsdarc_buffer::ptr_list`) are never
  null; if their value is `0`, they point to the pointer at `$20`.
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#file_ptr_t.3CT.3E
seq:
  - id: offset
    type: u8
