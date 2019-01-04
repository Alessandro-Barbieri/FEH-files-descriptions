# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from hero_definition import HeroDefinition
from xoru8 import Xoru8
from terrain_definition import TerrainDefinition
from enemy_definition import EnemyDefinition
from file_ptr import FilePtr
from weapon_class_definition import WeaponClassDefinition
class ObjList(KaitaiStruct):
    """Generic object list. A variety of files consist of a single list, pointed
    from the first relocatable pointer (always to `$20`).
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#obj_list.3CT.2C_xor.3E
    """
    def __init__(self, type, key, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.type = type
        self.key = key
        self._read()

    def _read(self):
        self.list_ptr = FilePtr(self._io)
        self._raw__raw_size = self._io.read_bytes(8)
        self._raw_size = KaitaiStream.process_xor_many(self._raw__raw_size, self.key)
        io = KaitaiStream(BytesIO(self._raw_size))
        self.size = Xoru8(io)

    @property
    def object_list(self):
        """Pointer to the array of objects. Usually `0x10` (points to `$30`)."""
        if hasattr(self, '_m_object_list'):
            return self._m_object_list if hasattr(self, '_m_object_list') else None

        if self.list_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.list_ptr.offset + 32))
            self._m_object_list = [None] * (self.size.data)
            for i in range(self.size.data):
                _on = self.type
                if _on == u"enemy_definition":
                    self._m_object_list[i] = EnemyDefinition(self._io)
                elif _on == u"hero_definition":
                    self._m_object_list[i] = HeroDefinition(self._io)
                elif _on == u"terrain_definition":
                    self._m_object_list[i] = TerrainDefinition(self._io)
                elif _on == u"weapon_class_definition":
                    self._m_object_list[i] = WeaponClassDefinition(self._io)

            self._io.seek(_pos)

        return self._m_object_list if hasattr(self, '_m_object_list') else None


