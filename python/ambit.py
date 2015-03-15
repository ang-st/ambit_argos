'''Wrapper for crc16.h

Generated with:
/home/pg/anaconda/bin/ctypesgen.py -llibambit.so ../src/libambit/crc16.h ../src/libambit/debug.h ../src/libambit/device_driver_common.h ../src/libambit/device_driver.h ../src/libambit/device_support.h ../src/libambit/libambit.h ../src/libambit/libambit_int.h ../src/libambit/personal.h ../src/libambit/pmem20.h ../src/libambit/protocol.h ../src/libambit/sbem0102.h ../src/libambit/sha256.h ../src/libambit/utils.h -o ambit.py

Do not modify this file.
'''

__docformat__ =  'restructuredtext'

# Begin preamble

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, 'c_int64'):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types

class c_void(Structure):
    # c_void_p is a buggy return type, converting to int, so
    # POINTER(None) == c_void_p is actually written as
    # POINTER(c_void), so it can be treated as a real pointer.
    _fields_ = [('dummy', c_int)]

def POINTER(obj):
    p = ctypes.POINTER(obj)

    # Convert None to a real NULL pointer to work around bugs
    # in how ctypes handles None on 64-bit platforms
    if not isinstance(p.from_param, classmethod):
        def from_param(cls, x):
            if x is None:
                return cls()
            else:
                return x
        p.from_param = classmethod(from_param)

    return p

class UserString:
    def __init__(self, seq):
        if isinstance(seq, basestring):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq)
    def __str__(self): return str(self.data)
    def __repr__(self): return repr(self.data)
    def __int__(self): return int(self.data)
    def __long__(self): return long(self.data)
    def __float__(self): return float(self.data)
    def __complex__(self): return complex(self.data)
    def __hash__(self): return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)
    def __contains__(self, char):
        return char in self.data

    def __len__(self): return len(self.data)
    def __getitem__(self, index): return self.__class__(self.data[index])
    def __getslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, basestring):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other))
    def __radd__(self, other):
        if isinstance(other, basestring):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other) + self.data)
    def __mul__(self, n):
        return self.__class__(self.data*n)
    __rmul__ = __mul__
    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self): return self.__class__(self.data.capitalize())
    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))
    def count(self, sub, start=0, end=sys.maxint):
        return self.data.count(sub, start, end)
    def decode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())
    def encode(self, encoding=None, errors=None): # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())
    def endswith(self, suffix, start=0, end=sys.maxint):
        return self.data.endswith(suffix, start, end)
    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))
    def find(self, sub, start=0, end=sys.maxint):
        return self.data.find(sub, start, end)
    def index(self, sub, start=0, end=sys.maxint):
        return self.data.index(sub, start, end)
    def isalpha(self): return self.data.isalpha()
    def isalnum(self): return self.data.isalnum()
    def isdecimal(self): return self.data.isdecimal()
    def isdigit(self): return self.data.isdigit()
    def islower(self): return self.data.islower()
    def isnumeric(self): return self.data.isnumeric()
    def isspace(self): return self.data.isspace()
    def istitle(self): return self.data.istitle()
    def isupper(self): return self.data.isupper()
    def join(self, seq): return self.data.join(seq)
    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))
    def lower(self): return self.__class__(self.data.lower())
    def lstrip(self, chars=None): return self.__class__(self.data.lstrip(chars))
    def partition(self, sep):
        return self.data.partition(sep)
    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))
    def rfind(self, sub, start=0, end=sys.maxint):
        return self.data.rfind(sub, start, end)
    def rindex(self, sub, start=0, end=sys.maxint):
        return self.data.rindex(sub, start, end)
    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))
    def rpartition(self, sep):
        return self.data.rpartition(sep)
    def rstrip(self, chars=None): return self.__class__(self.data.rstrip(chars))
    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)
    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)
    def splitlines(self, keepends=0): return self.data.splitlines(keepends)
    def startswith(self, prefix, start=0, end=sys.maxint):
        return self.data.startswith(prefix, start, end)
    def strip(self, chars=None): return self.__class__(self.data.strip(chars))
    def swapcase(self): return self.__class__(self.data.swapcase())
    def title(self): return self.__class__(self.data.title())
    def translate(self, *args):
        return self.__class__(self.data.translate(*args))
    def upper(self): return self.__class__(self.data.upper())
    def zfill(self, width): return self.__class__(self.data.zfill(width))

class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""
    def __init__(self, string=""):
        self.data = string
    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")
    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + sub + self.data[index+1:]
    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data): raise IndexError
        self.data = self.data[:index] + self.data[index+1:]
    def __setslice__(self, start, end, sub):
        start = max(start, 0); end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start]+sub.data+self.data[end:]
        elif isinstance(sub, basestring):
            self.data = self.data[:start]+sub+self.data[end:]
        else:
            self.data =  self.data[:start]+str(sub)+self.data[end:]
    def __delslice__(self, start, end):
        start = max(start, 0); end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]
    def immutable(self):
        return UserString(self.data)
    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, basestring):
            self.data += other
        else:
            self.data += str(other)
        return self
    def __imul__(self, n):
        self.data *= n
        return self

class String(MutableString, Union):

    _fields_ = [('raw', POINTER(c_char)),
                ('data', c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (str, unicode, UserString)):
            self.data = str(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj)

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)
    from_param = classmethod(from_param)

def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)

# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if (hasattr(type, "_type_") and isinstance(type._type_, str)
        and type._type_ != "P"):
        return type
    else:
        return c_void_p

# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self,func,restype,argtypes):
        self.func=func
        self.func.restype=restype
        self.argtypes=argtypes
    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func
    def __call__(self,*args):
        fixed_args=[]
        i=0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i+=1
        return self.func(*fixed_args+list(args[i:]))

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import ctypes
import ctypes.util

def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []

class LibraryLoader(object):
    def __init__(self):
        self.other_dirs=[]

    def load_library(self,libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            if os.path.exists(path):
                return self.load(path)

        raise ImportError("%s not found." % libname)

    def load(self,path):
        """Given a path to a library, load it."""
        try:
            # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
            # of the default RTLD_LOCAL.  Without this, you end up with
            # libraries not being loadable, resulting in "Symbol not found"
            # errors
            if sys.platform == 'darwin':
                return ctypes.CDLL(path, ctypes.RTLD_GLOBAL)
            else:
                return ctypes.cdll.LoadLibrary(path)
        except OSError,e:
            raise ImportError(e)

    def getpaths(self,libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname

        else:
            for path in self.getplatformpaths(libname):
                yield path

            path = ctypes.util.find_library(libname)
            if path: yield path

    def getplatformpaths(self, libname):
        return []

# Darwin (Mac OS X)

class DarwinLibraryLoader(LibraryLoader):
    name_formats = ["lib%s.dylib", "lib%s.so", "lib%s.bundle", "%s.dylib",
                "%s.so", "%s.bundle", "%s"]

    def getplatformpaths(self,libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir,name)

    def getdirs(self,libname):
        '''Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        '''

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser('~/lib'),
                                          '/usr/local/lib', '/usr/lib']

        dirs = []

        if '/' in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        dirs.extend(self.other_dirs)
        dirs.append(".")

        if hasattr(sys, 'frozen') and sys.frozen == 'macosx_app':
            dirs.append(os.path.join(
                os.environ['RESOURCEPATH'],
                '..',
                'Frameworks'))

        dirs.extend(dyld_fallback_library_path)

        return dirs

# Posix

class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = []
        for name in ("LD_LIBRARY_PATH",
                     "SHLIB_PATH", # HPUX
                     "LIBPATH", # OS/2, AIX
                     "LIBRARY_PATH", # BE/OS
                    ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))
        directories.extend(self.other_dirs)
        directories.append(".")

        try: directories.extend([dir.strip() for dir in open('/etc/ld.so.conf')])
        except IOError: pass

        directories.extend(['/lib', '/usr/lib', '/lib64', '/usr/lib64'])

        cache = {}
        lib_re = re.compile(r'lib(.*)\.s[ol]')
        ext_re = re.compile(r'\.s[ol]$')
        for dir in directories:
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    if file not in cache:
                        cache[file] = path

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        if library not in cache:
                            cache[library] = path
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname)
        if result: yield result

        path = ctypes.util.find_library(libname)
        if path: yield os.path.join("/lib",path)

