import itertools
import nltk

def solution(inputArray):
    
    def check_for_one(value, next_value):
        return nltk.edit_distance(value, next_value) == 1
                
    r = len(inputArray)
    
    possible_rearrangements = list(itertools.permutations(inputArray, r))
    
    for rearrangement in possible_rearrangements:
        distances_rearrangement = []
        for index, value in enumerate(rearrangement):
            if index != len(rearrangement)-1:
                distances_rearrangement.append(check_for_one(value, rearrangement[index+1]))
        if all(distances_rearrangement):
            return True
    return False