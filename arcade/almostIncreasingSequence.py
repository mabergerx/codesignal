def almostIncreasingSequence(sequence):
    
    left_list = []
    right_list = []
    
    for index, i in enumerate(sequence[:-1]):
        if i >= sequence[index+1]:
            left_list.append(index)
            right_list.append(index+1)
        
        try:
            if i >= sequence[index+2]:
                left_list.append(index)
                right_list.append(index+2)
        except:
            continue
    
    return len(set(left_list)) <= 1 or len(set(right_list)) <= 1