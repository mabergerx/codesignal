def checkPalindrome(inputString):
    
    middleIndex = int(len(inputString)/2)
    
    if len(inputString) % 2:
        return inputString[middleIndex+1:] == inputString[:middleIndex][::-1]
    else:
        return inputString[middleIndex:] == inputString[:middleIndex][::-1]


print(checkPalindrome("aabaa")) #true
print(checkPalindrome("abac")) #false
print(checkPalindrome("a"))  #true
print(checkPalindrome("az")) #false

print(checkPalindrome("abacaba")) #true
print(checkPalindrome("z")) #true
print(checkPalindrome("aaabaaaa")) #false
print(checkPalindrome("zzzazzazz")) #false

print(checkPalindrome("hlbeeykoqqqqokyeeblh")) #true
print(checkPalindrome("hlbeeykoqqqokyeeblh")) #true