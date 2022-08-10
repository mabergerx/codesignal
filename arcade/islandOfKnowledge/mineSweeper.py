def solution(matrix):
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            l = -matrix[i][j]
            for x in [-1,0,1]:
                for y in [-1,0,1]:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[i]):
                        l += matrix[i + x][j + y]
            result[i].append(l)
    return result