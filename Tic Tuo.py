
#function display Board
def display(board):
    print('\n'*1)
    print('   |   |    ')
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print('   |   |    ')
    print("------------")

    print('   |   |    ')
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('   |   |    ')
    print("------------")

    print('   |   |    ')
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print('   |   |    ')

#function to choice which player is x and o
def player_iput():
    marker=''
    while  not (marker == "x" or marker == "o"):
     marker=input("Player 1 choose X or O ").upper()

     if marker == "x".upper():
        return ("X","O")
     else:
        return ("O","X")

#function to replace my pos with x or o
def place_marker(board,marker,pos):
    board[pos]= marker

#function that check who is winer return true or false
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal

#function to choice random wich player play first
def choose_first():
    from random import randint
    player=randint(1,2)
    if player==1:
        return "player 1"
    else:
        return "player 2"

#func that check if pos is space or not
def space_check(board,pos):
    return board[pos]==" "

#func to check all of board is space or not
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

#func to
def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


#func to continue came
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# Let's play our game
while(True): #still gaming


# set Board , whos first , choose marker X or o
        the_board=[" "]*10
        player1_marker , player2_marker = player_iput() #take from user tha marker
        turn = choose_first()  #choose random
        print (turn+" will go first ")
        play_game=input("Ready to Play Y : N ? ").upper()

        if play_game == "y".upper() :   #to use game_on with continue to game
            game_on = True
        else:
            game_on=False

        while(game_on == True): # begin the game

            if turn == "player 1":
                display(the_board)  #Display Board
                position=player_choice(the_board) # where your game come on and check postion
                place_marker(the_board,player1_marker,position)  #replace position instead of marer
                if  win_check(the_board,player1_marker): # check if win or no
                    display(the_board)
                    print("Player 1 won !! ")
                    game_on = False # to breake from loop to firrst loop
                elif full_board_check(the_board):
                    display(the_board)
                    print("Tie Game !!")
                    game_on = False
                else:
                       turn = "player 2"

            else:
                display(the_board)
                position=player_choice(the_board)
                place_marker(the_board,player2_marker,position)
                if win_check(the_board,player2_marker):
                    display(the_board)
                    print("Player 2 won !! ")
                    game_on = False
                elif full_board_check(the_board):
                    print("Tie Game !! ")
                    game_on = False
                else:
                    turn = "player 1"

        if  not  replay():
            break
