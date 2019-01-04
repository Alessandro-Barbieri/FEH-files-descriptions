# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from decrypt_string import DecryptString


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from file_ptr import FilePtr
class CryptString(KaitaiStruct):
    """Null-terminated UTF-8 string of unspecified length. The XOR type parameter is
    used to show the XOR cipher used by the string. Because these strings are
    variable-length in nature, the cipher is repeated end-to-end for longer
    strings, and data bytes that match the respective cipher bytes are not XOR'ed
    in order to preserve the string length of the encrypted buffer.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#crypt_string.3CXOR.3E
    """
    def __init__(self, cipher, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self.cipher = cipher
        self._read()

    def _read(self):
        self.crypt_string_ptr = FilePtr(self._io)

    class CryptStringBuffer(KaitaiStruct):
        def __init__(self, key, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self.key = key
            self._read()

        def _read(self):
            self._raw__raw_buffer = self._io.read_bytes_term(0, False, True, True)
            _process = DecryptString(self.key)
            self._raw_buffer = _process.decode(self._raw__raw_buffer)
            io = KaitaiStream(BytesIO(self._raw_buffer))
            self.buffer = self._root.String(io, self, self._root)
            self.padding = self._io.read_bytes(((8 - self._io.pos()) % 8))


    class String(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = (self._io.read_bytes_full()).decode(u"UTF-8")


    @property
    def crypt_string(self):
        if hasattr(self, '_m_crypt_string'):
            return self._m_crypt_string if hasattr(self, '_m_crypt_string') else None

        if self.crypt_string_ptr.offset != 0:
            _pos = self._io.pos()
            self._io.seek((self.crypt_string_ptr.offset + 32))
            _on = self.cipher
            if _on == u"ID":
                self._m_crypt_string = self._root.CryptStringBuffer(b"\x81\x00\x80\xA4\x5A\x16\x6F\x78\x57\x81\x2D\xF7\xFC\x66\x0F\x27\x75\x35\xB4\x34\x10\xEE\xA2\xDB\xCC\xE3\x35\x99\x43\x48\xD2\xBB\x93\xC1", self._io, self, self._root)
            elif _on == u"NONE":
                self._m_crypt_string = self._root.CryptStringBuffer(b"\x00", self._io, self, self._root)
            self._io.seek(_pos)

        return self._m_crypt_string if hasattr(self, '_m_crypt_string') else None


