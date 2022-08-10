def solution(name):
    if name[0].isdigit():
        return False
    
    def is_element_legit(element):
        if element.isalpha():
            return True
        elif element.isdigit():
            return True
        elif element == "_":
            return True
        return False
        
    return all([is_element_legit(el) for el in name])