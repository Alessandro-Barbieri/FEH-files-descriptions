meta:
  id: legendary_info
  imports:
    - stats_tuple
    - legendary_element
  license: CC-BY-NC-SA-3.0
doc: The struct that defines the element and ally boosts of a Legendary Hero.
doc-ref: https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#legendary_info
seq:
  - id: bonus_effect
    type: stats_tuple
  - id: element
    type: legendary_element
    process: xor([0x05])
    size: 1
  - id: padding
    size: 7
