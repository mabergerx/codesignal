def solution(upSpeed, downSpeed, desiredHeight):
    height = 0
    days = 0
    while True:
        days += 1
        height = height + upSpeed
        if height >= desiredHeight:
            return days
        height = height - downSpeed
        if desiredHeight <= upSpeed:     
            if height <= desiredHeight:
                return days
        else:
            if height >= desiredHeight:
                return days - 1
                