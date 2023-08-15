from typing import Any, ClassVar, Iterator, List

from typing import overload
import lief # type: ignore
import lief.Android # type: ignore
import lief.DEX # type: ignore
import lief.ELF # type: ignore
import lief.OAT # type: ignore

class Binary(lief.ELF.Binary):
    class it_classes:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> lief.OAT.Class: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Class: ...

    class it_dex_files:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> lief.DEX.File: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.DEX.File: ...

    class it_methods:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> lief.OAT.Method: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Method: ...

    class it_oat_dex_files:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> lief.OAT.DexFile: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.DexFile: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def get_class(self, class_name: str) -> lief.OAT.Class: ...
    @overload
    def get_class(self, class_index: int) -> lief.OAT.Class: ...
    @property
    def classes(self) -> lief.OAT.Binary.it_classes: ...
    @property
    def dex2dex_json_info(self) -> str: ...
    @property
    def dex_files(self) -> lief.OAT.Binary.it_dex_files: ...
    @property
    def has_class(self) -> bool: ...
    @property
    def header(self) -> Any: ...
    @property
    def methods(self) -> lief.OAT.Binary.it_methods: ...
    @property
    def oat_dex_files(self) -> lief.OAT.Binary.it_oat_dex_files: ...

class Class(lief.Object):
    class it_methods:
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> lief.OAT.Method: ...
        def __iter__(self) -> Iterator: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Method: ...
    def __init__(self) -> None: ...
    def has_dex_class(self) -> bool: ...
    @overload
    def is_quickened(self, dex_method: lief.DEX.Method) -> bool: ...
    @overload
    def is_quickened(self, method_index: int) -> bool: ...
    @overload
    def method_offsets_index(self, arg0: lief.DEX.Method) -> int: ...
    @overload
    def method_offsets_index(self, arg0: int) -> int: ...
    @property
    def bitmap(self) -> List[int]: ...
    @property
    def fullname(self) -> str: ...
    @property
    def index(self) -> int: ...
    @property
    def methods(self) -> lief.OAT.Class.it_methods: ...
    @property
    def status(self) -> lief.OAT.OAT_CLASS_STATUS: ...
    @property
    def type(self) -> lief.OAT.OAT_CLASS_TYPES: ...

class DexFile(lief.Object):
    checksum: int
    dex_offset: int
    location: str
    def __init__(self) -> None: ...
    @property
    def dex_file(self) -> lief.DEX.File: ...
    @property
    def has_dex_file(self) -> bool: ...

