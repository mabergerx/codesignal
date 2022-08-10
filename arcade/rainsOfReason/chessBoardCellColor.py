import string

def solution(cell1, cell2):
    rowtype_1 = ["black", "white"]*4
    rowtype_2 = ["white", "black"]*4
    
    board = [
            rowtype_1,
            rowtype_2,
            ]*4
    
    cell1_row_index = int(cell1[1])-1
    cell1_column_index = string.ascii_uppercase.index(cell1[0])-1
    cell1_color = board[cell1_row_index][cell1_column_index]
    
    cell2_row_index = int(cell2[1])-1
    cell2_column_index = string.ascii_uppercase.index(cell2[0])-1
    cell2_color = board[cell2_row_index][cell2_column_index]
    
    return cell1_color == cell2_color