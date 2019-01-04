meta:
  id: encrypted
  endian: le
  license:  CC0-1.0
params:
  - id: typ
    type: str
seq:
  - id: data
    type:
      switch-on: typ
      cases:
        '"xorb1"': b1
        '"xoru1"': u1
        '"xoru2"': u2
        '"xoru4"': u4
        '"xoru8"': u8
        '"xors1"': s1
        '"xors2"': s2
        '"xors4"': s4
        '"xors8"': s8
