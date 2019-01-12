# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from crypt_string import CryptString
from stats_tuple import StatsTuple
from xorb1 import Xorb1
from encrypted import Encrypted
from magic_element import MagicElement
from badge_color import BadgeColor
class SkillDefinition(KaitaiStruct):
    """All skills, including refined weapons and exclusive skill refinements, are
    defined in the files at Common/SRPG/Skill/.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Skill_definitions
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.id_tag = CryptString(u"ID", self._io)
        self.refine_base = CryptString(u"ID", self._io)
        self.name_id = CryptString(u"ID", self._io)
        self.desc_id = CryptString(u"ID", self._io)
        self.refine_id = CryptString(u"ID", self._io)
        self.beast_effect_id = CryptString(u"ID", self._io)
        self.prerequisites = [None] * (2)
        for i in range(2):
            self.prerequisites[i] = CryptString(u"ID", self._io)

        self.next_skill = CryptString(u"ID", self._io)
        self.sprites = [None] * (4)
        for i in range(4):
            self.sprites[i] = CryptString(u"NONE", self._io)

        self.stats = StatsTuple(self._io)
        self.class_params = StatsTuple(self._io)
        self.skill_params = StatsTuple(self._io)
        self.refine_stats = StatsTuple(self._io)
        self._raw__raw_num_id = self._io.read_bytes(4)
        self._raw_num_id = KaitaiStream.process_xor_many(self._raw__raw_num_id, b"\x0C\x41\xD3\x90")
        io = KaitaiStream(BytesIO(self._raw_num_id))
        self.num_id = Encrypted(u"xoru4", io)
        self._raw__raw_sort_id = self._io.read_bytes(4)
        self._raw_sort_id = KaitaiStream.process_xor_many(self._raw__raw_sort_id, b"\x23\x3A\xA5\xC6")
        io = KaitaiStream(BytesIO(self._raw_sort_id))
        self.sort_id = Encrypted(u"xoru4", io)
        self._raw__raw_icon_id = self._io.read_bytes(4)
        self._raw_icon_id = KaitaiStream.process_xor_many(self._raw__raw_icon_id, b"\xAC\xF8\xDB\x8D")
        io = KaitaiStream(BytesIO(self._raw_icon_id))
        self.icon_id = Encrypted(u"xoru4", io)
        self._raw__raw_wep_equip = self._io.read_bytes(4)
        self._raw_wep_equip = KaitaiStream.process_xor_many(self._raw__raw_wep_equip, b"\x73\x21\xDF\xC6")
        io = KaitaiStream(BytesIO(self._raw_wep_equip))
        self.wep_equip = Encrypted(u"xoru4", io)
        self._raw__raw_mov_equip = self._io.read_bytes(4)
        self._raw_mov_equip = KaitaiStream.process_xor_many(self._raw__raw_mov_equip, b"\xEB\x18\x28\xAB")
        io = KaitaiStream(BytesIO(self._raw_mov_equip))
        self.mov_equip = Encrypted(u"xoru4", io)
        self._raw__raw_sp_cost = self._io.read_bytes(4)
        self._raw_sp_cost = KaitaiStream.process_xor_many(self._raw__raw_sp_cost, b"\x69\xF6\x31\xC0")
        io = KaitaiStream(BytesIO(self._raw_sp_cost))
        self.sp_cost = Encrypted(u"xoru4", io)
        self._raw__raw_category = self._io.read_bytes(1)
        self._raw_category = KaitaiStream.process_xor_many(self._raw__raw_category, b"\xBC")
        io = KaitaiStream(BytesIO(self._raw_category))
        self.category = Encrypted(u"xoru1", io)
        self._raw__raw_tome_class = self._io.read_bytes(1)
        self._raw_tome_class = KaitaiStream.process_xor_many(self._raw__raw_tome_class, b"\xF1")
        io = KaitaiStream(BytesIO(self._raw_tome_class))
        self.tome_class = MagicElement(io)
        self._raw__raw_exclusive = self._io.read_bytes(1)
        self._raw_exclusive = KaitaiStream.process_xor_many(self._raw__raw_exclusive, b"\xCC")
        io = KaitaiStream(BytesIO(self._raw_exclusive))
        self.exclusive = Xorb1(io)
        self._raw__raw_enemy_only = self._io.read_bytes(1)
        self._raw_enemy_only = KaitaiStream.process_xor_many(self._raw__raw_enemy_only, b"\x4F")
        io = KaitaiStream(BytesIO(self._raw_enemy_only))
        self.enemy_only = Xorb1(io)
        self._raw__raw_range = self._io.read_bytes(1)
        self._raw_range = KaitaiStream.process_xor_many(self._raw__raw_range, b"\x56")
        io = KaitaiStream(BytesIO(self._raw_range))
        self.range = Encrypted(u"xoru1", io)
        self._raw__raw_might = self._io.read_bytes(1)
        self._raw_might = KaitaiStream.process_xor_many(self._raw__raw_might, b"\xD2")
        io = KaitaiStream(BytesIO(self._raw_might))
        self.might = Encrypted(u"xoru1", io)
        self._raw__raw_cooldown_count = self._io.read_bytes(1)
        self._raw_cooldown_count = KaitaiStream.process_xor_many(self._raw__raw_cooldown_count, b"\x56")
        io = KaitaiStream(BytesIO(self._raw_cooldown_count))
        self.cooldown_count = Encrypted(u"xors1", io)
        self._raw__raw_assist_cd = self._io.read_bytes(1)
        self._raw_assist_cd = KaitaiStream.process_xor_many(self._raw__raw_assist_cd, b"\xF2")
        io = KaitaiStream(BytesIO(self._raw_assist_cd))
        self.assist_cd = Xorb1(io)
        self._raw__raw_healing = self._io.read_bytes(1)
        self._raw_healing = KaitaiStream.process_xor_many(self._raw__raw_healing, b"\x95")
        io = KaitaiStream(BytesIO(self._raw_healing))
        self.healing = Xorb1(io)
        self._raw__raw_skill_range = self._io.read_bytes(1)
        self._raw_skill_range = KaitaiStream.process_xor_many(self._raw__raw_skill_range, b"\x09")
        io = KaitaiStream(BytesIO(self._raw_skill_range))
        self.skill_range = Encrypted(u"xoru1", io)
        self._raw__raw_score = self._io.read_bytes(2)
        self._raw_score = KaitaiStream.process_xor_many(self._raw__raw_score, b"\x32\xA2")
        io = KaitaiStream(BytesIO(self._raw_score))
        self.score = Encrypted(u"xoru2", io)
        self._raw__raw_promotion_tier = self._io.read_bytes(1)
        self._raw_promotion_tier = KaitaiStream.process_xor_many(self._raw__raw_promotion_tier, b"\xE0")
        io = KaitaiStream(BytesIO(self._raw_promotion_tier))
        self.promotion_tier = Encrypted(u"xoru1", io)
        self._raw__raw_promotion_rarity = self._io.read_bytes(1)
        self._raw_promotion_rarity = KaitaiStream.process_xor_many(self._raw__raw_promotion_rarity, b"\x75")
        io = KaitaiStream(BytesIO(self._raw_promotion_rarity))
        self.promotion_rarity = Encrypted(u"xoru1", io)
        self._raw__raw_refined = self._io.read_bytes(1)
        self._raw_refined = KaitaiStream.process_xor_many(self._raw__raw_refined, b"\x02")
        io = KaitaiStream(BytesIO(self._raw_refined))
        self.refined = Xorb1(io)
        self._raw__raw_refine_sort_id = self._io.read_bytes(1)
        self._raw_refine_sort_id = KaitaiStream.process_xor_many(self._raw__raw_refine_sort_id, b"\xFC")
        io = KaitaiStream(BytesIO(self._raw_refine_sort_id))
        self.refine_sort_id = Encrypted(u"xoru1", io)
        self._raw__raw_wep_effective = self._io.read_bytes(4)
        self._raw_wep_effective = KaitaiStream.process_xor_many(self._raw__raw_wep_effective, b"\x43\x3D\xBE\x23")
        io = KaitaiStream(BytesIO(self._raw_wep_effective))
        self.wep_effective = Encrypted(u"xoru4", io)
        self._raw__raw_mov_effective = self._io.read_bytes(4)
        self._raw_mov_effective = KaitaiStream.process_xor_many(self._raw__raw_mov_effective, b"\xEB\xDA\x3F\x82")
        io = KaitaiStream(BytesIO(self._raw_mov_effective))
        self.mov_effective = Encrypted(u"xoru4", io)
        self._raw__raw_wep_shield = self._io.read_bytes(4)
        self._raw_wep_shield = KaitaiStream.process_xor_many(self._raw__raw_wep_shield, b"\x43\xB7\xBA\xAA")
        io = KaitaiStream(BytesIO(self._raw_wep_shield))
        self.wep_shield = Encrypted(u"xoru4", io)
        self._raw__raw_mov_shield = self._io.read_bytes(4)
        self._raw_mov_shield = KaitaiStream.process_xor_many(self._raw__raw_mov_shield, b"\x5B\xF2\xBE\x0E")
        io = KaitaiStream(BytesIO(self._raw_mov_shield))
        self.mov_shield = Encrypted(u"xoru4", io)
        self._raw__raw_wep_weakness = self._io.read_bytes(4)
        self._raw_wep_weakness = KaitaiStream.process_xor_many(self._raw__raw_wep_weakness, b"\xAF\x02\x5A\x00")
        io = KaitaiStream(BytesIO(self._raw_wep_weakness))
        self.wep_weakness = Encrypted(u"xoru4", io)
        self._raw__raw_mov_weakness = self._io.read_bytes(4)
        self._raw_mov_weakness = KaitaiStream.process_xor_many(self._raw__raw_mov_weakness, b"\x19\xB8\x69\xB2")
        io = KaitaiStream(BytesIO(self._raw_mov_weakness))
        self.mov_weakness = Encrypted(u"xoru4", io)
        self._raw__raw_wep_adaptive = self._io.read_bytes(4)
        self._raw_wep_adaptive = KaitaiStream.process_xor_many(self._raw__raw_wep_adaptive, b"\x29\x26\x4E\x49")
        io = KaitaiStream(BytesIO(self._raw_wep_adaptive))
        self.wep_adaptive = Encrypted(u"xoru4", io)
        self._raw__raw_mov_adaptive = self._io.read_bytes(4)
        self._raw_mov_adaptive = KaitaiStream.process_xor_many(self._raw__raw_mov_adaptive, b"\x2E\xEF\x6C\xEE")
        io = KaitaiStream(BytesIO(self._raw_mov_adaptive))
        self.mov_adaptive = Encrypted(u"xoru4", io)
        self._raw__raw_timing_id = self._io.read_bytes(4)
        self._raw_timing_id = KaitaiStream.process_xor_many(self._raw__raw_timing_id, b"\x48\x66\x77\x9C")
        io = KaitaiStream(BytesIO(self._raw_timing_id))
        self.timing_id = Encrypted(u"xoru4", io)
        self._raw__raw_ability_id = self._io.read_bytes(4)
        self._raw_ability_id = KaitaiStream.process_xor_many(self._raw__raw_ability_id, b"\x25\x73\xB0\x72")
        io = KaitaiStream(BytesIO(self._raw_ability_id))
        self.ability_id = Encrypted(u"xoru4", io)
        self._raw__raw_limit1_id = self._io.read_bytes(4)
        self._raw_limit1_id = KaitaiStream.process_xor_many(self._raw__raw_limit1_id, b"\x32\xB8\xBD\x0E")
        io = KaitaiStream(BytesIO(self._raw_limit1_id))
        self.limit1_id = Encrypted(u"xoru4", io)
        self._raw_limit1_params = [None] * (2)
        self.limit1_params = [None] * (2)
        for i in range(2):
            self._raw__raw_limit1_params[i] = self._io.read_bytes(2)
            self._raw_limit1_params = KaitaiStream.process_xor_many(self._raw__raw_limit1_params, b"\x90\xA5")
            io = KaitaiStream(BytesIO(self._raw_limit1_params[i]))
            self.limit1_params[i] = Encrypted(u"xors2", io)

        self._raw__raw_limit2_id = self._io.read_bytes(4)
        self._raw_limit2_id = KaitaiStream.process_xor_many(self._raw__raw_limit2_id, b"\x32\xB8\xBD\x0E")
        io = KaitaiStream(BytesIO(self._raw_limit2_id))
        self.limit2_id = Encrypted(u"xoru4", io)
        self._raw_limit2_params = [None] * (2)
        self.limit2_params = [None] * (2)
        for i in range(2):
            self._raw__raw_limit2_params[i] = self._io.read_bytes(2)
            self._raw_limit2_params = KaitaiStream.process_xor_many(self._raw__raw_limit2_params, b"\x90\xA5")
            io = KaitaiStream(BytesIO(self._raw_limit2_params[i]))
            self.limit2_params[i] = Encrypted(u"xors2", io)

        self._raw__raw_target_wep = self._io.read_bytes(4)
        self._raw_target_wep = KaitaiStream.process_xor_many(self._raw__raw_target_wep, b"\xD7\xC9\x9F\x40")
        io = KaitaiStream(BytesIO(self._raw_target_wep))
        self.target_wep = Encrypted(u"xoru4", io)
        self._raw__raw_target_mov = self._io.read_bytes(4)
        self._raw_target_mov = KaitaiStream.process_xor_many(self._raw__raw_target_mov, b"\x22\xD1\x64\x6C")
        io = KaitaiStream(BytesIO(self._raw_target_mov))
        self.target_mov = Encrypted(u"xoru4", io)
        self.passive_next = CryptString(u"ID", self._io)
        self._raw__raw_timestamp = self._io.read_bytes(8)
        self._raw_timestamp = KaitaiStream.process_xor_many(self._raw__raw_timestamp, b"\x51\x9F\xFE\x3B\xF9\x39\x3F\xED")
        io = KaitaiStream(BytesIO(self._raw_timestamp))
        self.timestamp = Encrypted(u"xors8", io)
        self._raw__raw_unknown1 = self._io.read_bytes(1)
        self._raw_unknown1 = KaitaiStream.process_xor_many(self._raw__raw_unknown1, b"\x10")
        io = KaitaiStream(BytesIO(self._raw_unknown1))
        self.unknown1 = Encrypted(u"xoru1", io)
        self._raw__raw_min_lv = self._io.read_bytes(1)
        self._raw_min_lv = KaitaiStream.process_xor_many(self._raw__raw_min_lv, b"\x90")
        io = KaitaiStream(BytesIO(self._raw_min_lv))
        self.min_lv = Encrypted(u"xoru1", io)
        self._raw__raw_max_lv = self._io.read_bytes(1)
        self._raw_max_lv = KaitaiStream.process_xor_many(self._raw__raw_max_lv, b"\x24")
        io = KaitaiStream(BytesIO(self._raw_max_lv))
        self.max_lv = Encrypted(u"xoru1", io)
        self._raw__raw_unknown2 = self._io.read_bytes(1)
        self._raw_unknown2 = KaitaiStream.process_xor_many(self._raw__raw_unknown2, b"\x19")
        io = KaitaiStream(BytesIO(self._raw_unknown2))
        self.unknown2 = Encrypted(u"xoru1", io)
        self._raw__raw_unknown3 = self._io.read_bytes(1)
        self._raw_unknown3 = KaitaiStream.process_xor_many(self._raw__raw_unknown3, b"\xBD")
        io = KaitaiStream(BytesIO(self._raw_unknown3))
        self.unknown3 = Encrypted(u"xoru1", io)
        self.padding = self._io.read_bytes(3)
        self.id_tag2 = CryptString(u"ID", self._io)
        self.next_seal = CryptString(u"ID", self._io)
        self.prev_seal = CryptString(u"ID", self._io)
        self._raw__raw_ss_coin = self._io.read_bytes(2)
        self._raw_ss_coin = KaitaiStream.process_xor_many(self._raw__raw_ss_coin, b"\x40\xC5")
        io = KaitaiStream(BytesIO(self._raw_ss_coin))
        self.ss_coin = Encrypted(u"xoru2", io)
        self._raw__raw_ss_badge_type = self._io.read_bytes(2)
        self._raw_ss_badge_type = KaitaiStream.process_xor_many(self._raw__raw_ss_badge_type, b"\x0F\xD5")
        io = KaitaiStream(BytesIO(self._raw_ss_badge_type))
        self.ss_badge_type = BadgeColor(io)
        self._raw__raw_ss_badge = self._io.read_bytes(2)
        self._raw_ss_badge = KaitaiStream.process_xor_many(self._raw__raw_ss_badge, b"\xEC\x8C")
        io = KaitaiStream(BytesIO(self._raw_ss_badge))
        self.ss_badge = Encrypted(u"xoru2", io)
        self._raw__raw_ss_great_badge = self._io.read_bytes(2)
        self._raw_ss_great_badge = KaitaiStream.process_xor_many(self._raw__raw_ss_great_badge, b"\xFF\xCC")
        io = KaitaiStream(BytesIO(self._raw_ss_great_badge))
        self.ss_great_badge = Encrypted(u"xoru2", io)


