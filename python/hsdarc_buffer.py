# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from file_ptr import FilePtr
from map_definition import MapDefinition
from file_tag import FileTag
from obj_list import ObjList
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
        self.magic = self._io.ensure_fixed_contents(b"\x00\x00\x00\x00\x00\x00\x00\x00")
        _on = self.type
        if _on == u"weapon":
            self.data = ObjList(u"weapon_class_definition", b"\x4F\x4C\x66\x6D\xEB\x17\xBA\xA7", self._io)
        elif _on == u"enemy":
            self.data = ObjList(u"enemy_definition", b"\x5C\x34\xC5\x9C\x11\x95\xCA\x62", self._io)
        elif _on == u"terrain":
            self.data = ObjList(u"terrain_definition", b"\x3C\x93\x7C\xA8\xA3\x2D\x25\x22", self._io)
        elif _on == u"map":
            self.data = MapDefinition(self._io)
        elif _on == u"person":
            self.data = ObjList(u"hero_definition", b"\xE1\xB9\x3A\x3C\x79\xAB\x51\xDE", self._io)

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


