import base64
def hex2base64(hex):
    '''Converts an ASCII string in hex to it's base64 representation'''
    raw = base64.b16decode(hex, True)
    return base64.b64encode(raw)

