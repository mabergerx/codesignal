def arrayMaximalAdjacentDifference(inputArray):
    pairwise = [(inputArray[i], inputArray[i+1]) for i in range(len(inputArray)-1)]
    max_diff = max([abs(first-second) for first, second in pairwise])
    return max_diff