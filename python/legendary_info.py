# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from stats_tuple import StatsTuple
from legendary_element import LegendaryElement
class LegendaryInfo(KaitaiStruct):
    """The struct that defines the element and ally boosts of a Legendary Hero.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes#legendary_info
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.bonus_effect = StatsTuple(self._io)
        self._raw__raw_element = self._io.read_bytes(1)
        self._raw_element = KaitaiStream.process_xor_many(self._raw__raw_element, b"\x05")
        io = KaitaiStream(BytesIO(self._raw_element))
        self.element = LegendaryElement(io)
        self.padding = self._io.read_bytes(7)


