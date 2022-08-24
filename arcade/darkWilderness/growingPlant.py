def solution(upSpeed, downSpeed, desiredHeight):
    if desiredHeight <= upSpeed:     
            return 1
    else:
        height = 0
        days = 0
        while True:
            days += 1
            height = height + upSpeed
            if height >= desiredHeight:
                return days
            height = height - downSpeed
            if height >= desiredHeight:
                return days - 1