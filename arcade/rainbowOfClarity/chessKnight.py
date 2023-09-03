def solution(cell):
    
    if int(cell[1]) == 1:
        cell_row = 0
    else:
        cell_row = int(cell[1]) - 1
    
    cell_column = ord(cell[0]) - 97 # Get the index of the letter
    
    max_moves = 8


    # Every time the horse moves one row down from row 2, it loses 2 moves. Every time the horse moves one row up from row 5, it loses 2 moves.
    
    # Every time the horse moves one column to the left from column 2, it loses two 2 moves. Every time the horse moves one column to the right from column 5, it loses 2 moves.
    
    # But sometimes, the lost moves overlap. So maybe it's easier to eliminate moves. So, when the horse moves beyond column 2 to the left, it loses 2 moves, always. If it moves beyond column 1 to the left, it loses extra 2 moves. Because it goes out of bounds. Similarly, when the horse moves to the right beyond column 5, it loses 2 moves, and another 2 moves when it moves to the 7th column. 
    
    # So, to summarize: when the horse moves to column 1, it loses 2 moves on the left side. If it moves to column 0, it loses 2 more moves on the left. When the horse moves to column 6, it loses 2 moves on the right side, if it then moves to column 7, it loses 2 more on the right side.
    
    # The same logic applies to vertical movement. When the horse moves to row 1 it loses 2 moves to the downside, and then loses 2 more to the downside when it moves to row 0. When the horse moves to row 6, it loses 2 moves to the topside, and it loses 2 more to the topside when on row 7. 
    
    # What we have to figure out, are the overlapping moves.

    # So horse on position a1, which is row 0 and column 0. Because of row 0, it lost 4 moves to the downside. Because it is on column 0, it lost 4 moves to the left. But we know that if horse loses 4 moves on left, and 4 on the bottom, two are overlapping, so it actually only lost 2 extra moves. So then it lost 4 + 2 moves = 6. So it has 8 - 6 = 2 moves left.
    
    lost_left_moves = 0
    lost_right_moves = 0
    lost_downwards_moves = 0
    lost_upwards_moves = 0
     
    if cell_row == 1:
        lost_downwards_moves += 2
    elif cell_row == 0:
        lost_downwards_moves += 4
    elif cell_row == 6:
        lost_upwards_moves += 2
    elif cell_row == 7:
        lost_upwards_moves += 4
        
    if cell_column == 1:
        lost_left_moves += 2
    elif cell_column == 0:
        lost_left_moves += 4
    elif cell_column == 6:
        lost_right_moves += 2
    elif cell_column == 7:
        lost_right_moves += 4
        
    print(f"Lost downwards moves: {lost_downwards_moves}")
    print(f"Lost upwards moves: {lost_upwards_moves}")
    print(f"Lost left moves: {lost_left_moves}")
    print(f"Lost right moves: {lost_right_moves}")
    
    total_lost_moves = lost_downwards_moves + lost_right_moves + lost_upwards_moves + lost_left_moves
    
    print(f"Total lost before: {total_lost_moves}")
    
    if (lost_downwards_moves == 4 or lost_upwards_moves == 4) and (lost_left_moves == 4 or lost_right_moves == 4):
        total_lost_moves -= 2
    elif (lost_upwards_moves == 4 or lost_downwards_moves ==4) and (lost_left_moves == 2 or lost_right_moves == 2):
        total_lost_moves -= 1
    
    return max_moves - total_lost_moves
    