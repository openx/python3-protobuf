
try:
    import cmp
except ImportError:
    #No cmp function available, probably Python 3
    def cmp(a, b):
        return (a > b) - (a < b)

def bytes_to_string(byte_array):
    return ''.join([chr(b) for b in byte_array])
    #return byte_array.decode('utf-8')

def string_to_bytes(text):
    return bytes([ord(c) for c in text])
    #return text.encode('utf-8')

def bytestr_to_string(bytestr):
    #print ("C %s %s" % (bytestr, type(bytestr)))
    return bytes([c for c in bytestr]).decode('utf-8')

def string_to_bytestr(string):
    #return b''.join([chr(b) for b in string.encode('utf-8')])
    return string.encode('utf-8')

def byte_ord(bytes):
    return bytes

def char_byte(char):
    return ord(char)

def bytestr(val):
    """Pass in an integer val"""
    return bytes([val])

