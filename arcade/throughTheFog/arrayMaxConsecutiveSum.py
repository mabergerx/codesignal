# def solution(inputArray, k):
#     sums = [sum(inputArray[i: i + k]) for i in range(len(inputArray)-k+1)]
#     return max(sums)
# Passes all but 20th test because of run time limitation.

def solution(inputArray, k):
    total = result = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        total += inputArray[i + k] - inputArray[i]
        result = max(result, total)
    return result