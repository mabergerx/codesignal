def solution(inputArray):
    start = 2
    init = 0
    while init < len(inputArray):
        current_obstacle = inputArray[init]
        if current_obstacle%start == 0:
            start+=1
            init = 0
        else:
            init+= 1
    return start