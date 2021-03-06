# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from file_ptr import FilePtr
from xorb1 import Xorb1
from encrypted import Encrypted
from map_position import MapPosition
from unit_data import UnitData
from crypt_string import CryptString
class MapDefinition(KaitaiStruct):
    """Top-level definition of a map. One instance appears in each map file at `$20`.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#map_definition
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.unknown1 = self._io.read_u4le()
        self._raw__raw_highest_score = self._io.read_bytes(4)
        self._raw_highest_score = KaitaiStream.process_xor_many(self._raw__raw_highest_score, b"\xB1\x50\xE2\xA9")
        io = KaitaiStream(BytesIO(self._raw_highest_score))
        self.highest_score = Encrypted(u"xoru4", io)
        self.field_ptr = FilePtr(self._io)
        self.player_pos_ptr = FilePtr(self._io)
        self.units_ptr = FilePtr(self._io)
        self._raw__raw_player_count = self._io.read_bytes(4)
        self._raw_player_count = KaitaiStream.process_xor_many(self._raw__raw_player_count, b"\x9A\xC7\x63\x9D")
        io = KaitaiStream(BytesIO(self._raw_player_count))
        self.player_count = Encrypted(u"xoru4", io)
        self._raw__raw_unit_count = self._io.read_bytes(4)
        self._raw_unit_count = KaitaiStream.process_xor_many(self._raw__raw_unit_count, b"\xEE\x10\x67\xAC")
        io = KaitaiStream(BytesIO(self._raw_unit_count))
        self.unit_count = Encrypted(u"xoru4", io)
        self._raw__raw_turns_to_win = self._io.read_bytes(1)
        self._raw_turns_to_win = KaitaiStream.process_xor_many(self._raw__raw_turns_to_win, b"\xFD")
        io = KaitaiStream(BytesIO(self._raw_turns_to_win))
        self.turns_to_win = Encrypted(u"xoru1", io)
        self._raw__raw_last_enemy_phase = self._io.read_bytes(1)
        self._raw_last_enemy_phase = KaitaiStream.process_xor_many(self._raw__raw_last_enemy_phase, b"\xC7")
        io = KaitaiStream(BytesIO(self._raw_last_enemy_phase))
        self.last_enemy_phase = Xorb1(io)
        self._raw__raw_turns_to_defend = self._io.read_bytes(1)
        self._raw_turns_to_defend = KaitaiStream.process_xor_many(self._raw__raw_turns_to_defend, b"\xEC")
        io = KaitaiStream(BytesIO(self._raw_turns_to_defend))
        self.turns_to_defend = Encrypted(u"xoru1", io)

    class FieldDefinition(KaitaiStruct):
        """Terrain data of a map. Graphical information is stored outside map files.
        
        .. seealso::
           Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#field_definition
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.id = CryptString(u"ID", self._io)
            self._raw__raw_width = self._io.read_bytes(4)
            self._raw_width = KaitaiStream.process_xor_many(self._raw__raw_width, b"\x5F\xD7\x7C\x6B")
            io = KaitaiStream(BytesIO(self._raw_width))
            self.width = Encrypted(u"xoru4", io)
            self._raw__raw_height = self._io.read_bytes(4)
            self._raw_height = KaitaiStream.process_xor_many(self._raw__raw_height, b"\xD5\x12\xAA\x2B")
            io = KaitaiStream(BytesIO(self._raw_height))
            self.height = Encrypted(u"xoru4", io)
            self._raw__raw_base_terrain = self._io.read_bytes(1)
            self._raw_base_terrain = KaitaiStream.process_xor_many(self._raw__raw_base_terrain, b"\x41")
            io = KaitaiStream(BytesIO(self._raw_base_terrain))
            self.base_terrain = Encrypted(u"xoru1", io)
            self.padding = self._io.read_bytes(7)
            self._raw_terrain = self._io.read_bytes((self.height.data * self.width.data))
            self.terrain = KaitaiStream.process_xor_many(self._raw_terrain, b"\xA1")


    @property
    def field(self):
        """Terrain definition of this map."""
        if hasattr(self, '_m_field'):
            return self._m_field if hasattr(self, '_m_field') else None

        if self.field_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.field_ptr.offset + 32))
            self._m_field = self._root.FieldDefinition(self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_field if hasattr(self, '_m_field') else None

    @property
    def player_pos(self):
        """List of coordinates for the player's team, in the order they are placed.
        Each element is followed by 4 bytes of padding. For Tactics Drills maps
        this list is empty.
        """
        if hasattr(self, '_m_player_pos'):
            return self._m_player_pos if hasattr(self, '_m_player_pos') else None

        if self.player_pos_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.player_pos_ptr.offset + 32))
            self._m_player_pos = [None] * (self.player_count.data)
            for i in range(self.player_count.data):
                self._m_player_pos[i] = MapPosition(self._io)

            self._io.seek(_pos)

        return self._m_player_pos if hasattr(self, '_m_player_pos') else None

    @property
    def units(self):
        """List of units on the map, including all reinforcements."""
        if hasattr(self, '_m_units'):
            return self._m_units if hasattr(self, '_m_units') else None

        if self.units_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.units_ptr.offset + 32))
            self._m_units = [None] * (self.unit_count.data)
            for i in range(self.unit_count.data):
                self._m_units[i] = UnitData(self._io)

            self._io.seek(_pos)

        return self._m_units if hasattr(self, '_m_units') else None


