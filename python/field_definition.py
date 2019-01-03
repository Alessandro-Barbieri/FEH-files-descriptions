# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from xoru4 import Xoru4
from xoru1 import Xoru1
from crypt_string import CryptString
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
        self.width = Xoru4(io)
        self._raw__raw_height = self._io.read_bytes(4)
        self._raw_height = KaitaiStream.process_xor_many(self._raw__raw_height, b"\xD5\x12\xAA\x2B")
        io = KaitaiStream(BytesIO(self._raw_height))
        self.height = Xoru4(io)
        self._raw__raw_base_terrain = self._io.read_bytes(1)
        self._raw_base_terrain = KaitaiStream.process_xor_many(self._raw__raw_base_terrain, b"\x41")
        io = KaitaiStream(BytesIO(self._raw_base_terrain))
        self.base_terrain = Xoru1(io)
        self.padding = self._io.read_bytes(7)
        self._raw_terrain = self._io.read_bytes((self.height.data * self.width.data))
        self.terrain = KaitaiStream.process_xor_many(self._raw_terrain, b"\xA1")