class HEADER_KEYS:
    __members__: ClassVar[dict] = ...  # read-only
    BOOT_CLASS_PATH: ClassVar[HEADER_KEYS] = ...
    CLASS_PATH: ClassVar[HEADER_KEYS] = ...
    COMPILER_FILTER: ClassVar[HEADER_KEYS] = ...
    CONCURRENT_COPYING: ClassVar[HEADER_KEYS] = ...
    DEBUGGABLE: ClassVar[HEADER_KEYS] = ...
    DEX2OAT_CMD_LINE: ClassVar[HEADER_KEYS] = ...
    DEX2OAT_HOST: ClassVar[HEADER_KEYS] = ...
    HAS_PATCH_INFO: ClassVar[HEADER_KEYS] = ...
    IMAGE_LOCATION: ClassVar[HEADER_KEYS] = ...
    NATIVE_DEBUGGABLE: ClassVar[HEADER_KEYS] = ...
    PIC: ClassVar[HEADER_KEYS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Header(lief.Object):
    class it_key_values_t:
        class value_type:
            value: str
            def __init__(self, *args, **kwargs) -> None: ...
            @property
            def key(self) -> lief.OAT.HEADER_KEYS: ...
        def __init__(self, *args, **kwargs) -> None: ...
        def __getitem__(self, arg0: int) -> lief.OAT.Header.it_key_values_t.value_type: ...
        def __iter__(self) -> lief.OAT.Header.it_key_values_t: ...
        def __len__(self) -> int: ...
        def __next__(self) -> lief.OAT.Header.it_key_values_t.value_type: ...
    def __init__(self) -> None: ...
    def get(self, key: lief.OAT.HEADER_KEYS) -> str: ...
    def set(self, key: lief.OAT.HEADER_KEYS, value: str) -> Any: ...
    def __getitem__(self, arg0: lief.OAT.HEADER_KEYS) -> str: ...
    def __setitem__(self, arg0: lief.OAT.HEADER_KEYS, arg1: str) -> Any: ...
    @property
    def checksum(self) -> int: ...
    @property
    def executable_offset(self) -> int: ...
    @property
    def i2c_code_bridge_offset(self) -> int: ...
    @property
    def i2i_bridge_offset(self) -> int: ...
    @property
    def image_file_location_oat_checksum(self) -> int: ...
    @property
    def image_file_location_oat_data_begin(self) -> int: ...
    @property
    def image_patch_delta(self) -> int: ...
    @property
    def instruction_set(self) -> lief.OAT.INSTRUCTION_SETS: ...
    @property
    def jni_dlsym_lookup_offset(self) -> int: ...
    @property
    def key_value_size(self) -> int: ...
    @property
    def key_values(self) -> lief.OAT.Header.it_key_values_t: ...
    @property
    def keys(self) -> List[lief.OAT.HEADER_KEYS]: ...
    @property
    def magic(self) -> List[int]: ...
    @property
    def nb_dex_files(self) -> int: ...
    @property
    def oat_dex_files_offset(self) -> int: ...
    @property
    def quick_generic_jni_trampoline_offset(self) -> int: ...
    @property
    def quick_imt_conflict_trampoline_offset(self) -> int: ...
    @property
    def quick_resolution_trampoline_offset(self) -> int: ...
    @property
    def quick_to_interpreter_bridge_offset(self) -> int: ...
    @property
    def values(self) -> List[str]: ...
    @property
    def version(self) -> int: ...

class INSTRUCTION_SETS:
    __members__: ClassVar[dict] = ...  # read-only
    ARM: ClassVar[INSTRUCTION_SETS] = ...
    ARM_64: ClassVar[INSTRUCTION_SETS] = ...
    MIPS: ClassVar[INSTRUCTION_SETS] = ...
    MIPS_64: ClassVar[INSTRUCTION_SETS] = ...
    NONE: ClassVar[INSTRUCTION_SETS] = ...
    THUMB2: ClassVar[INSTRUCTION_SETS] = ...
    X86: ClassVar[INSTRUCTION_SETS] = ...
    X86_64: ClassVar[INSTRUCTION_SETS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class Method(lief.Object):
    quick_code: List[int]
    def __init__(self) -> None: ...
    @property
    def dex_method(self) -> lief.DEX.Method: ...
    @property
    def has_dex_method(self) -> bool: ...
    @property
    def is_compiled(self) -> bool: ...
    @property
    def is_dex2dex_optimized(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def oat_class(self) -> lief.OAT.Class: ...

class OAT_CLASS_STATUS:
    __members__: ClassVar[dict] = ...  # read-only
    ERROR: ClassVar[OAT_CLASS_STATUS] = ...
    IDX: ClassVar[OAT_CLASS_STATUS] = ...
    INITIALIZED: ClassVar[OAT_CLASS_STATUS] = ...
    INITIALIZING: ClassVar[OAT_CLASS_STATUS] = ...
    LOADED: ClassVar[OAT_CLASS_STATUS] = ...
    NOTREADY: ClassVar[OAT_CLASS_STATUS] = ...
    RESOLVED: ClassVar[OAT_CLASS_STATUS] = ...
    RESOLVING: ClassVar[OAT_CLASS_STATUS] = ...
    RETIRED: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFICATION_AT_RUNTIME: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFIED: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFYING: ClassVar[OAT_CLASS_STATUS] = ...
    VERIFYING_AT_RUNTIME: ClassVar[OAT_CLASS_STATUS] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class OAT_CLASS_TYPES:
    __members__: ClassVar[dict] = ...  # read-only
    ALL_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    NONE_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    SOME_COMPILED: ClassVar[OAT_CLASS_TYPES] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

def android_version(arg0: int) -> lief.Android.ANDROID_VERSIONS: ...
@overload
def is_oat(binary: lief.ELF.Binary) -> bool: ...
@overload
def is_oat(path: str) -> bool: ...
@overload
def is_oat(raw: List[int]) -> bool: ...
@overload
def parse(oat_file: str) -> lief.OAT.Binary: ...
@overload
def parse(oat_file: str, vdex_file: str) -> lief.OAT.Binary: ...
@overload
def parse(raw: List[int], name: str = ...) -> lief.OAT.Binary: ...
@overload
def parse(io: object, name: str = ...) -> lief.OAT.Binary: ...
@overload
def version(binary: lief.ELF.Binary) -> int: ...
@overload
def version(file: str) -> int: ...
@overload
def version(raw: List[int]) -> int: ...
