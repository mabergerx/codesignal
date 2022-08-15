def solution(a):
    
    def single_value(x, to_compare):
        return abs(to_compare - x)
    
    target_sums = dict()
    
    for number in a:
        a_without_number = [n for n in a if n != number]
        target_sum = 0
        for a_ in a_without_number:
            target_sum += single_value(number, a_)
        target_sums[number] = target_sum
    
    sorted_target_sums = dict(sorted(target_sums.items(), key=lambda item: item[1]))
    
    return list(sorted_target_sums.keys())[0]