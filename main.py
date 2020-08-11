CHARSET = '''0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()`~-=_+[]\{}|;':",./<>? '''

def idontknowwhattonamethisfunction(length, inputs):
    a = [0] * length
    b = [CHARSET.index(c) for c in ''.join(inputs)]
    ba = len(b)
    d = len(CHARSET)
    c = ((sum(b) ** 2) + (length ** 3)) % d
    for i in range(max(ba, length)):
        bc = b[i % ba]
        a[i % length] += (bc + c)
        c += (bc ** 2) % d
    return ''.join([CHARSET[cc % d] for cc in a])
