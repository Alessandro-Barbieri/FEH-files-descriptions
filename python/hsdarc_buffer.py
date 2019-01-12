# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from enemy_definition import EnemyDefinition
from map_definition import MapDefinition
from file_ptr import FilePtr
from weapon_class_definition import WeaponClassDefinition
from encrypted import Encrypted
from hero_definition import HeroDefinition
from skill_definition import SkillDefinition
from terrain_definition import TerrainDefinition
from field_gfx_definition import FieldGfxDefinition
from file_tag import FileTag
class HsdarcBuffer(KaitaiStruct):
    """The contents of an HSDArc archive.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#hsdarc_buffer
    """
    def __init__(self, type, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.type = type
        self._read()

    def _read(self):
        self.archive_size = self._io.read_u4le()
        self.ptr_list_offset = self._io.read_u4le()
        self.ptr_list_length = self._io.read_u4le()
        self.tag_list_length = self._io.read_u4le()
        self.unknown1 = self._io.read_u4le()
        self.unknown2 = self._io.read_u4le()
        self.magic_bytes = self._io.ensure_fixed_contents(b"\x00\x00\x00\x00\x00\x00\x00\x00")
        _on = self.type
        if _on == u"skill":
            self.data = self._root.ObjList(u"skill_definition", b"\xAD\xE9\xDE\x4A\x07\xC7\xEC\x7F", self._io, self, self._root)
        elif _on == u"weapon":
            self.data = self._root.ObjList(u"weapon_class_definition", b"\x4F\x4C\x66\x6D\xEB\x17\xBA\xA7", self._io, self, self._root)
        elif _on == u"enemy":
            self.data = self._root.ObjList(u"enemy_definition", b"\x5C\x34\xC5\x9C\x11\x95\xCA\x62", self._io, self, self._root)
        elif _on == u"terrain":
            self.data = self._root.ObjList(u"terrain_definition", b"\x3C\x93\x7C\xA8\xA3\x2D\x25\x22", self._io, self, self._root)
        elif _on == u"map":
            self.data = MapDefinition(self._io)
        elif _on == u"field":
            self.data = self._root.ObjList(u"field_gfx_definition", b"\x58\xBC\xDF\xCA\x3C\x08\x90\x1D", self._io, self, self._root)
        elif _on == u"person":
            self.data = self._root.ObjList(u"hero_definition", b"\xE1\xB9\x3A\x3C\x79\xAB\x51\xDE", self._io, self, self._root)

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
            self.size = Encrypted(u"xoru8", io)

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
                    if _on == u"field_gfx_definition":
                        self._m_object_list[i] = FieldGfxDefinition(self._io)
                    elif _on == u"weapon_class_definition":
                        self._m_object_list[i] = WeaponClassDefinition(self._io)
                    elif _on == u"skill_definition":
                        self._m_object_list[i] = SkillDefinition(self._io)
                    elif _on == u"hero_definition":
                        self._m_object_list[i] = HeroDefinition(self._io)
                    elif _on == u"enemy_definition":
                        self._m_object_list[i] = EnemyDefinition(self._io)
                    elif _on == u"terrain_definition":
                        self._m_object_list[i] = TerrainDefinition(self._io)

                self._io.seek(_pos)

            return self._m_object_list if hasattr(self, '_m_object_list') else None


    @property
    def ptr_list(self):
        """The relocatable pointer list. Each entry on this table points to another
        file offset pointer, which may point to anything depending on
        interpretation. While loading the archive into memory, pointers referred
        to by this table are converted into absolute memory pointers, by adding
        the address of hsdarc_buffer::data to their values; pointers on this list
        itself remain unaltered. (Note that this allows archive files to be
        restored from raw memory.)
        """
        if hasattr(self, '_m_ptr_list'):
            return self._m_ptr_list if hasattr(self, '_m_ptr_list') else None

        _pos = self._io.pos()
        self._io.seek((self.ptr_list_offset + 32))
        self._m_ptr_list = [None] * (self.ptr_list_length)
        for i in range(self.ptr_list_length):
            self._m_ptr_list[i] = FilePtr(self._io)

        self._io.seek(_pos)
        return self._m_ptr_list if hasattr(self, '_m_ptr_list') else None

    @property
    def tag_list(self):
        """A list of objects with tag strings associated to them.
        """
        if hasattr(self, '_m_tag_list'):
            return self._m_tag_list if hasattr(self, '_m_tag_list') else None

        _pos = self._io.pos()
        self._io.seek(((self.ptr_list_length + self.ptr_list_offset) + 32))
        self._m_tag_list = [None] * (self.tag_list_length)
        for i in range(self.tag_list_length):
            self._m_tag_list[i] = FileTag(self._io)

        self._io.seek(_pos)
        return self._m_tag_list if hasattr(self, '_m_tag_list') else None


