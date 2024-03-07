def solution(matrix):
    unique_squares = set()  # Use a set to store unique squares
    
    def matrix_to_tuple(matrix):
        """Converts a 2x2 matrix to a hashable tuple of tuples."""
        return tuple(tuple(row) for row in matrix)
    
    def extract_squares_from_two_rows(row1, row2):
        """Extract 2x2 squares from two rows."""
        squares = []
        for i in range(len(row1) - 1):
            square = [
                [row1[i], row1[i+1]],
                [row2[i], row2[i+1]]
            ]
            squares.append(matrix_to_tuple(square))  # Convert to tuple of tuples
        return squares
    
    for i in range(len(matrix) - 1):
        upper_row = matrix[i]
        lower_row = matrix[i+1]
        these_squares = extract_squares_from_two_rows(upper_row, lower_row)
        unique_squares.update(these_squares)  # Add new squares, ensuring uniqueness
    
    return len(unique_squares)
