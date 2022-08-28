def solution(inputString):
    prefix = []
    inputString_list = list(inputString)
    
    def recursive_pop(inputString_list, prefix):
        for index, el in enumerate(inputString_list):
            if el.isdigit():
                prefix.append(el)
                del inputString_list[index]
                recursive_pop(inputString_list, prefix)
                if len(prefix) == len(inputString):
                    return "".join(prefix)
            else:
                return "".join(prefix)
    
    return recursive_pop(inputString_list, prefix)