from collections import Counter

def commonCharacterCount(s1, s2):
    all_chars_s1 = list(s1)
    all_chars_s2 = list(s2)

    c = list((Counter(all_chars_s1) & Counter(all_chars_s2)).elements())  
    
    return len(c)