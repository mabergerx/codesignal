from itertools import groupby

def solution(s):
    letter_substrings = [''.join(g) for _, g in groupby(s)]
    letter_encodings = []
    for letter_sub in letter_substrings:
        if len(letter_sub) > 1:
            letter_encoding = f"{len(letter_sub)}{letter_sub[0]}"
        else:
            letter_encoding = letter_sub[0]
        letter_encodings.append(letter_encoding)
    
    return "".join(letter_encodings)