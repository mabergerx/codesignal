def solution(n):
    
    if n < 10:
        return 0
    
    count = 0
    
    def recursively_solve(number, count=count):
        count += 1
        string_representation = str(number)
        sum_digits = sum([int(digit) for digit in string_representation])
        if sum_digits > 9:
            return recursively_solve(sum_digits, count)
        else:
            return count
    
    return recursively_solve(n)