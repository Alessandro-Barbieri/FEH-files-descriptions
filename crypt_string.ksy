meta:
  id: crypt_string
  endian: le
  imports:
    - file_ptr
params:
  - id: cipher
    type: str
seq:
  - id: crypt_string_ptr
    type: file_ptr
instances:
  crypt_string:
    type: crypt_string_buffer
    pos:  crypt_string_ptr.offset + 0x20
    if: crypt_string_ptr.offset != 0
types:
  crypt_string_buffer:
    seq:
      - id: buffer
        type: string
        terminator: 0
        process: decrypt_string([0x81,0x00,0x80,0xA4,0x5A ,0x16 ,0x6F,0x78 ,0x57 ,0x81 ,0x2D,0xF7,0xFC ,0x66 ,0x0F ,0x27 ,0x75 ,0x35 ,0xB4 ,0x34,0x10,0xEE ,0xA2 ,0xDB,0xCC ,0xE3 ,0x35 ,0x99,0x43 ,0x48 ,0xD2 ,0xBB ,0x93 ,0xC1])
      - id: padding
        size: (8 - _io.pos) % 8
  string:
    seq:
      - id: value
        type: str
        size-eos: true
        encoding: UTF-8