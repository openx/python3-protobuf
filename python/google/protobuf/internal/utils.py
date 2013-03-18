
try:
    import cmp
except ImportError:
    #No cmp function available, probably Python 3
    def cmp(a, b):
        return (a > b) - (a < b)



def bytestr_to_string(bytestr):
    return unicode(bytestr, 'utf-8')

def string_to_bytestr(string):
    #return b''.join([chr(b) for b in string.encode('utf-8')])
    return string.encode('utf-8')


def byte_ord(bytes):
    return ord(bytes)

def char_byte(char):
    return char

