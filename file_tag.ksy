meta:
  id: file_tag
  endian: le
  license: CC-BY-NC-SA-3.0
doc: |
  Generic absolute file offset pointer that additionally associates the
  pointed-to data with a tag string.
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#file_tag_t.3CT.3E
seq:
  - id: ptr
    type: u4
    doc: |
      Same as `file_ptr::ptr`, but with 32 bits instead of 64.
  - id: tag
    type: u8
    doc: |
      Pointer to unencrypted UTF-8 string inside `hsdarc_buffer::tags` that is
      associated with the data. Usually represents filenames.
