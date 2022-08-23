def solution(inputArray, k):
    sums = []
    for i in range(len(inputArray) - k + 1):
        sums.append(sum(inputArray[i: i + k]))
    return max(sums)