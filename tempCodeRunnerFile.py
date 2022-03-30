def solveGrid(board)
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