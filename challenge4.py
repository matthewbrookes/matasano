import ChallengeUtils
import EnglishUtils

cipher_file = open("challenge-data/4.txt", "r")
best_score = -100
best_guess = ''
for line in cipher_file:
    guess = ChallengeUtils.guess_single_character_xor(line.rstrip())
    score = EnglishUtils.score_word(guess)
    if score > best_score:
        best_score = score
        best_guess = guess
cipher_file.close()
print(best_guess)
