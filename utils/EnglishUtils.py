def score_word(word):
    ''' 
    Assigns a score to the english-like characteristics of a word
    Each English feature adds to the score
    '''
    score = 0
    index = 0
    frequencies = dict()
    for char in word:
        # Update character frequency definition
        frequencies[char] = frequencies.get(char, 0) + 1
        # Check Q/q U/u sequence
        if (char == 'Q' or char == 'q') and index < len(word) - 1:
            if word[index + 1] == 'U' or word[index + 1] == 'u':
                score += 1
            else:
                score -= 1
        # Check apostrophe followed by s/l/d/<space>
        if char == '\'' and index < len(word) - 1:
            letters_after_apostrophe = {'s', 'l', 'd', ' '}
            if word[index + 1] in letters_after_apostrophe:
                score += 1
            else:
                score -= 1
        # Reduce score if word contains weird character
        if(isinstance(char, str)
                and not char.isalpha()
                and char not in {'\'', ' ', ':', ';'}):
            score -= 1
        index += 1
    # Increase score if first letter is capital
    if isinstance(word[0], str) and word[0].isupper():
        score += 1
    # More than half of all words end in E,T,D,S check for this
    last_letter = word[-1:]
    if last_letter.upper() in {'E', 'T', 'D', 'S'}:
        score += 1
    # Check frequencies in word
    e_frequency = frequencies.get('e', 0)
    if (e_frequency / len(word) > 0.12):
        score += 1
    t_frequency = frequencies.get('t', 0)
    if (t_frequency / len(word) > 0.09):
        score += 1
    a_frequency = frequencies.get('a', 0)
    if (a_frequency / len(word) > 0.08):
        score += 1
    o_frequency = frequencies.get('o', 0)
    if (o_frequency / len(word) > 0.07):
        score += 1
    i_frequency = frequencies.get('i', 0)
    if (i_frequency / len(word) > 0.07):
        score += 1
    s_frequency = frequencies.get('s', 0)
    if (s_frequency / len(word) > 0.06):
        score += 1

    return score
