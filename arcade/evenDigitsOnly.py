def solution(n):
    return all([not int(x) % 2 for x in str(n)])