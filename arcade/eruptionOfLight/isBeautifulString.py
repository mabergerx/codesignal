from collections import Counter

def solution(inputString):
    c = sorted(Counter(inputString).most_common())
    for index, (letter, count) in enumerate(c):
        try:
            if count < c[index+1][1]:
                return False
        except IndexError:
            pass
    return True