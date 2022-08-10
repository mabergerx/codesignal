def solution(inputArray):

    moves = 0
    previouslyIncremented = inputArray[0]

    for index, _ in enumerate(inputArray):
        try:
            next_element = inputArray[index+1]
            if next_element <= previouslyIncremented:
                incrementSize = (previouslyIncremented - next_element)+1
                moves += incrementSize
                previouslyIncremented = incrementSize+next_element
            else:
                previouslyIncremented = next_element
        except IndexError:
            pass
    return moves