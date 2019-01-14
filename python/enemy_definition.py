# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from stats_tuple import StatsTuple
from xorb1 import Xorb1
from encrypted import Encrypted
from magic_element import MagicElement
from move_index import MoveIndex
from weapon_index import WeaponIndex
from crypt_string import CryptString
class EnemyDefinition(KaitaiStruct):
    """The files at `Common/SRPG/Enemy/` define data for enemy-only units. This
    means enemies have base stats and GPs too.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Enemy_definitions
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.id_tag = CryptString(u"ID", self._io)
        self.roman = CryptString(u"ID", self._io)
        self.face_name = CryptString(u"ID", self._io)
        self.face_name_2 = CryptString(u"ID", self._io)
        self.top_weapon = CryptString(u"ID", self._io)
        self._raw__raw_timestamp = self._io.read_bytes(8)
        self._raw_timestamp = KaitaiStream.process_xor_many(self._raw__raw_timestamp, b"\x9B\x48\xB6\xE9\x42\xE7\xC1\xBD")
        io = KaitaiStream(BytesIO(self._raw_timestamp))
        self.timestamp = Encrypted(u"xors8", io)
        self._raw__raw_id_num = self._io.read_bytes(4)
        self._raw_id_num = KaitaiStream.process_xor_many(self._raw__raw_id_num, b"\xD4\x41\x2F\x42")
        io = KaitaiStream(BytesIO(self._raw_id_num))
        self.id_num = Encrypted(u"xoru4", io)
        self._raw__raw_weapon_type = self._io.read_bytes(1)
        self._raw_weapon_type = KaitaiStream.process_xor_many(self._raw__raw_weapon_type, b"\xE4")
        io = KaitaiStream(BytesIO(self._raw_weapon_type))
        self.weapon_type = WeaponIndex(io)
        self._raw__raw_tome_class = self._io.read_bytes(1)
        self._raw_tome_class = KaitaiStream.process_xor_many(self._raw__raw_tome_class, b"\x81")
        io = KaitaiStream(BytesIO(self._raw_tome_class))
        self.tome_class = MagicElement(io)
        self._raw__raw_move_type = self._io.read_bytes(1)
        self._raw_move_type = KaitaiStream.process_xor_many(self._raw__raw_move_type, b"\x0D")
        io = KaitaiStream(BytesIO(self._raw_move_type))
        self.move_type = MoveIndex(io)
        self._raw__raw_unknown1 = self._io.read_bytes(1)
        self._raw_unknown1 = KaitaiStream.process_xor_many(self._raw__raw_unknown1, b"\xC5")
        io = KaitaiStream(BytesIO(self._raw_unknown1))
        self.unknown1 = Xorb1(io)
        self._raw__raw_is_boss = self._io.read_bytes(1)
        self._raw_is_boss = KaitaiStream.process_xor_many(self._raw__raw_is_boss, b"\x6A")
        io = KaitaiStream(BytesIO(self._raw_is_boss))
        self.is_boss = Xorb1(io)
        self.padding = self._io.read_bytes(7)
        self.base_stats = StatsTuple(self._io)
        self.growth_rates = StatsTuple(self._io)


