def solution(time):
    first_part, last_part = time.split(":")
    return not (int(first_part) > 23 or int(last_part) > 59)