def solution(value1, weight1, value2, weight2, maxW):
    if weight1 > maxW and weight2 > maxW:
        return 0
    elif weight1 + weight2 <= maxW:
        return value1+value2
    if value1 >= value2:
        highest_value={"weight": weight1, "value": value1}
        low_value = {"weight": weight2, "value": value2}
    else:
        highest_value={"weight": weight2, "value": value2}
        low_value = {"weight": weight1, "value": value1}
    if highest_value["weight"] > maxW:
        return low_value["value"]
    else:
        return highest_value["value"]  
