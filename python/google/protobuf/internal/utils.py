
try:
    import cmp
except ImportError:
    #No cmp function available, probably Python 3
    def cmp(a, b):
        return (a > b) - (a < b)

