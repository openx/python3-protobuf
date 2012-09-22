
def cmp(a, b):
    return (a > b) - (a < b)

def bytes_to_string(byte_array):
    return ''.join([chr(b) for b in byte_array])
    #return byte_array.decode('utf-8')

def string_to_bytes(text):
    return bytes([ord(c) for c in text])
    #return text.encode('utf-8')

def bytestr_to_string(bytestr):
    return bytes([ord(c) for c in bytestr]).decode('utf-8')

def string_to_bytestr(string):
    return ''.join([chr(b) for b in string.encode('utf-8')])
