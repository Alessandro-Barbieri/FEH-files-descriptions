# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from xors8 import Xors8
from magic_element import MagicElement
from xoru4 import Xoru4
from file_ptr import FilePtr
from xorb1 import Xorb1
from xoru1 import Xoru1
from weapon_index import WeaponIndex
from move_index import MoveIndex
from crypt_string import CryptString
from stats_tuple import StatsTuple
from legendary_info import LegendaryInfo
class HeroDefinition(KaitaiStruct):
    """Complete definition of a hero.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#hero_definition
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
        self.legendary_ptr = FilePtr(self._io)
        self._raw__raw_timestamp = self._io.read_bytes(8)
        self._raw_timestamp = KaitaiStream.process_xor_many(self._raw__raw_timestamp, b"\x9B\x48\xB6\xE9\x42\xE7\xC1\xBD")
        io = KaitaiStream(BytesIO(self._raw_timestamp))
        self.timestamp = Xors8(io)
        self._raw__raw_id_num = self._io.read_bytes(4)
        self._raw_id_num = KaitaiStream.process_xor_many(self._raw__raw_id_num, b"\x18\x4E\x6E\x5F")
        io = KaitaiStream(BytesIO(self._raw_id_num))
        self.id_num = Xoru4(io)
        self._raw__raw_sort_value = self._io.read_bytes(4)
        self._raw_sort_value = KaitaiStream.process_xor_many(self._raw__raw_sort_value, b"\x9B\x34\x80\x2A")
        io = KaitaiStream(BytesIO(self._raw_sort_value))
        self.sort_value = Xoru4(io)
        self._raw__raw_weapon_type = self._io.read_bytes(1)
        self._raw_weapon_type = KaitaiStream.process_xor_many(self._raw__raw_weapon_type, b"\x06")
        io = KaitaiStream(BytesIO(self._raw_weapon_type))
        self.weapon_type = WeaponIndex(io)
        self._raw__raw_tome_class = self._io.read_bytes(1)
        self._raw_tome_class = KaitaiStream.process_xor_many(self._raw__raw_tome_class, b"\x35")
        io = KaitaiStream(BytesIO(self._raw_tome_class))
        self.tome_class = MagicElement(io)
        self._raw__raw_move_type = self._io.read_bytes(1)
        self._raw_move_type = KaitaiStream.process_xor_many(self._raw__raw_move_type, b"\x2A")
        io = KaitaiStream(BytesIO(self._raw_move_type))
        self.move_type = MoveIndex(io)
        self._raw__raw_series = self._io.read_bytes(1)
        self._raw_series = KaitaiStream.process_xor_many(self._raw__raw_series, b"\x43")
        io = KaitaiStream(BytesIO(self._raw_series))
        self.series = Xoru1(io)
        self._raw__raw_regular_hero = self._io.read_bytes(1)
        self._raw_regular_hero = KaitaiStream.process_xor_many(self._raw__raw_regular_hero, b"\xA1")
        io = KaitaiStream(BytesIO(self._raw_regular_hero))
        self.regular_hero = Xorb1(io)
        self._raw__raw_permanent_hero = self._io.read_bytes(1)
        self._raw_permanent_hero = KaitaiStream.process_xor_many(self._raw__raw_permanent_hero, b"\xC7")
        io = KaitaiStream(BytesIO(self._raw_permanent_hero))
        self.permanent_hero = Xorb1(io)
        self._raw__raw_base_vector_id = self._io.read_bytes(1)
        self._raw_base_vector_id = KaitaiStream.process_xor_many(self._raw__raw_base_vector_id, b"\x3D")
        io = KaitaiStream(BytesIO(self._raw_base_vector_id))
        self.base_vector_id = Xoru1(io)
        self._raw__raw_refresher = self._io.read_bytes(1)
        self._raw_refresher = KaitaiStream.process_xor_many(self._raw__raw_refresher, b"\xFF")
        io = KaitaiStream(BytesIO(self._raw_refresher))
        self.refresher = Xorb1(io)
        self.unknown2 = self._io.read_u1()
        self.padding = self._io.read_bytes(7)
        self.base_stats = StatsTuple(self._io)
        self.growth_rates = StatsTuple(self._io)
        self.max_stats = StatsTuple(self._io)
        self.skills = [None] * ((5 * 14))
        for i in range((5 * 14)):
            self.skills[i] = CryptString(u"ID", self._io)


    @property
    def legendary(self):
        if hasattr(self, '_m_legendary'):
            return self._m_legendary if hasattr(self, '_m_legendary') else None

        if self.legendary_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.legendary_ptr.offset + 32))
            self._m_legendary = [None] * (1)
            for i in range(1):
                self._m_legendary[i] = LegendaryInfo(self._io)

            self._io.seek(_pos)

        return self._m_legendary if hasattr(self, '_m_legendary') else None


