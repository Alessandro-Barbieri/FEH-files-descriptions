# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from xoru2 import Xoru2
class MapPosition(KaitaiStruct):
    """Coordinates representing a point on a map.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#map_position
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw__raw_x = self._io.read_bytes(2)
        self._raw_x = KaitaiStream.process_xor_many(self._raw__raw_x, b"\x32\xB3")
        io = KaitaiStream(BytesIO(self._raw_x))
        self.x = Xoru2(io)
        self._raw__raw_y = self._io.read_bytes(2)
        self._raw_y = KaitaiStream.process_xor_many(self._raw__raw_y, b"\xB2\x28")
        io = KaitaiStream(BytesIO(self._raw_y))
        self.y = Xoru2(io)
        self.padding = self._io.read_bytes(4)


