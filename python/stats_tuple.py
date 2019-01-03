# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from xors2 import Xors2
class StatsTuple(KaitaiStruct):
    """A tuple representing the five stat values. The meaning of the tuple depends
    on the context.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#stats_tuple
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self._raw__raw_hp = self._io.read_bytes(2)
        self._raw_hp = KaitaiStream.process_xor_many(self._raw__raw_hp, b"\x32\xD6")
        io = KaitaiStream(BytesIO(self._raw_hp))
        self.hp = Xors2(io)
        self._raw__raw_attack = self._io.read_bytes(2)
        self._raw_attack = KaitaiStream.process_xor_many(self._raw__raw_attack, b"\xA0\x14")
        io = KaitaiStream(BytesIO(self._raw_attack))
        self.attack = Xors2(io)
        self._raw__raw_speed = self._io.read_bytes(2)
        self._raw_speed = KaitaiStream.process_xor_many(self._raw__raw_speed, b"\x5E\xA5")
        io = KaitaiStream(BytesIO(self._raw_speed))
        self.speed = Xors2(io)
        self._raw__raw_defense = self._io.read_bytes(2)
        self._raw_defense = KaitaiStream.process_xor_many(self._raw__raw_defense, b"\x66\x85")
        io = KaitaiStream(BytesIO(self._raw_defense))
        self.defense = Xors2(io)
        self._raw__raw_resistance = self._io.read_bytes(2)
        self._raw_resistance = KaitaiStream.process_xor_many(self._raw__raw_resistance, b"\xE5\xAE")
        io = KaitaiStream(BytesIO(self._raw_resistance))
        self.resistance = Xors2(io)
        self.unknown1 = self._io.read_s2le()
        self.unknown2 = self._io.read_s2le()
        self.unknown3 = self._io.read_s2le()


