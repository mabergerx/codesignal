def allLongestStrings(inputArray):
    longest_length = max([len(item) for item in inputArray])
    
    return [item for item in inputArray if len(item) == longest_length]