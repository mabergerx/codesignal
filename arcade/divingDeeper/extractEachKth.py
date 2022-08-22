def solution(inputArray, k):
    return [el for index, el in enumerate(inputArray) if (index+1) % k != 0]