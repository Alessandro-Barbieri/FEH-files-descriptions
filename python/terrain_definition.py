# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from encrypted import Encrypted
class TerrainDefinition(KaitaiStruct):
    """The file `Common/SRPG/Terrain.bin` defines all 31 terrains used in the game.
    These only handle the gameplay aspects; animation background is defined
    elsewhere. Movement costs are defined in `Common/SRPG/Move.bin.lz`.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#terrain_definition
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw__raw_index = self._io.read_bytes(4)
        self._raw_index = KaitaiStream.process_xor_many(self._raw__raw_index, b"\xAB\xA1\xE0\xDA")
        io = KaitaiStream(BytesIO(self._raw_index))
        self.index = Encrypted(u"xoru4", io)
        self._raw__raw_base_terrain = self._io.read_bytes(4)
        self._raw_base_terrain = KaitaiStream.process_xor_many(self._raw__raw_base_terrain, b"\xD2\x7D\xD0\x6F")
        io = KaitaiStream(BytesIO(self._raw_base_terrain))
        self.base_terrain = Encrypted(u"xors4", io)
        self._raw__raw_foe_base_terrain = self._io.read_bytes(4)
        self._raw_foe_base_terrain = KaitaiStream.process_xor_many(self._raw__raw_foe_base_terrain, b"\xD2\x7D\xD0\x6F")
        io = KaitaiStream(BytesIO(self._raw_foe_base_terrain))
        self.foe_base_terrain = Encrypted(u"xors4", io)
        self._raw__raw_side = self._io.read_bytes(1)
        self._raw_side = KaitaiStream.process_xor_many(self._raw__raw_side, b"\x21")
        io = KaitaiStream(BytesIO(self._raw_side))
        self.side = Encrypted(u"xors1", io)
        self._raw__raw_terrain_group = self._io.read_bytes(1)
        self._raw_terrain_group = KaitaiStream.process_xor_many(self._raw__raw_terrain_group, b"\xCB")
        io = KaitaiStream(BytesIO(self._raw_terrain_group))
        self.terrain_group = Encrypted(u"xoru1", io)
        self._raw__raw_inaccessible = self._io.read_bytes(1)
        self._raw_inaccessible = KaitaiStream.process_xor_many(self._raw__raw_inaccessible, b"\x16")
        io = KaitaiStream(BytesIO(self._raw_inaccessible))
        self.inaccessible = Encrypted(u"xorb1", io)
        self._raw__raw_hp = self._io.read_bytes(1)
        self._raw_hp = KaitaiStream.process_xor_many(self._raw__raw_hp, b"\xBA")
        io = KaitaiStream(BytesIO(self._raw_hp))
        self.hp = Encrypted(u"xoru1", io)
        self._raw__raw_is_wall = self._io.read_bytes(1)
        self._raw_is_wall = KaitaiStream.process_xor_many(self._raw__raw_is_wall, b"\xA8")
        io = KaitaiStream(BytesIO(self._raw_is_wall))
        self.is_wall = Encrypted(u"xorb1", io)
        self._raw__raw_is_liquid = self._io.read_bytes(1)
        self._raw_is_liquid = KaitaiStream.process_xor_many(self._raw__raw_is_liquid, b"\x7C")
        io = KaitaiStream(BytesIO(self._raw_is_liquid))
        self.is_liquid = Encrypted(u"xorb1", io)
        self._raw__raw_is_bridge = self._io.read_bytes(1)
        self._raw_is_bridge = KaitaiStream.process_xor_many(self._raw__raw_is_bridge, b"\x08")
        io = KaitaiStream(BytesIO(self._raw_is_bridge))
        self.is_bridge = Encrypted(u"xorb1", io)
        self._raw__raw_is_trench = self._io.read_bytes(1)
        self._raw_is_trench = KaitaiStream.process_xor_many(self._raw__raw_is_trench, b"\x30")
        io = KaitaiStream(BytesIO(self._raw_is_trench))
        self.is_trench = Encrypted(u"xorb1", io)
        self._raw__raw_is_fortress = self._io.read_bytes(1)
        self._raw_is_fortress = KaitaiStream.process_xor_many(self._raw__raw_is_fortress, b"\xDA")
        io = KaitaiStream(BytesIO(self._raw_is_fortress))
        self.is_fortress = Encrypted(u"xorb1", io)
        self._raw__raw_is_rd_terrain = self._io.read_bytes(1)
        self._raw_is_rd_terrain = KaitaiStream.process_xor_many(self._raw__raw_is_rd_terrain, b"\xCD")
        io = KaitaiStream(BytesIO(self._raw_is_rd_terrain))
        self.is_rd_terrain = Encrypted(u"xorb1", io)
        self._raw__raw_mit_mod = self._io.read_bytes(1)
        self._raw_mit_mod = KaitaiStream.process_xor_many(self._raw__raw_mit_mod, b"\xAA")
        io = KaitaiStream(BytesIO(self._raw_mit_mod))
        self.mit_mod = Encrypted(u"xoru1", io)
        self._raw__raw_regen_hp = self._io.read_bytes(1)
        self._raw_regen_hp = KaitaiStream.process_xor_many(self._raw__raw_regen_hp, b"\x7D")
        io = KaitaiStream(BytesIO(self._raw_regen_hp))
        self.regen_hp = Encrypted(u"xoru1", io)