# Windows

class _WindowsLibrary(object):
    def __init__(self, path):
        self.cdll = ctypes.cdll.LoadLibrary(path)
        self.windll = ctypes.windll.LoadLibrary(path)

    def __getattr__(self, name):
        try: return getattr(self.cdll,name)
        except AttributeError:
            try: return getattr(self.windll,name)
            except AttributeError:
                raise

class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll"]

    def load_library(self, libname):
        try:
            result = LibraryLoader.load_library(self, libname)
        except ImportError:
            result = None
            if os.path.sep not in libname:
                for name in self.name_formats:
                    try:
                        result = getattr(ctypes.cdll, name % libname)
                        if result:
                            break
                    except WindowsError:
                        result = None
            if result is None:
                try:
                    result = getattr(ctypes.cdll, libname)
                except WindowsError:
                    result = None
            if result is None:
                raise ImportError("%s not found." % libname)
        return result

    def load(self, path):
        return _WindowsLibrary(path)

    def getplatformpaths(self, libname):
        if os.path.sep not in libname:
            for name in self.name_formats:
                dll_in_current_dir = os.path.abspath(name % libname)
                if os.path.exists(dll_in_current_dir):
                    yield dll_in_current_dir
                path = ctypes.util.find_library(name % libname)
                if path:
                    yield path

# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin":   DarwinLibraryLoader,
    "cygwin":   WindowsLibraryLoader,
    "win32":    WindowsLibraryLoader
}

loader = loaderclass.get(sys.platform, PosixLibraryLoader)()

def add_library_search_dirs(other_dirs):
    loader.other_dirs = other_dirs

load_library = loader.load_library

del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries

_libs["libambit.so"] = load_library("libambit.so")

# 1 libraries
# End libraries

# No modules

# /home/pg/code/argos_ambit/openambit/src/libambit/crc16.h: 28
if hasattr(_libs['libambit.so'], 'crc16_ccitt_false'):
    crc16_ccitt_false = _libs['libambit.so'].crc16_ccitt_false
    crc16_ccitt_false.argtypes = [POINTER(c_ubyte), c_size_t]
    crc16_ccitt_false.restype = c_uint16

# /home/pg/code/argos_ambit/openambit/src/libambit/crc16.h: 29
if hasattr(_libs['libambit.so'], 'crc16_ccitt_false_init'):
    crc16_ccitt_false_init = _libs['libambit.so'].crc16_ccitt_false_init
    crc16_ccitt_false_init.argtypes = [POINTER(c_ubyte), c_size_t, c_uint16]
    crc16_ccitt_false_init.restype = c_uint16

enum_debug_level_e = c_int # /home/pg/code/argos_ambit/openambit/src/libambit/debug.h: 32

debug_level_err = 0 # /home/pg/code/argos_ambit/openambit/src/libambit/debug.h: 32

debug_level_warn = (debug_level_err + 1) # /home/pg/code/argos_ambit/openambit/src/libambit/debug.h: 32

debug_level_info = (debug_level_warn + 1) # /home/pg/code/argos_ambit/openambit/src/libambit/debug.h: 32

debug_level_t = enum_debug_level_e # /home/pg/code/argos_ambit/openambit/src/libambit/debug.h: 32

# /home/pg/code/argos_ambit/openambit/src/libambit/debug.h: 34
if hasattr(_libs['libambit.so'], 'debug_printf'):
    _func = _libs['libambit.so'].debug_printf
    _restype = None
    _argtypes = [debug_level_t, String, c_int, String, String]
    debug_printf = _variadic_function(_func,_restype,_argtypes)

# /usr/include/time.h: 133
class struct_tm(Structure):
    pass

