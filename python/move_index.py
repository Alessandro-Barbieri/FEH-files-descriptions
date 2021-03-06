# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class MoveIndex(KaitaiStruct):
    """
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Enumeration_types#move_index
    """

    class MoveIndexEnum(Enum):
        infantry = 0
        armored = 1
        cavalry = 2
        flying = 3
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.idx = self._root.MoveIndexEnum(self._io.read_u1())


