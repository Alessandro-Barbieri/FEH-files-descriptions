meta:
  id: legendary_info
  imports:
    - stats_tuple
    - legendary_element
seq:
  - id: bonus_effect
    type: stats_tuple
  - id: element
    type: legendary_element
    process:  xor([0x05])
    size: 1
  - id: padding
    size:  7