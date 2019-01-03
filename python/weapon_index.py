# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class WeaponIndex(KaitaiStruct):
    """
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Enumeration_types#weapon_index
    """

    class WeaponIndexEnum(Enum):
        sword = 0
        lance = 1
        axe = 2
        red_bow = 3
        blue_bow = 4
        green_bow = 5
        colorless_bow = 6
        red_dagger = 7
        blue_dagger = 8
        green_dagger = 9
        colorless_dagger = 10
        red_tome = 11
        blue_tome = 12
        green_tome = 13
        staff = 14
        red_breath = 15
        blue_breath = 16
        green_breath = 17
        colorless_breath = 18
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.index = self._root.WeaponIndexEnum(self._io.read_u1())


