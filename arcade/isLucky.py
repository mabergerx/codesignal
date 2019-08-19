def isLucky(n):
    
    string_representation = str(n)
    
    first_half = sum([int(i) for i in string_representation[:int(len(string_representation)/2)]])
    second_half = sum([int(i) for i in string_representation[int(len(string_representation)/2):]])
    
    return first_half == second_half