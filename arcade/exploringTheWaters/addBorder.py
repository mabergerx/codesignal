def solution(picture):
    firstRow = "*"*(len(picture[0])+2)
    middleRows = [f"*{row}*" for row in picture]
    middleRows.insert(0, firstRow)
    middleRows.append(firstRow)
    return middleRows
