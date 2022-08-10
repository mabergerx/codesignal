def solution(a, b):
    if a == b:
        return True
    elif sorted(a) == sorted(b):
        amount_swaps = 0
        for ela, elb in zip(a, b):
            if ela != elb:
                amount_swaps += 1
            if amount_swaps > 2:
                return False
        return True
    return False