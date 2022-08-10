import math

def solution(year):
    
    century = math.ceil(year / 100)
    
    if not year % 100:
        return century
    else:
        return math.ceil(century)
