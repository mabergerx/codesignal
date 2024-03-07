import re

def solution(inputString):
    digits = re.findall(r'\d+', inputString)
    digits_as_ints = [int(digit) for digit in digits]
    return sum(digits_as_ints)

