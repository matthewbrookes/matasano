from utils import Bitwise as Bitwise
from utils import ChallengeUtils as ChallengeUtils
from utils import EnglishUtils as EnglishUtils
from queue import PriorityQueue
from base64 import b64decode, b16encode, b16decode

def queue_hamming_distances(hex_string):
    queue = PriorityQueue()
    for keysize in range(2, 40):
        byteset1 = hex_string[0: 4*keysize]
        byteset2 = hex_string[4*keysize: 8*keysize]
        hamming_distance = ChallengeUtils.hamming_distance_hex(byteset1,
                                                               byteset2)
        hamming_distance_normalised = hamming_distance / keysize
        queue.put((hamming_distance_normalised, keysize))
    return queue

def main():
    encrypted_file = open('./challenge-data/6.txt')
    encrypted_base64 = encrypted_file.read().rstrip()
    encrypted_file.close()
    encrypted_hex_bytes = b16encode(b64decode(encrypted_base64))
    queue = queue_hamming_distances(encrypted_hex_bytes.decode())

    best_guess = ''
    best_score = -100000

    for i in range(2):
        # Trying two most probable keysizes
        (_, keysize) = queue.get()
        # Create blocks of keysize bytes
        blocks = [encrypted_hex_bytes[j:j+(2*keysize)]
                    for j in range(0, len(encrypted_hex_bytes), 2*keysize)]
        potential_key = ''
        for j in range(keysize):
            # Create transposed block
            block_string = bytes()
            for k in range(len(blocks)):
                block_string += blocks[k][2*j:2*(j+1)]
            c = ChallengeUtils.single_character_most_english_xor(block_string)
            potential_key += chr(c)
        potential_plaintext_hex = Bitwise.repeat_key_XOR(encrypted_hex_bytes,
                                                    potential_key)
        potential_plaintext = b16decode(potential_plaintext_hex, True).decode()
        score = EnglishUtils.score_word(potential_plaintext)
        if score > best_score:
            best_score = score
            best_guess = potential_plaintext

    return best_guess

if __name__ == "__main__":
    print(main())
