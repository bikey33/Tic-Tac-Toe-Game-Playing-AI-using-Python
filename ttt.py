cell=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
def IsSpaceFree(pos):
    return cell[pos]== ' '
def get_input(sign):
    ch=input('Enter the Cell No where you want to place your sign (1-9)')
    try:
        a=int(ch)
        if (a<9  and a>0):
            if IsSpaceFree(a-1):
                cell[a-1]=sign
            else: print("You requested already occupied position")
        else: print("Invalid Position number")
    except:
        print("Please Type a number")


def print_game():
    for i in range(0,3):
            print(cell[3*i] + " | "+cell[3*i+1]+" | "+ cell[3*i+2])
            print("--------")
def IsboardFull(c):
    if cell.count(' ') > 1:
        return False
    else:
        return True
def Gameover(c,sg):
    result= ((c[0]==sg and c[1]==sg and c[2]==sg)
            or (c[3] == sg and c[4] == sg and c[5] == sg) or
            (c[6] == sg and c[7] == sg and c[8] == sg) or
            (c[0] == sg and c[3] == sg and c[6] == sg) or
            (c[1] == sg and c[4] == sg and c[7] == sg) or
            (c[2] == sg and c[5] == sg and c[8] == sg) or
            (c[0] == sg and c[4] == sg and c[8] == sg) or
            (c[2] == sg and c[4] == sg and c[6] == sg))

    if(result):
        return sg
    else:
        y="N"
        return y
def X_turn(c):
    count_X=c.count("X")
    count_0=c.count("0")
    if(count_X==count_0):
        return (True)
    elif(count_X>count_0):
        return(False)
def Check_Center(p,c):
    check_list=c
    list_as_set= set(p)
    intersection = list_as_set.intersection(check_list)
    inter_list=list(intersection)
    return inter_list
def computer():
    #Determine all sets of possible moves
    #Find out values of each possible moves
    #Select  a move to that  maximizes the winning situations of Computer
    #Use min max algorithm

    possible_move = []
    for i in range(1, 9):
        if (cell[i] == ' '):
            possible_move.append(i)
    cell_copy= cell[:]
    print(possible_move)
    print(possible_move.count(5))

    for move in possible_move:
        cell_copy[move]='O'
        if (Gameover(cell_copy, "0") == "0") or (Gameover(cell_copy, "X")):
            cell[move]= '0'
            break

        if (possible_move.count(5) > 0):
            #Center move
            cell[5]='0'
            print("5 is available")
            break
        if len(Check_Center(possible_move,[2,4,6,8]))>0:
            import random
            index=random.randint(1,len(Check_Center(possible_move,[2,4,6,8]))+1)
            cell[2*index]= '0'
            print(index)
            break
        if(len(Check_Center(possible_move,[1,3,7,9]))>0):
            #corner piece
            import random
            list= Check_Center(possible_move, [1, 3, 7, 9])
            index = random.randint(1, len(list + 1))
            x=list[index-1]
            cell[x] = '0'
            break
    print('computer placed an \'0\' in position', move)
    print(cell)


def main():
    print("Welcome to Tic Tac Toe")
    print_game()
    sgn= "X"
    print("It's X's Turn")
    get_input(sgn)
    print_game()
    while not (IsboardFull(cell)):
        if(X_turn(cell)):
            sgn = "X"
            if (Gameover(cell, "0") == "0"):
                print('Sorry Computer won the game this time.')
                break

            print("X's Turn")
            get_input(sgn)
            print_game()
        elif not (X_turn(cell)):
            sgn = "0"
            if (Gameover(cell, "X") == "X"):
                print('Congratulations Player X,you won the game.')
                break
            print("Computer's turn")
            computer()
            print_game()
        if IsboardFull(cell):
            print("Game is draw.Play Again.")
            break
main()
#computer()