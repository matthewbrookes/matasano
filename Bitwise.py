import base64
def fixedXOR(hex1, hex2):
    '''Returns the XOR of two ASCII representations of hex strings'''
    raw1 = base64.b16decode(hex1, True)
    raw2 = base64.b16decode(hex2, True)
    hex_sum_as_int = 0
    for (x,y) in zip (raw1, raw2):
        hex_sum_as_int *= (16*16)
        hex_sum_as_int += x^y
    return "{0:0{1}x}".format(hex_sum_as_int, len(hex1))

def repeat_key_XOR(hex_rep_plaintext, key):
    ''' Returns encrypted form of hex plaintext using the key for repeat XOR '''
    cipher_text = ''
    key_index = 0
    bytes_in_hex_rep_plaintext = [
        hex_rep_plaintext[i: i+2] for i in range(0, len(hex_rep_plaintext), 2)
    ]
    for byte in bytes_in_hex_rep_plaintext:
        key_char = key[key_index]
        hex_rep_key_char = base64.b16encode(key_char.encode())
        xor = fixedXOR(hex_rep_key_char, byte)
        cipher_text += xor
        key_index += 1
        if key_index == len(key):
            key_index = 0
    return cipher_text
