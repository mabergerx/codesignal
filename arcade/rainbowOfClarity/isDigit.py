# def solution(symbol):
#     return symbol.isdigit()

# Another way
def solution(symbol):
    try:
        int(symbol)
        return True
    except:
        return False