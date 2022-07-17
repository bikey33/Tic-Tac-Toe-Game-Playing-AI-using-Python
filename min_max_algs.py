# A function to implement Min-Max Algorithm
# I have put all the board conditions to a list called cell so cell = board
cell=[' ','X',' ',' ','X',' ','X','0','0'] # List holding all the signs and represents board conditons

def IsboardFull(c):
    # Checks if the Board is Full
    if cell.count(' ') > 0:
        return False
    else:
        return True


def Gameover(c,sg):
    # Check if the Game has been over or not
    result= ((c[0]==sg and c[1]==sg and c[2]==sg)
            or (c[3] == sg and c[4] == sg and c[5] == sg) or
            (c[6] == sg and c[7] == sg and c[8] == sg) or
            (c[0] == sg and c[3] == sg and c[6] == sg) or
            (c[1] == sg and c[4] == sg and c[7] == sg) or
            (c[2] == sg and c[5] == sg and c[8] == sg) or
            (c[0] == sg and c[4] == sg and c[8] == sg) or
            (c[2] == sg and c[4] == sg and c[6] == sg))

    if(result):
        return sg #Return the winner's sign
    else:
        y="N" # Other wise return "N" indicating no-one won
        return y


def X_turn(c):
    # Determine Player's turn
    count_X=c.count("X") # Count Number of X's on board
    count_0=c.count("0")
    if(count_X==count_0):

        return (True) # If X's turn return True
    elif(count_X>count_0):
        print("Not X's Turn")
        return(False)

def isMaximizingPlayer():
    return not X_turn(cell)

def FindScore(cell):
    sg = 'X'
    # Defining Terminal state, if computer win return 1
    # if computer lose in current board state, return -1
    # If current board is draw --> 0
    if not (Gameover(cell, 'X') == "N") or (Gameover(cell, '0') == "N") :
        if (Gameover(cell, '0') == "0"):
            return 1
        if (Gameover(cell, 'X') == "X"):
            return -1
    else:
        if (IsboardFull(cell)):
            return 0

# 'O' is maximizing player
def PossibleMoveFinder(cell):

    possible_move = []
    for i in range(0, 9):  # Finding out available valid moves
        if (cell[i] == ' '):
            possible_move.append(i)
    print(possible_move)
    return possible_move

def Min_Max(board,depth,Maximizer):

    possible_move = PossibleMoveFinder(cell)
    score = FindScore(board)
   # Checking if the current board position is terminal state.
    # If so return final score
    if score == -1:
        return score
    if score == 1:
        return score
    if (score == 0):
        return score

    # If not terminal state, Whose turn is this?
    if Maximizer: #If computer's turn(maximizer)

        best = -100
        for move in possible_move:
            board[move] = '0'
            # Minmax Recurssive call
            best = max(best,Min_Max(cell,depth + 1, not Maximizer))
            # Undo the current move
            board[move] = ' '

        return best
    # IF the minimizer's turn
    else:
        best = 100
        for move in possible_move:
            board[move] = 'X'
            # Minmax Recurssive call
            best = min(best, Min_Max(cell, depth + 1, not Maximizer))
            # Undo the current move
            board[move] = ' '

        return best


def BestMoveFinder(cell):
    bestValue = -100
    bestmove = -1
    possible_move = PossibleMoveFinder(cell)
    for move in possible_move:

        cell [move] = '0'
        # Finding out utility of all possible moves
        utility = Min_Max(cell,0,False)
        print ("Utility of Move", move, " is ", utility)
        cell [move] = ' ' # Undo

        # If the move has better utility update the bestval
        if utility > bestValue:
            bestmove = move
            bestValue = utility
    print("The best possible move is:", bestmove)
    print("Corrosponding move value is:",bestValue)
    return bestmove



if __name__ == '__main__':
    BestMoveFinder(cell)
    print(cell)