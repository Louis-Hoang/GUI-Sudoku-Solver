sample =[]
for i in range (9):
    sample.append([0 for i in range(9)])


def print_board(board):
    '''
    
    Parameter: a list of list representation of 9x9 board
    Return value: None
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i!=0: #every three row (exclude the first)
             print("- - - - - - - - - -")    
    
        for j in range(len(board[0])):

            if j % 3 == 0 and j!=0: #every three column (exclude the first):
                print("|", end="") 
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def check_valid(board,num,loc):
    # check row
    for i in range(len(board[0])):
        if board[loc[0]][i] == num and loc[1] != i:
            return False
    
    # check column

    for i in range(len(board)):
        if board[i][loc[1]] == num and loc[0] != i:
            return False
    
    # check table 3x3

    box_x = loc[1] //3 #(box_x = 0|1|2)
    box_y = loc[0] //3 #(box_y = 0|1|2)

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == num and (i,j) != loc:
                return False 

    return True



def backtrack_solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, column = find 

    for i in range(1,10):
        if check_valid(board,i,(row,column)):
            board[row][column] = i

            if backtrack_solve(board):
                return True
        
            board[row][column] = 0 #reset the entry 

    return False 

print_board(sample)
backtrack_solve(sample)
print("___________________")
print_board(sample)