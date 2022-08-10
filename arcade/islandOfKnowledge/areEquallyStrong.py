def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    you = yourLeft+yourRight
    friend = friendsLeft+friendsRight
    you_strongest = max(yourLeft, yourRight)
    friend_strongest = max(friendsLeft, friendsRight)
    you_weakest = min(yourLeft, yourRight)
    friend_weakest = min(friendsLeft, friendsRight)
    
    return you==friend and you_strongest==friend_strongest and you_weakest==friend_weakest