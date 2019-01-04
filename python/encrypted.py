# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Encrypted(KaitaiStruct):
    def __init__(self, typ, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.typ = typ
        self._read()

    def _read(self):
        _on = self.typ
        if _on == u"xors4":
            self.data = self._io.read_s4le()
        elif _on == u"xors2":
            self.data = self._io.read_s2le()
        elif _on == u"xoru4":
            self.data = self._io.read_u4le()
        elif _on == u"xoru1":
            self.data = self._io.read_u1()
        elif _on == u"xorb1":
            self.data = self._io.read_bits_int(1) != 0
        elif _on == u"xoru2":
            self.data = self._io.read_u2le()
        elif _on == u"xors1":
            self.data = self._io.read_s1()
        elif _on == u"xoru8":
            self.data = self._io.read_u8le()
        elif _on == u"xors8":
            self.data = self._io.read_s8le()


