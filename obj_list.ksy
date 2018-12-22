meta:
  id: obj_list
  endian: le
  imports:
    - file_ptr
    - xoru8
params:
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