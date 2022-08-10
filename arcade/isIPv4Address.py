def solution(inputString):
    if "" in inputString.split("."):
        return False
    if (sum([not char.isdigit() for char in inputString if char != "."]) > 0):
        return False
    if (len([ins for ins in inputString.split(".") if ins]) != 4):
        return False
    else:
        if (any([int(item) > 255 for item in inputString.split(".")])) or (any([item[0] == '0' for item in inputString.split(".") if len(item) > 1])):
            return False
    return True