# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from crypt_string import CryptString
from stats_tuple import StatsTuple
from xorb1 import Xorb1
from encrypted import Encrypted
from map_position import MapPosition
class UnitData(KaitaiStruct):
    """Definition of a single unit placed on the map.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#unit_data
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.id_tag = CryptString(u"ID", self._io)
        self.skills = [None] * (7)
        for i in range(7):
            self.skills[i] = CryptString(u"ID", self._io)

        self.accessory = CryptString(u"ID", self._io)
        self.pos = MapPosition(self._io)
        self._raw__raw_rarity = self._io.read_bytes(1)
        self._raw_rarity = KaitaiStream.process_xor_many(self._raw__raw_rarity, b"\x61")
        io = KaitaiStream(BytesIO(self._raw_rarity))
        self.rarity = Encrypted(u"xoru1", io)
        self._raw__raw_lv = self._io.read_bytes(1)
        self._raw_lv = KaitaiStream.process_xor_many(self._raw__raw_lv, b"\x2A")
        io = KaitaiStream(BytesIO(self._raw_lv))
        self.lv = Encrypted(u"xoru1", io)
        self._raw__raw_cooldown_count = self._io.read_bytes(1)
        self._raw_cooldown_count = KaitaiStream.process_xor_many(self._raw__raw_cooldown_count, b"\x1E")
        io = KaitaiStream(BytesIO(self._raw_cooldown_count))
        self.cooldown_count = Encrypted(u"xors1", io)
        self.unknown1 = self._io.read_u1()
        self.stats = StatsTuple(self._io)
        self._raw__raw_start_turn = self._io.read_bytes(1)
        self._raw_start_turn = KaitaiStream.process_xor_many(self._raw__raw_start_turn, b"\xCF")
        io = KaitaiStream(BytesIO(self._raw_start_turn))
        self.start_turn = Encrypted(u"xors1", io)
        self._raw__raw_movement_group = self._io.read_bytes(1)
        self._raw_movement_group = KaitaiStream.process_xor_many(self._raw__raw_movement_group, b"\xF4")
        io = KaitaiStream(BytesIO(self._raw_movement_group))
        self.movement_group = Encrypted(u"xors1", io)
        self._raw__raw_movement_delay = self._io.read_bytes(1)
        self._raw_movement_delay = KaitaiStream.process_xor_many(self._raw__raw_movement_delay, b"\x95")
        io = KaitaiStream(BytesIO(self._raw_movement_delay))
        self.movement_delay = Encrypted(u"xors1", io)
        self._raw__raw_break_terrain = self._io.read_bytes(1)
        self._raw_break_terrain = KaitaiStream.process_xor_many(self._raw__raw_break_terrain, b"\x71")
        io = KaitaiStream(BytesIO(self._raw_break_terrain))
        self.break_terrain = Xorb1(io)
        self._raw__raw_tether = self._io.read_bytes(1)
        self._raw_tether = KaitaiStream.process_xor_many(self._raw__raw_tether, b"\xB8")
        io = KaitaiStream(BytesIO(self._raw_tether))
        self.tether = Xorb1(io)
        self._raw__raw_true_lv = self._io.read_bytes(1)
        self._raw_true_lv = KaitaiStream.process_xor_many(self._raw__raw_true_lv, b"\x85")
        io = KaitaiStream(BytesIO(self._raw_true_lv))
        self.true_lv = Encrypted(u"xoru1", io)
        self._raw__raw_is_enemy = self._io.read_bytes(1)
        self._raw_is_enemy = KaitaiStream.process_xor_many(self._raw__raw_is_enemy, b"\xD0")
        io = KaitaiStream(BytesIO(self._raw_is_enemy))
        self.is_enemy = Xorb1(io)
        self.padding = self._io.read_bytes(1)
        self.spawn_check = CryptString(u"ID", self._io)
        self._raw__raw_spawn_count = self._io.read_bytes(1)
        self._raw_spawn_count = KaitaiStream.process_xor_many(self._raw__raw_spawn_count, b"\x0A")
        io = KaitaiStream(BytesIO(self._raw_spawn_count))
        self.spawn_count = Encrypted(u"xors1", io)
        self._raw__raw_spawn_turns = self._io.read_bytes(1)
        self._raw_spawn_turns = KaitaiStream.process_xor_many(self._raw__raw_spawn_turns, b"\x0A")
        io = KaitaiStream(BytesIO(self._raw_spawn_turns))
        self.spawn_turns = Encrypted(u"xors1", io)
        self._raw__raw_spawn_target_remain = self._io.read_bytes(1)
        self._raw_spawn_target_remain = KaitaiStream.process_xor_many(self._raw__raw_spawn_target_remain, b"\x2D")
        io = KaitaiStream(BytesIO(self._raw_spawn_target_remain))
        self.spawn_target_remain = Encrypted(u"xors1", io)
        self._raw__raw_spawn_target_kills = self._io.read_bytes(1)
        self._raw_spawn_target_kills = KaitaiStream.process_xor_many(self._raw__raw_spawn_target_kills, b"\x5B")
        io = KaitaiStream(BytesIO(self._raw_spawn_target_kills))
        self.spawn_target_kills = Encrypted(u"xors1", io)


