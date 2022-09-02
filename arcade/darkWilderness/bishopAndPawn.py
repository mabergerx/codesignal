def solution(bishop, pawn):
    
    bishop_row = int(bishop[1])
    bishop_column = ord(bishop[0]) - 96 # Get the index of the letter
    
    pawn_row = int(pawn[1])
    pawn_column = ord(pawn[0]) - 96
    
    row_difference = abs(bishop_row - pawn_row)
    column_difference = abs(bishop_column - pawn_column)
    
    return row_difference == column_difference