struct_tm.__slots__ = [
    'tm_sec',
    'tm_min',
    'tm_hour',
    'tm_mday',
    'tm_mon',
    'tm_year',
    'tm_wday',
    'tm_yday',
    'tm_isdst',
    'tm_gmtoff',
    'tm_zone',
]
struct_tm._fields_ = [
    ('tm_sec', c_int),
    ('tm_min', c_int),
    ('tm_hour', c_int),
    ('tm_mday', c_int),
    ('tm_mon', c_int),
    ('tm_year', c_int),
    ('tm_wday', c_int),
    ('tm_yday', c_int),
    ('tm_isdst', c_int),
    ('tm_gmtoff', c_long),
    ('tm_zone', String),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit_int.h: 29
class struct_ambit_object_s(Structure):
    pass

ambit_object_t = struct_ambit_object_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 33

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 35
class struct_ambit_device_info_s(Structure):
    pass

struct_ambit_device_info_s.__slots__ = [
    'name',
    'model',
    'serial',
    'fw_version',
    'hw_version',
    'path',
    'vendor_id',
    'product_id',
    'is_supported',
    'access_status',
    'next',
]
struct_ambit_device_info_s._fields_ = [
    ('name', String),
    ('model', String),
    ('serial', String),
    ('fw_version', c_uint8 * 4),
    ('hw_version', c_uint8 * 4),
    ('path', String),
    ('vendor_id', c_uint16),
    ('product_id', c_uint16),
    ('is_supported', c_uint8),
    ('access_status', c_int),
    ('next', POINTER(struct_ambit_device_info_s)),
]

ambit_device_info_t = struct_ambit_device_info_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 49

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 53
class struct_ambit_device_status_s(Structure):
    pass

struct_ambit_device_status_s.__slots__ = [
    'charge',
]
struct_ambit_device_status_s._fields_ = [
    ('charge', c_uint8),
]

ambit_device_status_t = struct_ambit_device_status_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 53

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 60
class struct_anon_2(Structure):
    pass

struct_anon_2.__slots__ = [
    'pressure',
    'altitude',
    'distance',
    'height',
    'temperature',
    'verticalspeed',
    'weight',
    'compass',
    'heartrate',
    'speed',
]
struct_anon_2._fields_ = [
    ('pressure', c_uint8),
    ('altitude', c_uint8),
    ('distance', c_uint8),
    ('height', c_uint8),
    ('temperature', c_uint8),
    ('verticalspeed', c_uint8),
    ('weight', c_uint8),
    ('compass', c_uint8),
    ('heartrate', c_uint8),
    ('speed', c_uint8),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 77
class struct_anon_3(Structure):
    pass

struct_anon_3.__slots__ = [
    'hour',
    'minute',
]
struct_anon_3._fields_ = [
    ('hour', c_uint8),
    ('minute', c_uint8),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 82
class struct_anon_4(Structure):
    pass

struct_anon_4.__slots__ = [
    'hour',
    'minute',
]
struct_anon_4._fields_ = [
    ('hour', c_uint8),
    ('minute', c_uint8),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 109
class struct_ambit_personal_settings_s(Structure):
    pass

struct_ambit_personal_settings_s.__slots__ = [
    'sportmode_button_lock',
    'timemode_button_lock',
    'compass_declination',
    'units_mode',
    'units',
    'gps_position_format',
    'language',
    'navigation_style',
    'sync_time_w_gps',
    'time_format',
    'alarm',
    'alarm_enable',
    'dual_time',
    'date_format',
    'tones_mode',
    'backlight_mode',
    'backlight_brightness',
    'display_brightness',
    'display_is_negative',
    'weight',
    'birthyear',
    'max_hr',
    'rest_hr',
    'fitness_level',
    'is_male',
    'length',
    'alti_baro_mode',
    'storm_alarm',
    'fused_alti_disabled',
    'bikepod_calibration',
    'bikepod_calibration2',
    'bikepod_calibration3',
    'footpod_calibration',
    'automatic_bikepower_calib',
    'automatic_footpod_calib',
    'training_program',
]
struct_ambit_personal_settings_s._fields_ = [
    ('sportmode_button_lock', c_uint8),
    ('timemode_button_lock', c_uint8),
    ('compass_declination', c_uint16),
    ('units_mode', c_uint8),
    ('units', struct_anon_2),
    ('gps_position_format', c_uint8),
    ('language', c_uint8),
    ('navigation_style', c_uint8),
    ('sync_time_w_gps', c_uint8),
    ('time_format', c_uint8),
    ('alarm', struct_anon_3),
    ('alarm_enable', c_uint8),
    ('dual_time', struct_anon_4),
    ('date_format', c_uint8),
    ('tones_mode', c_uint8),
    ('backlight_mode', c_uint8),
    ('backlight_brightness', c_uint8),
    ('display_brightness', c_uint8),
    ('display_is_negative', c_uint8),
    ('weight', c_uint16),
    ('birthyear', c_uint16),
    ('max_hr', c_uint8),
    ('rest_hr', c_uint8),
    ('fitness_level', c_uint8),
    ('is_male', c_uint8),
    ('length', c_uint8),
    ('alti_baro_mode', c_uint8),
    ('storm_alarm', c_uint8),
    ('fused_alti_disabled', c_uint8),
    ('bikepod_calibration', c_uint16),
    ('bikepod_calibration2', c_uint16),
    ('bikepod_calibration3', c_uint16),
    ('footpod_calibration', c_uint16),
    ('automatic_bikepower_calib', c_uint8),
    ('automatic_footpod_calib', c_uint8),
    ('training_program', c_uint8),
]

ambit_personal_settings_t = struct_ambit_personal_settings_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 109

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 118
class struct_ambit_log_date_time_s(Structure):
    pass

struct_ambit_log_date_time_s.__slots__ = [
    'year',
    'month',
    'day',
    'hour',
    'minute',
    'msec',
]
struct_ambit_log_date_time_s._fields_ = [
    ('year', c_uint16),
    ('month', c_uint8),
    ('day', c_uint8),
    ('hour', c_uint8),
    ('minute', c_uint8),
    ('msec', c_uint16),
]

ambit_date_time_t = struct_ambit_log_date_time_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 118

enum_ambit_log_sample_type_e = c_int # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_periodic = 512 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_logpause = 772 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_logrestart = 773 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_ibi = 774 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_ttff = 775 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_distance_source = 776 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_lapinfo = 777 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_altitude_source = 781 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_gps_base = 783 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_gps_small = 784 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_gps_tiny = 785 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_time = 786 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_swimming_turn = 788 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_swimming_stroke = 789 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_activity = 792 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_cadence_source = 794 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_position = 795 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_fwinfo = 796 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_unknown = 61440 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

ambit_log_sample_type_t = enum_ambit_log_sample_type_e # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 140

enum_ambit_log_sample_periodic_type_e = c_int # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_latitude = 1 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_longitude = 2 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_distance = 3 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_speed = 4 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_hr = 5 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_time = 6 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_gpsspeed = 7 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_wristaccspeed = 8 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_bikepodspeed = 9 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_ehpe = 10 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_evpe = 11 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_altitude = 12 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_abspressure = 13 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_energy = 14 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_temperature = 15 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_charge = 16 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_gpsaltitude = 17 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_gpsheading = 18 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_gpshdop = 19 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_gpsvdop = 20 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_wristcadence = 21 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_snr = 22 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_noofsatellites = 23 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_sealevelpressure = 24 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_verticalspeed = 25 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_cadence = 26 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_bikepower = 31 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_swimingstrokecnt = 32 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_ruleoutput1 = 100 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_ruleoutput2 = 101 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_ruleoutput3 = 102 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_ruleoutput4 = 103 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_ruleoutput5 = 104 # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

ambit_log_sample_periodic_type_t = enum_ambit_log_sample_periodic_type_e # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 176

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 180
class union_anon_5(Union):
    pass

union_anon_5.__slots__ = [
    'latitude',
    'longitude',
    'distance',
    'speed',
    'hr',
    'time',
    'gpsspeed',
    'wristaccspeed',
    'bikepodspeed',
    'ehpe',
    'evpe',
    'altitude',
    'abspressure',
    'energy',
    'temperature',
    'charge',
    'gpsaltitude',
    'gpsheading',
    'gpshdop',
    'gpsvdop',
    'wristcadence',
    'snr',
    'noofsatellites',
    'sealevelpressure',
    'verticalspeed',
    'cadence',
    'bikepower',
    'swimingstrokecnt',
    'ruleoutput1',
    'ruleoutput2',
    'ruleoutput3',
    'ruleoutput4',
    'ruleoutput5',
]
union_anon_5._fields_ = [
    ('latitude', c_int32),
    ('longitude', c_int32),
    ('distance', c_uint32),
    ('speed', c_uint16),
    ('hr', c_uint8),
    ('time', c_uint32),
    ('gpsspeed', c_uint16),
    ('wristaccspeed', c_uint16),
    ('bikepodspeed', c_uint16),
    ('ehpe', c_uint32),
    ('evpe', c_uint32),
    ('altitude', c_int16),
    ('abspressure', c_uint16),
    ('energy', c_uint16),
    ('temperature', c_int16),
    ('charge', c_uint8),
    ('gpsaltitude', c_int32),
    ('gpsheading', c_uint16),
    ('gpshdop', c_uint8),
    ('gpsvdop', c_uint8),
    ('wristcadence', c_uint16),
    ('snr', c_uint8 * 16),
    ('noofsatellites', c_uint8),
    ('sealevelpressure', c_int16),
    ('verticalspeed', c_int16),
    ('cadence', c_uint8),
    ('bikepower', c_uint16),
    ('swimingstrokecnt', c_uint32),
    ('ruleoutput1', c_int32),
    ('ruleoutput2', c_int32),
    ('ruleoutput3', c_int32),
    ('ruleoutput4', c_int32),
    ('ruleoutput5', c_int32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 215
class struct_ambit_log_sample_periodic_value_s(Structure):
    pass

struct_ambit_log_sample_periodic_value_s.__slots__ = [
    'type',
    'u',
]
struct_ambit_log_sample_periodic_value_s._fields_ = [
    ('type', ambit_log_sample_periodic_type_t),
    ('u', union_anon_5),
]

ambit_log_sample_periodic_value_t = struct_ambit_log_sample_periodic_value_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 215

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 221
class struct_ambit_log_gps_satellite_s(Structure):
    pass

struct_ambit_log_gps_satellite_s.__slots__ = [
    'sv',
    'snr',
    'state',
]
struct_ambit_log_gps_satellite_s._fields_ = [
    ('sv', c_uint8),
    ('snr', c_uint8),
    ('state', c_uint8),
]

ambit_log_gps_satellite_t = struct_ambit_log_gps_satellite_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 221

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 228
class struct_anon_6(Structure):
    pass

struct_anon_6.__slots__ = [
    'value_count',
    'values',
]
struct_anon_6._fields_ = [
    ('value_count', c_uint8),
    ('values', POINTER(ambit_log_sample_periodic_value_t)),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 232
class struct_anon_7(Structure):
    pass

struct_anon_7.__slots__ = [
    'ibi_count',
    'ibi',
]
struct_anon_7._fields_ = [
    ('ibi_count', c_uint8),
    ('ibi', c_uint16 * 32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 243
class struct_anon_8(Structure):
    pass

struct_anon_8.__slots__ = [
    'event_type',
    'date_time',
    'duration',
    'distance',
]
struct_anon_8._fields_ = [
    ('event_type', c_uint8),
    ('date_time', ambit_date_time_t),
    ('duration', c_uint32),
    ('distance', c_uint32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 254
class struct_anon_9(Structure):
    pass

struct_anon_9.__slots__ = [
    'source_type',
    'altitude_offset',
    'pressure_offset',
]
struct_anon_9._fields_ = [
    ('source_type', c_uint8),
    ('altitude_offset', c_int16),
    ('pressure_offset', c_int16),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 259
class struct_anon_10(Structure):
    pass

struct_anon_10.__slots__ = [
    'navvalid',
    'navtype',
    'utc_base_time',
    'latitude',
    'longitude',
    'altitude',
    'speed',
    'heading',
    'ehpe',
    'noofsatellites',
    'hdop',
    'satellites_count',
    'satellites',
]
struct_anon_10._fields_ = [
    ('navvalid', c_uint16),
    ('navtype', c_uint16),
    ('utc_base_time', ambit_date_time_t),
    ('latitude', c_int32),
    ('longitude', c_int32),
    ('altitude', c_int32),
    ('speed', c_uint16),
    ('heading', c_uint16),
    ('ehpe', c_uint32),
    ('noofsatellites', c_uint8),
    ('hdop', c_uint8),
    ('satellites_count', c_uint8),
    ('satellites', POINTER(ambit_log_gps_satellite_t)),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 274
class struct_anon_11(Structure):
    pass

struct_anon_11.__slots__ = [
    'noofsatellites',
    'latitude',
    'longitude',
    'ehpe',
]
struct_anon_11._fields_ = [
    ('noofsatellites', c_uint8),
    ('latitude', c_int32),
    ('longitude', c_int32),
    ('ehpe', c_uint32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 280
class struct_anon_12(Structure):
    pass

struct_anon_12.__slots__ = [
    'latitude',
    'longitude',
    'ehpe',
    'unknown',
]
struct_anon_12._fields_ = [
    ('latitude', c_int32),
    ('longitude', c_int32),
    ('ehpe', c_uint32),
    ('unknown', c_uint8),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 286
class struct_anon_13(Structure):
    pass

struct_anon_13.__slots__ = [
    'hour',
    'minute',
    'second',
]
struct_anon_13._fields_ = [
    ('hour', c_uint8),
    ('minute', c_uint8),
    ('second', c_uint8),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 291
class struct_anon_14(Structure):
    pass

struct_anon_14.__slots__ = [
    'distance',
    'lengths',
    'classification',
    'style',
]
struct_anon_14._fields_ = [
    ('distance', c_uint32),
    ('lengths', c_uint16),
    ('classification', c_uint16 * 4),
    ('style', c_uint8),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 303
class struct_anon_15(Structure):
    pass

struct_anon_15.__slots__ = [
    'activitytype',
    'custommode',
]
struct_anon_15._fields_ = [
    ('activitytype', c_uint16),
    ('custommode', c_uint32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 308
class struct_anon_16(Structure):
    pass

struct_anon_16.__slots__ = [
    'latitude',
    'longitude',
]
struct_anon_16._fields_ = [
    ('latitude', c_int32),
    ('longitude', c_int32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 312
class struct_anon_17(Structure):
    pass

struct_anon_17.__slots__ = [
    'version',
    'build_date',
]
struct_anon_17._fields_ = [
    ('version', c_uint8 * 4),
    ('build_date', ambit_date_time_t),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 316
class struct_anon_18(Structure):
    pass

struct_anon_18.__slots__ = [
    'datalen',
    'data',
]
struct_anon_18._fields_ = [
    ('datalen', c_size_t),
    ('data', POINTER(c_uint8)),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 227
class union_anon_19(Union):
    pass

union_anon_19.__slots__ = [
    'periodic',
    'ibi',
    'ttff',
    'distance_source',
    'lapinfo',
    'altitude_source',
    'gps_base',
    'gps_small',
    'gps_tiny',
    'time',
    'swimming_turn',
    'activity',
    'cadence_source',
    'position',
    'fwinfo',
    'unknown',
]
union_anon_19._fields_ = [
    ('periodic', struct_anon_6),
    ('ibi', struct_anon_7),
    ('ttff', c_uint16),
    ('distance_source', c_uint8),
    ('lapinfo', struct_anon_8),
    ('altitude_source', struct_anon_9),
    ('gps_base', struct_anon_10),
    ('gps_small', struct_anon_11),
    ('gps_tiny', struct_anon_12),
    ('time', struct_anon_13),
    ('swimming_turn', struct_anon_14),
    ('activity', struct_anon_15),
    ('cadence_source', c_uint8),
    ('position', struct_anon_16),
    ('fwinfo', struct_anon_17),
    ('unknown', struct_anon_18),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 321
class struct_ambit_log_sample_s(Structure):
    pass

struct_ambit_log_sample_s.__slots__ = [
    'type',
    'time',
    'utc_time',
    'u',
]
struct_ambit_log_sample_s._fields_ = [
    ('type', ambit_log_sample_type_t),
    ('time', c_uint32),
    ('utc_time', ambit_date_time_t),
    ('u', union_anon_19),
]

ambit_log_sample_t = struct_ambit_log_sample_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 321

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 368
class struct_ambit_log_header_s(Structure):
    pass

struct_ambit_log_header_s.__slots__ = [
    'date_time',
    'duration',
    'ascent',
    'descent',
    'ascent_time',
    'descent_time',
    'recovery_time',
    'speed_avg',
    'speed_max',
    'speed_max_time',
    'altitude_max',
    'altitude_min',
    'altitude_max_time',
    'altitude_min_time',
    'heartrate_avg',
    'heartrate_max',
    'heartrate_min',
    'heartrate_max_time',
    'heartrate_min_time',
    'peak_training_effect',
    'activity_type',
    'activity_name',
    'temperature_max',
    'temperature_min',
    'temperature_max_time',
    'temperature_min_time',
    'distance',
    'samples_count',
    'energy_consumption',
    'first_fix_time',
    'battery_start',
    'battery_end',
    'distance_before_calib',
    'unknown1',
    'unknown2',
    'cadence_max',
    'cadence_avg',
    'unknown3',
    'swimming_pool_lengths',
    'cadence_max_time',
    'swimming_pool_length',
    'unknown5',
    'unknown6',
]
struct_ambit_log_header_s._fields_ = [
    ('date_time', ambit_date_time_t),
    ('duration', c_uint32),
    ('ascent', c_uint16),
    ('descent', c_uint16),
    ('ascent_time', c_uint32),
    ('descent_time', c_uint32),
    ('recovery_time', c_uint32),
    ('speed_avg', c_uint16),
    ('speed_max', c_uint16),
    ('speed_max_time', c_uint32),
    ('altitude_max', c_int16),
    ('altitude_min', c_int16),
    ('altitude_max_time', c_uint32),
    ('altitude_min_time', c_uint32),
    ('heartrate_avg', c_uint8),
    ('heartrate_max', c_uint8),
    ('heartrate_min', c_uint8),
    ('heartrate_max_time', c_uint32),
    ('heartrate_min_time', c_uint32),
    ('peak_training_effect', c_uint8),
    ('activity_type', c_uint8),
    ('activity_name', String),
    ('temperature_max', c_int16),
    ('temperature_min', c_int16),
    ('temperature_max_time', c_uint32),
    ('temperature_min_time', c_uint32),
    ('distance', c_uint32),
    ('samples_count', c_uint32),
    ('energy_consumption', c_uint16),
    ('first_fix_time', c_uint32),
    ('battery_start', c_uint8),
    ('battery_end', c_uint8),
    ('distance_before_calib', c_uint32),
    ('unknown1', c_uint8 * 5),
    ('unknown2', c_uint8),
    ('cadence_max', c_uint8),
    ('cadence_avg', c_uint8),
    ('unknown3', c_uint8 * 2),
    ('swimming_pool_lengths', c_uint16),
    ('cadence_max_time', c_uint32),
    ('swimming_pool_length', c_uint32),
    ('unknown5', c_uint8 * 4),
    ('unknown6', c_uint8 * 24),
]

ambit_log_header_t = struct_ambit_log_header_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 368

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 374
class struct_ambit_log_entry_s(Structure):
    pass

struct_ambit_log_entry_s.__slots__ = [
    'header',
    'samples_count',
    'samples',
]
struct_ambit_log_entry_s._fields_ = [
    ('header', ambit_log_header_t),
    ('samples_count', c_uint32),
    ('samples', POINTER(ambit_log_sample_t)),
]

ambit_log_entry_t = struct_ambit_log_entry_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 374

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 381
if hasattr(_libs['libambit.so'], 'libambit_enumerate'):
    libambit_enumerate = _libs['libambit.so'].libambit_enumerate
    libambit_enumerate.argtypes = []
    libambit_enumerate.restype = POINTER(ambit_device_info_t)

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 385
if hasattr(_libs['libambit.so'], 'libambit_free_enumeration'):
    libambit_free_enumeration = _libs['libambit.so'].libambit_free_enumeration
    libambit_free_enumeration.argtypes = [POINTER(ambit_device_info_t)]
    libambit_free_enumeration.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 393
if hasattr(_libs['libambit.so'], 'libambit_new'):
    libambit_new = _libs['libambit.so'].libambit_new
    libambit_new.argtypes = [POINTER(ambit_device_info_t)]
    libambit_new.restype = POINTER(ambit_object_t)

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 400
if hasattr(_libs['libambit.so'], 'libambit_new_from_pathname'):
    libambit_new_from_pathname = _libs['libambit.so'].libambit_new_from_pathname
    libambit_new_from_pathname.argtypes = [String]
    libambit_new_from_pathname.restype = POINTER(ambit_object_t)

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 406
if hasattr(_libs['libambit.so'], 'libambit_close'):
    libambit_close = _libs['libambit.so'].libambit_close
    libambit_close.argtypes = [POINTER(ambit_object_t)]
    libambit_close.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 412
if hasattr(_libs['libambit.so'], 'libambit_sync_display_show'):
    libambit_sync_display_show = _libs['libambit.so'].libambit_sync_display_show
    libambit_sync_display_show.argtypes = [POINTER(ambit_object_t)]
    libambit_sync_display_show.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 418
if hasattr(_libs['libambit.so'], 'libambit_sync_display_clear'):
    libambit_sync_display_clear = _libs['libambit.so'].libambit_sync_display_clear
    libambit_sync_display_clear.argtypes = [POINTER(ambit_object_t)]
    libambit_sync_display_clear.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 426
if hasattr(_libs['libambit.so'], 'libambit_date_time_set'):
    libambit_date_time_set = _libs['libambit.so'].libambit_date_time_set
    libambit_date_time_set.argtypes = [POINTER(ambit_object_t), POINTER(struct_tm)]
    libambit_date_time_set.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 434
if hasattr(_libs['libambit.so'], 'libambit_device_status_get'):
    libambit_device_status_get = _libs['libambit.so'].libambit_device_status_get
    libambit_device_status_get.argtypes = [POINTER(ambit_object_t), POINTER(ambit_device_status_t)]
    libambit_device_status_get.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 442
if hasattr(_libs['libambit.so'], 'libambit_personal_settings_get'):
    libambit_personal_settings_get = _libs['libambit.so'].libambit_personal_settings_get
    libambit_personal_settings_get.argtypes = [POINTER(ambit_object_t), POINTER(ambit_personal_settings_t)]
    libambit_personal_settings_get.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 451
if hasattr(_libs['libambit.so'], 'libambit_gps_orbit_header_read'):
    libambit_gps_orbit_header_read = _libs['libambit.so'].libambit_gps_orbit_header_read
    libambit_gps_orbit_header_read.argtypes = [POINTER(ambit_object_t), c_uint8 * 8]
    libambit_gps_orbit_header_read.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 460
if hasattr(_libs['libambit.so'], 'libambit_gps_orbit_write'):
    libambit_gps_orbit_write = _libs['libambit.so'].libambit_gps_orbit_write
    libambit_gps_orbit_write.argtypes = [POINTER(ambit_object_t), POINTER(c_uint8), c_size_t]
    libambit_gps_orbit_write.restype = c_int

ambit_log_skip_cb = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(ambit_log_header_t)) # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 469

ambit_log_push_cb = CFUNCTYPE(UNCHECKED(None), POINTER(None), POINTER(ambit_log_entry_t)) # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 477

ambit_log_progress_cb = CFUNCTYPE(UNCHECKED(None), POINTER(None), c_uint16, c_uint16, c_uint8) # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 486

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 498
if hasattr(_libs['libambit.so'], 'libambit_log_read'):
    libambit_log_read = _libs['libambit.so'].libambit_log_read
    libambit_log_read.argtypes = [POINTER(ambit_object_t), ambit_log_skip_cb, ambit_log_push_cb, ambit_log_progress_cb, POINTER(None)]
    libambit_log_read.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 504
if hasattr(_libs['libambit.so'], 'libambit_log_entry_free'):
    libambit_log_entry_free = _libs['libambit.so'].libambit_log_entry_free
    libambit_log_entry_free.argtypes = [POINTER(ambit_log_entry_t)]
    libambit_log_entry_free.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 508
if hasattr(_libs['libambit.so'], 'log_skip_cb'):
    log_skip_cb = _libs['libambit.so'].log_skip_cb
    log_skip_cb.argtypes = [POINTER(None), POINTER(ambit_log_header_t)]
    log_skip_cb.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 509
if hasattr(_libs['libambit.so'], 'log_data_cb'):
    log_data_cb = _libs['libambit.so'].log_data_cb
    log_data_cb.argtypes = [POINTER(None), POINTER(ambit_log_entry_t)]
    log_data_cb.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 511
if hasattr(_libs['libambit.so'], 'mydump'):
    mydump = _libs['libambit.so'].mydump
    mydump.argtypes = [POINTER(None), ambit_log_skip_cb, ambit_log_push_cb]
    mydump.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/device_driver_common.h: 32
if hasattr(_libs['libambit.so'], 'libambit_device_driver_lock_log'):
    libambit_device_driver_lock_log = _libs['libambit.so'].libambit_device_driver_lock_log
    libambit_device_driver_lock_log.argtypes = [POINTER(ambit_object_t), c_uint8]
    libambit_device_driver_lock_log.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/device_driver_common.h: 33
if hasattr(_libs['libambit.so'], 'libambit_device_driver_date_time_set'):
    libambit_device_driver_date_time_set = _libs['libambit.so'].libambit_device_driver_date_time_set
    libambit_device_driver_date_time_set.argtypes = [POINTER(ambit_object_t), POINTER(struct_tm)]
    libambit_device_driver_date_time_set.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/device_driver_common.h: 34
if hasattr(_libs['libambit.so'], 'libambit_device_driver_status_get'):
    libambit_device_driver_status_get = _libs['libambit.so'].libambit_device_driver_status_get
    libambit_device_driver_status_get.argtypes = [POINTER(ambit_object_t), POINTER(ambit_device_status_t)]
    libambit_device_driver_status_get.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/device_driver.h: 40
class struct_ambit_device_driver_s(Structure):
    pass

struct_ambit_device_driver_s.__slots__ = [
    'init',
    'deinit',
    'lock_log',
    'date_time_set',
    'status_get',
    'personal_settings_get',
    'log_read',
    'gps_orbit_header_read',
    'gps_orbit_write',
]
struct_ambit_device_driver_s._fields_ = [
    ('init', CFUNCTYPE(UNCHECKED(None), POINTER(ambit_object_t), c_uint32)),
    ('deinit', CFUNCTYPE(UNCHECKED(None), POINTER(ambit_object_t))),
    ('lock_log', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), c_uint8)),
    ('date_time_set', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), POINTER(struct_tm))),
    ('status_get', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), POINTER(ambit_device_status_t))),
    ('personal_settings_get', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), POINTER(ambit_personal_settings_t))),
    ('log_read', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), ambit_log_skip_cb, ambit_log_push_cb, ambit_log_progress_cb, POINTER(None))),
    ('gps_orbit_header_read', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), c_uint8 * 8)),
    ('gps_orbit_write', CFUNCTYPE(UNCHECKED(c_int), POINTER(ambit_object_t), POINTER(c_uint8), c_size_t)),
]

ambit_device_driver_t = struct_ambit_device_driver_s # /home/pg/code/argos_ambit/openambit/src/libambit/device_driver.h: 40

# /home/pg/code/argos_ambit/openambit/src/libambit/device_driver.h: 42
try:
    ambit_device_driver_ambit = (ambit_device_driver_t).in_dll(_libs['libambit.so'], 'ambit_device_driver_ambit')
except:
    pass

# /home/pg/code/argos_ambit/openambit/src/libambit/device_driver.h: 43
try:
    ambit_device_driver_ambit3 = (ambit_device_driver_t).in_dll(_libs['libambit.so'], 'ambit_device_driver_ambit3')
except:
    pass

# /home/pg/code/argos_ambit/openambit/src/libambit/device_support.h: 34
class struct_ambit_known_device_s(Structure):
    pass

struct_ambit_known_device_s.__slots__ = [
    'name',
    'supported',
    'driver',
    'driver_param',
]
struct_ambit_known_device_s._fields_ = [
    ('name', String),
    ('supported', c_uint8),
    ('driver', POINTER(struct_ambit_device_driver_s)),
    ('driver_param', c_uint32),
]

ambit_known_device_t = struct_ambit_known_device_s # /home/pg/code/argos_ambit/openambit/src/libambit/device_support.h: 34

# /home/pg/code/argos_ambit/openambit/src/libambit/device_support.h: 36
if hasattr(_libs['libambit.so'], 'libambit_device_support_known'):
    libambit_device_support_known = _libs['libambit.so'].libambit_device_support_known
    libambit_device_support_known.argtypes = [c_uint16, c_uint16]
    libambit_device_support_known.restype = c_uint8

# /home/pg/code/argos_ambit/openambit/src/libambit/device_support.h: 37
if hasattr(_libs['libambit.so'], 'libambit_device_support_find'):
    libambit_device_support_find = _libs['libambit.so'].libambit_device_support_find
    libambit_device_support_find.argtypes = [c_uint16, c_uint16, String, POINTER(c_uint8)]
    libambit_device_support_find.restype = POINTER(ambit_known_device_t)

# /home/pg/code/argos_ambit/openambit/src/libambit/hidapi/hidapi.h: 45
class struct_hid_device_(Structure):
    pass

hid_device = struct_hid_device_ # /home/pg/code/argos_ambit/openambit/src/libambit/hidapi/hidapi.h: 46

# /home/pg/code/argos_ambit/openambit/src/libambit/libambit_int.h: 35
class struct_ambit_device_driver_data_s(Structure):
    pass

struct_ambit_object_s.__slots__ = [
    'handle',
    'sequence_no',
    'device_info',
    'driver',
    'driver_data',
]
struct_ambit_object_s._fields_ = [
    ('handle', POINTER(hid_device)),
    ('sequence_no', c_uint16),
    ('device_info', ambit_device_info_t),
    ('driver', POINTER(struct_ambit_device_driver_s)),
    ('driver_data', POINTER(struct_ambit_device_driver_data_s)),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/personal.h: 29
if hasattr(_libs['libambit.so'], 'libambit_personal_settings_parse'):
    libambit_personal_settings_parse = _libs['libambit.so'].libambit_personal_settings_parse
    libambit_personal_settings_parse.argtypes = [POINTER(c_uint8), c_size_t, POINTER(ambit_personal_settings_t)]
    libambit_personal_settings_parse.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 39
class struct_anon_22(Structure):
    pass

struct_anon_22.__slots__ = [
    'current',
    'next',
    'prev',
]
struct_anon_22._fields_ = [
    ('current', c_uint32),
    ('next', c_uint32),
    ('prev', c_uint32),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 31
class struct_anon_23(Structure):
    pass

struct_anon_23.__slots__ = [
    'initialized',
    'mem_start',
    'mem_size',
    'first_entry',
    'last_entry',
    'entries',
    'next_free_address',
    'current',
    'buffer',
    'chunks_read',
]
struct_anon_23._fields_ = [
    ('initialized', c_uint8),
    ('mem_start', c_uint32),
    ('mem_size', c_uint32),
    ('first_entry', c_uint32),
    ('last_entry', c_uint32),
    ('entries', c_uint32),
    ('next_free_address', c_uint32),
    ('current', struct_anon_22),
    ('buffer', POINTER(c_uint8)),
    ('chunks_read', POINTER(c_uint8)),
]

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 48
class struct_libambit_pmem20_s(Structure):
    pass

struct_libambit_pmem20_s.__slots__ = [
    'chunk_size',
    'log',
    'ambit_object',
]
struct_libambit_pmem20_s._fields_ = [
    ('chunk_size', c_uint16),
    ('log', struct_anon_23),
    ('ambit_object', POINTER(ambit_object_t)),
]

libambit_pmem20_t = struct_libambit_pmem20_s # /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 48

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 50
if hasattr(_libs['libambit.so'], 'libambit_pmem20_init'):
    libambit_pmem20_init = _libs['libambit.so'].libambit_pmem20_init
    libambit_pmem20_init.argtypes = [POINTER(libambit_pmem20_t), POINTER(ambit_object_t), c_uint16]
    libambit_pmem20_init.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 51
if hasattr(_libs['libambit.so'], 'libambit_pmem20_deinit'):
    libambit_pmem20_deinit = _libs['libambit.so'].libambit_pmem20_deinit
    libambit_pmem20_deinit.argtypes = [POINTER(libambit_pmem20_t)]
    libambit_pmem20_deinit.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 52
if hasattr(_libs['libambit.so'], 'libambit_pmem20_log_init'):
    libambit_pmem20_log_init = _libs['libambit.so'].libambit_pmem20_log_init
    libambit_pmem20_log_init.argtypes = [POINTER(libambit_pmem20_t), c_uint32, c_uint32]
    libambit_pmem20_log_init.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 53
for _lib in _libs.itervalues():
    if not hasattr(_lib, 'libambit_pmem20_log_deinit'):
        continue
    libambit_pmem20_log_deinit = _lib.libambit_pmem20_log_deinit
    libambit_pmem20_log_deinit.argtypes = [POINTER(libambit_pmem20_t)]
    libambit_pmem20_log_deinit.restype = c_int
    break

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 54
if hasattr(_libs['libambit.so'], 'libambit_pmem20_log_next_header'):
    libambit_pmem20_log_next_header = _libs['libambit.so'].libambit_pmem20_log_next_header
    libambit_pmem20_log_next_header.argtypes = [POINTER(libambit_pmem20_t), POINTER(ambit_log_header_t)]
    libambit_pmem20_log_next_header.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 55
if hasattr(_libs['libambit.so'], 'libambit_pmem20_log_read_entry'):
    libambit_pmem20_log_read_entry = _libs['libambit.so'].libambit_pmem20_log_read_entry
    libambit_pmem20_log_read_entry.argtypes = [POINTER(libambit_pmem20_t)]
    libambit_pmem20_log_read_entry.restype = POINTER(ambit_log_entry_t)

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 56
if hasattr(_libs['libambit.so'], 'libambit_pmem20_log_read_entry_address'):
    libambit_pmem20_log_read_entry_address = _libs['libambit.so'].libambit_pmem20_log_read_entry_address
    libambit_pmem20_log_read_entry_address.argtypes = [POINTER(libambit_pmem20_t), c_uint32, c_uint32]
    libambit_pmem20_log_read_entry_address.restype = POINTER(ambit_log_entry_t)

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 57
if hasattr(_libs['libambit.so'], 'libambit_pmem20_log_parse_header'):
    libambit_pmem20_log_parse_header = _libs['libambit.so'].libambit_pmem20_log_parse_header
    libambit_pmem20_log_parse_header.argtypes = [POINTER(c_uint8), c_size_t, POINTER(ambit_log_header_t)]
    libambit_pmem20_log_parse_header.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 58
if hasattr(_libs['libambit.so'], 'libambit_pmem20_gps_orbit_write'):
    libambit_pmem20_gps_orbit_write = _libs['libambit.so'].libambit_pmem20_gps_orbit_write
    libambit_pmem20_gps_orbit_write.argtypes = [POINTER(libambit_pmem20_t), POINTER(c_uint8), c_size_t, c_uint8]
    libambit_pmem20_gps_orbit_write.restype = c_int

enum_ambit_commands_e = c_int # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_device_info = 0 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_time = 768 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_date = 770 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_status = 774 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_personal_settings = 2816 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_unknown2 = 2818 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_unknown1 = 2820 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_log_count = 2822 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_log_head_first = 2823 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_log_head_peek = 2824 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_log_head_step = 2826 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_log_head = 2827 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_gps_orbit_head = 2837 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_data_write = 2838 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_log_read = 2839 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_data_tail_len = 2840 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_lock_check = 2841 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_lock_set = 2842 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_write_start = 2843 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_ambit3_memory_map = 2849 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_ambit3_settings = 4352 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_ambit3_settings_write = 4353 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_ambit3_log_headers = 4608 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

ambit_command_ambit3_log_synced = 4609 # /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 29

# /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 60
if hasattr(_libs['libambit.so'], 'libambit_protocol_command'):
    libambit_protocol_command = _libs['libambit.so'].libambit_protocol_command
    libambit_protocol_command.argtypes = [POINTER(ambit_object_t), c_uint16, POINTER(c_uint8), c_size_t, POINTER(POINTER(c_uint8)), POINTER(c_size_t), c_uint8]
    libambit_protocol_command.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/protocol.h: 61
if hasattr(_libs['libambit.so'], 'libambit_protocol_free'):
    libambit_protocol_free = _libs['libambit.so'].libambit_protocol_free
    libambit_protocol_free.argtypes = [POINTER(c_uint8)]
    libambit_protocol_free.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 32
class struct_libambit_sbem0102_s(Structure):
    pass

struct_libambit_sbem0102_s.__slots__ = [
    'chunk_size',
    'ambit_object',
]
struct_libambit_sbem0102_s._fields_ = [
    ('chunk_size', c_uint16),
    ('ambit_object', POINTER(ambit_object_t)),
]

libambit_sbem0102_t = struct_libambit_sbem0102_s # /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 32

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 38
class struct_libambit_sbem0102_data_s(Structure):
    pass

struct_libambit_sbem0102_data_s.__slots__ = [
    'data',
    'size',
    'read_ptr',
]
struct_libambit_sbem0102_data_s._fields_ = [
    ('data', POINTER(c_uint8)),
    ('size', c_size_t),
    ('read_ptr', POINTER(c_uint8)),
]

libambit_sbem0102_data_t = struct_libambit_sbem0102_data_s # /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 38

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 48
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_init'):
    libambit_sbem0102_init = _libs['libambit.so'].libambit_sbem0102_init
    libambit_sbem0102_init.argtypes = [POINTER(libambit_sbem0102_t), POINTER(ambit_object_t), c_uint16]
    libambit_sbem0102_init.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 55
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_deinit'):
    libambit_sbem0102_deinit = _libs['libambit.so'].libambit_sbem0102_deinit
    libambit_sbem0102_deinit.argtypes = [POINTER(libambit_sbem0102_t)]
    libambit_sbem0102_deinit.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 64
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_write'):
    libambit_sbem0102_write = _libs['libambit.so'].libambit_sbem0102_write
    libambit_sbem0102_write.argtypes = [POINTER(libambit_sbem0102_t), c_uint16, POINTER(libambit_sbem0102_data_t)]
    libambit_sbem0102_write.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 75
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_command_request'):
    libambit_sbem0102_command_request = _libs['libambit.so'].libambit_sbem0102_command_request
    libambit_sbem0102_command_request.argtypes = [POINTER(libambit_sbem0102_t), c_uint16, POINTER(libambit_sbem0102_data_t), POINTER(libambit_sbem0102_data_t)]
    libambit_sbem0102_command_request.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 87
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_command_request_raw'):
    libambit_sbem0102_command_request_raw = _libs['libambit.so'].libambit_sbem0102_command_request_raw
    libambit_sbem0102_command_request_raw.argtypes = [POINTER(libambit_sbem0102_t), c_uint16, POINTER(c_uint8), c_size_t, POINTER(libambit_sbem0102_data_t)]
    libambit_sbem0102_command_request_raw.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 94
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_data_init'):
    libambit_sbem0102_data_init = _libs['libambit.so'].libambit_sbem0102_data_init
    libambit_sbem0102_data_init.argtypes = [POINTER(libambit_sbem0102_data_t)]
    libambit_sbem0102_data_init.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 101
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_data_free'):
    libambit_sbem0102_data_free = _libs['libambit.so'].libambit_sbem0102_data_free
    libambit_sbem0102_data_free.argtypes = [POINTER(libambit_sbem0102_data_t)]
    libambit_sbem0102_data_free.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 110
if hasattr(_libs['libambit.so'], 'libambit_sbem0102_data_add'):
    libambit_sbem0102_data_add = _libs['libambit.so'].libambit_sbem0102_data_add
    libambit_sbem0102_data_add.argtypes = [POINTER(libambit_sbem0102_data_t), c_uint8, POINTER(c_uint8), c_uint8]
    libambit_sbem0102_data_add.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 35
class struct_anon_24(Structure):
    pass

struct_anon_24.__slots__ = [
    'data',
    'datalen',
    'bitlen',
    'h',
]
struct_anon_24._fields_ = [
    ('data', c_uint8 * (512 / 8)),
    ('datalen', c_uint32),
    ('bitlen', c_uint64),
    ('h', c_uint32 * 8),
]

sha256_ctx = struct_anon_24 # /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 35

# /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 37
if hasattr(_libs['libambit.so'], 'sha256'):
    sha256 = _libs['libambit.so'].sha256
    sha256.argtypes = [POINTER(c_uint8), c_size_t, POINTER(c_uint8)]
    sha256.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 38
if hasattr(_libs['libambit.so'], 'sha256_init'):
    sha256_init = _libs['libambit.so'].sha256_init
    sha256_init.argtypes = [POINTER(sha256_ctx)]
    sha256_init.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 39
if hasattr(_libs['libambit.so'], 'sha256_update'):
    sha256_update = _libs['libambit.so'].sha256_update
    sha256_update.argtypes = [POINTER(sha256_ctx), POINTER(c_uint8), c_size_t]
    sha256_update.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 40
if hasattr(_libs['libambit.so'], 'sha256_final'):
    sha256_final = _libs['libambit.so'].sha256_final
    sha256_final.argtypes = [POINTER(sha256_ctx), POINTER(c_uint8)]
    sha256_final.restype = None

# /home/pg/code/argos_ambit/openambit/src/libambit/utils.h: 33
if hasattr(_libs['libambit.so'], 'libambit_strptime'):
    libambit_strptime = _libs['libambit.so'].libambit_strptime
    libambit_strptime.argtypes = [String, String, POINTER(struct_tm)]
    if sizeof(c_int) == sizeof(c_void_p):
        libambit_strptime.restype = ReturnString
    else:
        libambit_strptime.restype = String
        libambit_strptime.errcheck = ReturnString

# /home/pg/code/argos_ambit/openambit/src/libambit/utils.h: 42
if hasattr(_libs['libambit.so'], 'libambit_htob'):
    libambit_htob = _libs['libambit.so'].libambit_htob
    libambit_htob.argtypes = [String, POINTER(c_uint8), c_size_t]
    libambit_htob.restype = c_int

# /home/pg/code/argos_ambit/openambit/src/libambit/utils.h: 50
if hasattr(_libs['libambit.so'], 'utf8memconv'):
    utf8memconv = _libs['libambit.so'].utf8memconv
    utf8memconv.argtypes = [String, c_size_t, String]
    if sizeof(c_int) == sizeof(c_void_p):
        utf8memconv.restype = ReturnString
    else:
        utf8memconv.restype = String
        utf8memconv.errcheck = ReturnString

# /home/pg/code/argos_ambit/openambit/src/libambit/utils.h: 58
if hasattr(_libs['libambit.so'], 'utf8wcsconv'):
    utf8wcsconv = _libs['libambit.so'].utf8wcsconv
    utf8wcsconv.argtypes = [POINTER(c_wchar)]
    if sizeof(c_int) == sizeof(c_void_p):
        utf8wcsconv.restype = ReturnString
    else:
        utf8wcsconv.restype = String
        utf8wcsconv.errcheck = ReturnString

# /home/pg/code/argos_ambit/openambit/src/libambit/sha256.h: 28
try:
    SHA256_BLOCK_SIZE = (512 / 8)
except:
    pass

ambit_object_s = struct_ambit_object_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit_int.h: 29

ambit_device_info_s = struct_ambit_device_info_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 35

ambit_device_status_s = struct_ambit_device_status_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 53

ambit_personal_settings_s = struct_ambit_personal_settings_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 109

ambit_log_date_time_s = struct_ambit_log_date_time_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 118

ambit_log_sample_periodic_value_s = struct_ambit_log_sample_periodic_value_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 215

ambit_log_gps_satellite_s = struct_ambit_log_gps_satellite_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 221

ambit_log_sample_s = struct_ambit_log_sample_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 321

ambit_log_header_s = struct_ambit_log_header_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 368

ambit_log_entry_s = struct_ambit_log_entry_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit.h: 374

ambit_device_driver_s = struct_ambit_device_driver_s # /home/pg/code/argos_ambit/openambit/src/libambit/device_driver.h: 40

ambit_known_device_s = struct_ambit_known_device_s # /home/pg/code/argos_ambit/openambit/src/libambit/device_support.h: 34

ambit_device_driver_data_s = struct_ambit_device_driver_data_s # /home/pg/code/argos_ambit/openambit/src/libambit/libambit_int.h: 35

libambit_pmem20_s = struct_libambit_pmem20_s # /home/pg/code/argos_ambit/openambit/src/libambit/pmem20.h: 48

libambit_sbem0102_s = struct_libambit_sbem0102_s # /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 32

libambit_sbem0102_data_s = struct_libambit_sbem0102_data_s # /home/pg/code/argos_ambit/openambit/src/libambit/sbem0102.h: 38

# No inserted files

