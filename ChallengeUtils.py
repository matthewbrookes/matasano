import EnglishUtils
import Bitwise


def guess_single_character_xor(hex_string):
    ''' Returns the best guess of xoring hex_string with a character '''
    best_guess = hex_string
    best_score = -100
    for i in range(256):
        digit_as_hex_string = "{0:0{1}x}".format(i, 2)
        # Split hex string into individual bytes
        bytes_in_hex = [
            hex_string[i: i+2] for i in range(0, len(hex_string), 2)
        ]
        characters = ''
        for byte in bytes_in_hex:
            char = bitwise.fixedXOR(byte, digit_as_hex_string)
            characters += chr(int(char, 16))
        score = EnglishUtils.score_word(characters)
        if score > best_score:
            best_score = score
            best_guess = characters
    return best_guess
