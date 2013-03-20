"""
This module abstracts all the bytes<-->string conversions so that the python 2
and 3 code everywhere else is similar.  This also has a few simple functions
that deal with the fact that bytes are different between the 2 versions even
when using from __future__ import unicode_literals.  For example:
Python 2:
    b'mybytes'[0] --> b'm' (type str)
Python 3:
    b'mybytes'[0] --> 109 (type int)
So in some places we get an index of a bytes object and we have to make sure
the behaviour is the same in both versions of python so functions here take
care of that.
"""

try:
    import cmp
except ImportError:
    #No cmp function available, probably Python 3
    def cmp(a, b):
        return (a > b) - (a < b)

def string_to_bytes(text):
    """
    Convert a string to a bytes object.  This is a raw conversion
    so that ord() on each element remains unchanged.
    Input type: string
    Output type: bytes
    """
    return bytes([ord(c) for c in text])

def bytes_to_string(byte_array):
    """
    Inverse of string_to_bytes.
    """
    return ''.join([chr(b) for b in byte_array])

def string_to_bytestr(string):
    """
    Convert a string to a bytes object.  This encodes the object as well which
    will typically change ord on each element & change the length (i.e. 1 char
    could become 1/2/3 bytes)
    """
    return string.encode('utf-8')

def bytestr_to_string(bytestr):
    """
    Inverse of string_to_bytestr.
    """
    return bytes([c for c in bytestr]).decode('utf-8')

def byte_ord(bytes):
    """
    This converts a *single* input byte to an integer.  Usually used in
    conjuction with b'mybytes'[i].  See module description.
    Input: 2: string/pseudo-bytes 3: int
    Output: int
    """
    return bytes

def char_byte(char):
    """
    Convert a *single* byte to an int.  Usually used like char(b'm').  See
    module description.
    Input: 2: string/pseudo-bytes 3: bytes
    Output: 2: string/pseudo-bytes 3: int
    """
    return ord(char)

def bytestr(val):
    """
    Convert a *single* integer to a bytes object.  Usually used like
    bytestr(int).
    Input: int
    Output: bytes
    """
    return bytes([val])

def single_byte(byte_val):
    """
    Convert a *single* byte to a byte.  This is usually used in conjuction with
    b'mybytes'[i].  See module description.
    Input: 2: string/pseudo-bytes 3: int
    Output: bytes
    """
    return bytestr(byte_val)

