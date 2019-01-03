# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class FilePtr(KaitaiStruct):
    """Generic absolute file offset pointer. The actual pointed-to file offset is the
    value of the pointer + `0x20`, since the archives have a 32-byte header. As a
    special case, `0` points to nowhere, and is used to indicate absence of
    pointed-to data (much like the real nullptr).
    File offsets inside the data section of each archive are replaced with
    absolute pointers to raw memory when the archives are loaded into memory. File
    pointers on the relocatable pointer list (`hsdarc_buffer::ptr_list`) are never
    null; if their value is `0`, they point to the pointer at `$20`.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/User:HertzDevil/Reverse-engineering_notes/Basic_data_types#file_ptr_t.3CT.3E
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.offset = self._io.read_u8le()


