def adjacentElementsProduct(inputArray):

    combis = zip(inputArray, inputArray[1:])

    return max([(t[0]*t[1]) for t in combis])


print(adjacentElementsProduct([3, 6, -2, -5, 7, 3])) # 21