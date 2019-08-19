import numpy as np

def matrixElementsSum(matrix):
    np_matrix = np.matrix(matrix)
    
    total_sum = 0
    
    for column in np_matrix.T:

        column = [item for sublist in column.tolist() for item in sublist]
        
        try:
            zero_index = column.index(0)
            sum_per_column = sum(column[:zero_index])
            total_sum += sum_per_column
        except:
            sum_per_column = sum(column)
            total_sum += sum_per_column
    
    return total_sum