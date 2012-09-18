
def cmp(a, b):
    return (a > b) - (a < b)


def bytes_to_string(byte_array):
    #return ''.join([chr(b) for b in byte_array])
    return byte_array.decode('latin-1')


def string_to_bytes(text):
    #return bytes([ord(c) for c in text])
    return text.encode('latin-1')

