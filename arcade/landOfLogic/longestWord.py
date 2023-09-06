def solution(text):
    # Use regular expression to find all words (sequences of alphabets)
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    # Sort the words by length and return the longest one
    return sorted(words, key=len, reverse=True)[0]