def almostIncreasingSequence(sequence):
    
    to_remove = []
    # highest_yet = -10**6

    for index, i in enumerate(sequence):
        try:
            if i >= sequence[index+1]:
                to_remove.append(i)
            else:
                continue
        except:
            continue
    # for i in sequence:
    #     if i > highest_yet:
    #         highest_yet = i
    #     else:
    #         to_remove.append(i)

    print(to_remove)

    return len(to_remove) <= 1

print(almostIncreasingSequence([1, 1, 1, 2, 3])) #true
