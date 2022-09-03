def solution(inputString):
    groups = inputString.split("-")
    if len(groups) != 6:
        return False
    else:
        for group in groups:
            if len(group) != 2:
                return False
            if not all([el in "0123456789ABCDEF" for el in group]):
                return False
    return True
