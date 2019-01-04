# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

from crypt_string import CryptString
from weapon_index import WeaponIndex
from encrypted import Encrypted
class WeaponClassDefinition(KaitaiStruct):
    """The file `assets/Common/SRPG/Weapon.bin` defines the weapon classes used by
    units. Weapon skills only indicate which weapon classes can equip them;
    common weapon attributes are defined in the weapon classes rather than the
    weapon skills.
    
    Only one of `is_staff`, `is_dagger`, and `is_breath` can be used by skills,
    in that order of precedence.
    
    .. seealso::
       Source - https://feheroes.gamepedia.com/index.php?title=User:HertzDevil/Reverse-engineering_notes#Weapon_class_definitions
    """

    class ColorEnum(Enum):
        colorless = 44
        red = 45
        blue = 46
        green = 47
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.id_tag = CryptString(u"ID", self._io)
        self.sprite_base = [None] * (2)
        for i in range(2):
            self.sprite_base[i] = CryptString(u"NONE", self._io)

        self.base_weapon = CryptString(u"ID", self._io)
        self._raw__raw_index = self._io.read_bytes(4)
        self._raw_index = KaitaiStream.process_xor_many(self._raw__raw_index, b"\x0C\x41\xD3\x90")
        io = KaitaiStream(BytesIO(self._raw_index))
        self.index = WeaponIndex(io)
        self.color = self._root.ColorEnum(self._io.read_u1())
        self._raw__raw_range = self._io.read_bytes(1)
        self._raw_range = KaitaiStream.process_xor_many(self._raw__raw_range, b"\x8B")
        io = KaitaiStream(BytesIO(self._raw_range))
        self.range = Encrypted(u"xoru1", io)
        self._raw__raw_unknown1 = self._io.read_bytes(1)
        self._raw_unknown1 = KaitaiStream.process_xor_many(self._raw__raw_unknown1, b"\xD0")
        io = KaitaiStream(BytesIO(self._raw_unknown1))
        self.unknown1 = Encrypted(u"xoru1", io)
        self._raw__raw_equip_group = self._io.read_bytes(1)
        self._raw_equip_group = KaitaiStream.process_xor_many(self._raw__raw_equip_group, b"\xB7")
        io = KaitaiStream(BytesIO(self._raw_equip_group))
        self.equip_group = Encrypted(u"xoru1", io)
        self._raw__raw_res_damage = self._io.read_bytes(1)
        self._raw_res_damage = KaitaiStream.process_xor_many(self._raw__raw_res_damage, b"\x07")
        io = KaitaiStream(BytesIO(self._raw_res_damage))
        self.res_damage = Encrypted(u"xorb1", io)
        self._raw__raw_is_staff = self._io.read_bytes(1)
        self._raw_is_staff = KaitaiStream.process_xor_many(self._raw__raw_is_staff, b"\x78")
        io = KaitaiStream(BytesIO(self._raw_is_staff))
        self.is_staff = Encrypted(u"xorb1", io)
        self._raw__raw_is_dagger = self._io.read_bytes(1)
        self._raw_is_dagger = KaitaiStream.process_xor_many(self._raw__raw_is_dagger, b"\xD7")
        io = KaitaiStream(BytesIO(self._raw_is_dagger))
        self.is_dagger = Encrypted(u"xorb1", io)
        self._raw__raw_is_breath = self._io.read_bytes(1)
        self._raw_is_breath = KaitaiStream.process_xor_many(self._raw__raw_is_breath, b"\x11")
        io = KaitaiStream(BytesIO(self._raw_is_breath))
        self.is_breath = Encrypted(u"xorb1", io)
        self.padding = self._io.read_bytes(4)


