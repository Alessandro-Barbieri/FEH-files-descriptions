# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from file_ptr import FilePtr
from crypt_string import CryptString
class FieldGfxDefinition(KaitaiStruct):
    """The files at `Common/SRPG/Field/` define the graphical assets maps use.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#field_gfx_definition
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.map_id = CryptString(u"ID", self._io)
        self.wall_ptr = FilePtr(self._io)
        self.backdrop_ptr = FilePtr(self._io)
        self.overlay1_ptr = FilePtr(self._io)
        self.overlay2_ptr = FilePtr(self._io)
        self.anim = CryptString(u"NONE", self._io)

    class GfxResource(KaitaiStruct):
        """A single graphical asset.
        
        .. seealso::
           Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#gfx_resource_t
        """
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.kind = CryptString(u"ID", self._io)
            self.filename = CryptString(u"NONE", self._io)


    @property
    def wall(self):
        """The sprites for wall terrains. Walls are only drawn if at least one wall
        tile is breakable; otherwise, wall graphics are directly embedded in the
        map image.
        """
        if hasattr(self, '_m_wall'):
            return self._m_wall if hasattr(self, '_m_wall') else None

        if self.wall_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.wall_ptr.offset + 32))
            self._m_wall = self._root.GfxResource(self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_wall if hasattr(self, '_m_wall') else None

    @property
    def backdrop(self):
        """The sprite for the map's backdrop."""
        if hasattr(self, '_m_backdrop'):
            return self._m_backdrop if hasattr(self, '_m_backdrop') else None

        if self.backdrop_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.backdrop_ptr.offset + 32))
            self._m_backdrop = self._root.GfxResource(self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_backdrop if hasattr(self, '_m_backdrop') else None

    @property
    def overlay1(self):
        """The sprites for the map's overlays. Up to 2 can be defined."""
        if hasattr(self, '_m_overlay1'):
            return self._m_overlay1 if hasattr(self, '_m_overlay1') else None

        if self.overlay1_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.overlay1_ptr.offset + 32))
            self._m_overlay1 = self._root.GfxResource(self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_overlay1 if hasattr(self, '_m_overlay1') else None

    @property
    def overlay2(self):
        """The sprites for the map's overlays. Up to 2 can be defined."""
        if hasattr(self, '_m_overlay2'):
            return self._m_overlay2 if hasattr(self, '_m_overlay2') else None

        if self.overlay2_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.overlay2_ptr.offset + 32))
            self._m_overlay2 = self._root.GfxResource(self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_overlay2 if hasattr(self, '_m_overlay2') else None


