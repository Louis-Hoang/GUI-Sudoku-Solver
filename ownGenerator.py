from random import randint, shuffle

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

board = []
for i in range (9):
    board.append([0 for i in range(9)])

def checkGrid(board):
  for row in range(len(board)):
      for col in range((len(board[0]))):
        if board[row][col]==0:
          return False 
  return True 

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


def solveGrid(board):
    global counter
    for i in range(0,81): #Find next empty cell
        row=i // 9
        column=i % 9
        if board[row][column]==0:
            for i in range(1,10):
                if check_valid(board,i,(row,column)):
                    board[row][column] = i
                    if checkGrid(board):
                        counter+=1
                        break
                    else:
                        if solveGrid(board):
                            return True
            break
    board[row][column] = 0 #reset the entry 

numberList=[i for i in range(1,10)]

def fillGrid(board):
    global counter
    for i in range(0,81):
        row=i // 9
        column=i % 9
        if board[row][column]==0:
            shuffle(numberList)      
            for value in numberList:
                if check_valid(board,value,(row,column)):
                    board[row][column] = value
                    if checkGrid(board):
                        return True
                    else:
                        if fillGrid(board):
                            return True            
            break
    board[row][column] = 0 #reset the entry 

fillGrid(board)

attempts = 5 
counter=1
while attempts>0:
  #Select a random cell that is not already empty
  row = randint(0,8)
  col = randint(0,8)
  while board[row][col]==0:
    row = randint(0,8)
    col = randint(0,8)
  #Remember its cell value in case we need to put it back  
  backup = board[row][col]
  board[row][col]=0
  
  #Take a full copy of the grid
  copyGrid = []
  for r in range(0,9):
     copyGrid.append([])
     for c in range(0,9):
        copyGrid[r].append(board[r][c])
  
  #Count the number of solutions that this grid has (using a backtracking approach implemented in the solveGrid() function)
  counter=0      
  solveGrid(copyGrid)   
  #If the number of solution is different from 1 then we need to cancel the change by putting the value we took away back in the grid
  if counter!=1:
    board[row][col]=backup
    #We could stop here, but we can also have another attempt with a different cell just to try to remove more numbers
    attempts -= 1

print_board(board)