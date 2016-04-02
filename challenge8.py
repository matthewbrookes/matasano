import base64

def main():
    cipher_file = open("./challenge-data/8.txt")
    lowest_differing_words = 80
    aes_string = ''
    for line in cipher_file:
        frequencies = dict()
        hex_line = base64.b16decode(line.rstrip(), True)
        for i in range(0, len(hex_line), 2):
            sixteenbits = hex_line[i:i+2]
            hex_string = base64.b16encode(sixteenbits)
            frequencies[hex_string] = frequencies.get(hex_string, 0) + 1
        if len(frequencies) < lowest_differing_words:
            lowest_differing_words = len(frequencies)
            aes_string = line
    cipher_file.close()
    return aes_string.rstrip()

if __name__ == "__main__":
    print(main())
