cell=[' ',' ',' ',' ',' ',' ',' ',' ',' '] # List holding all the signs and represents board conditons

def IsSpaceFree(pos):
    # Checks If the space in board is free
    return cell[pos]== ' '


def get_input(sign):
    # Get Input from the User
    ch=input('Enter the Cell Number where you want to place your sign (1-9)')
    try:
        a=int(ch)
        if (a<=9  and a>0):
            if IsSpaceFree(a-1):
                cell[a-1]=sign
            else: print("You requested already occupied position")
        else: print("Invalid Position number")
    except:
        print("Please Type a number\n")


def print_game():
    # print game text to console
    for i in range(0,3):
            print(cell[3*i] + " | "+cell[3*i+1]+" | "+ cell[3*i+2])
            print("__________")


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


def Check_intersection(p,c):
    #To check if the given list of possible moves contain specific corner pieces or central pieces by evaluating intersection
    check_list=c
    list_as_set= set(p)
    intersection = list_as_set.intersection(check_list)
    inter_list=list(intersection)
    return inter_list


def computer():
    # Determine all sets of possible moves
    # Find out values of each possible moves
    # Select  a move to that  maximizes the winning situations of Computer
    # Use min max algorithm

    possible_move = []
    for i in range(0, 9):# Finding out available valid moves
        if (cell[i] == ' '):
            possible_move.append(i)
    print(possible_move)
    flag = False
    # Checking whether the next move is winning and losing
    # If that the case make moves accordingly
    for move in possible_move:
        cell_copy = cell[:]
        cell_copy_forX = cell[:]
        cell_copy[move] = '0'
        cell_copy_forX[move]= 'X'
        #print(cell_copy)
        Checkwinning = (Gameover(cell_copy, "0") == "0")
        CheckLosing = (Gameover(cell_copy_forX, "X") =="X")

        if Checkwinning:
            # If winning finish the game
            cell[move] = '0'
            flag = True
            print('computer placed an \'0\' in position', move)
            break

        elif CheckLosing:
            # If Losing Prevent the loss
            cell[move] = '0'
            flag= True
            print('computer placed an \'0\' in position', move)
            break

    if(not flag):
        # If the next moves are not winning or losing play casually
        if(possible_move.count(4) > 0):
            #If the central position i.e 5 is available, place there
           #Checking at corner piece
            cell[4] = '0'

        else:
            if len(Check_intersection(possible_move,[1,3,5,7]))>1:
                #Placing at Corners
                import random
                #Generating random integer between 1 to select moves among available center peices
                list= Check_intersection(possible_move, [1,3,5,7])
                if(len(list)<1):
                    x=list[0]
                else:
                    index=random.randint(0,len(list)-1)
                    x = list[index]
                cell[x] = '0'
                print('computer placed an \'0\' in position', 2*index+1)


            elif (len(Check_intersection(possible_move, [0, 2, 6, 8])) > 1):
                # Placing at middle Piece
                import random
                list = Check_intersection(possible_move, [0, 2, 6, 8])
                if (len(list) < 1):
                    x = list[0]
                else:
                    index = random.randint(0, len(list) - 1)
                    x = list[index]
                cell[x] = '0'
                print('\ncomputer placed an \'0\' in position')


def main():

    print("Welcome to Tic Tac Toe \n")
    print_game()
    sgn= "X"
    print("\nIt's X's Turn")
    get_input(sgn)
    print_game()

    while not (IsboardFull(cell)):
        if(X_turn(cell)):
            sgn = "X"
            if (Gameover(cell, "0") == "0"):
                print('\nSorry Computer won the game this time.')
                break

            print("\nX's Turn")
            get_input(sgn)
            print_game()

        if not (X_turn(cell)):
            sgn = "0"
            if (Gameover(cell, "X") == "X"):
                print('\nCongratulations Player X,you won the game.')
                break
            print("\nComputer's turn")


            computer()
            print_game()


    if IsboardFull(cell):
        print("\nGame is draw.Play Again.")

# Calling the main function
main()
#computer()