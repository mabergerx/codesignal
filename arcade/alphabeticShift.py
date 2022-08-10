def solution(inputString):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    indeces = [alphabet.index(letter) for letter in inputString]
    
    return "".join([alphabet[i+1] if i != len(alphabet)-1 else "a" for i in indeces])