def solution(n):
    str_rep = list(str(n))
    
    all_possible_digits = []
    
   # What we want to do is to remove each of the digits in the str_rep once, and store all the possible combinations into a list.
   
    for digit in str_rep:
        list_without_digit = list(str_rep)
        list_without_digit.remove(digit)
        all_possible_digits.append(int("".join(list_without_digit)))
    
    return max(all_possible_digits)