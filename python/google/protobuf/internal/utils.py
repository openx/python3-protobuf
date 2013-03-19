from __future__ import unicode_literals

try:
    import cmp
except ImportError:
    #No cmp function available, probably Python 3
    def cmp(a, b):
        return (a > b) - (a < b)

def bytes_to_string(byte_array):
    return ''.join([b for b in byte_array])

def string_to_bytes(text):
    return b"".join([c for c in text])

def bytestr_to_string(bytestr):
    return unicode(bytestr, 'utf-8')

def string_to_bytestr(string):
    #return b''.join([chr(b) for b in string.encode('utf-8')])
    return string.encode('utf-8')

def byte_ord(bytes):
    return ord(bytes)

def char_byte(char):
    return char

def bytestr(val):
    """Pass in an integer val"""
    return chr(val)

