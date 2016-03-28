import base64
def fixedXOR(hex1, hex2):
    '''Returns the XOR of two ASCII representations of hex strings'''
    raw1 = base64.b16decode(hex1, True)
    raw2 = base64.b16decode(hex2, True)
    hex_sum_as_int = 0
    for (x,y) in zip (raw1, raw2):
        hex_sum_as_int *= (16*16)
        hex_sum_as_int += x^y
    return format(hex_sum_as_int, 'x')
