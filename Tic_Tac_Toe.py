# TIC TAC TOE
intro = "Hello, and welcome to tic tac toe! Player one, you're X. Player two will be O."
question = "Enter a number from 1 to 9 to choose which spot on the board you'd like to place your "
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def print_board():
    for i in range(0, 9):
        if ((i + 1) % 3 == 0 and i != 0):
            print(str(board[i]) + "|")
        else:
            print(str(board[i]) + "|", end=" ")

def checkGame():
    horizontals = ((board[0] == board[1] and board[1] == board[2]) or (board[3] == board[4] and board[4] == board[5]) or (board[6] == board[7] and board[7] == board[8]))

    diagonals = ((board[0] == board[4] and board[0] == board[8]) or (board[2] == board[4] and board[6] == board[4]))

    verticals = ((board[2] == board[5] and board[5] == board[8]) or (board[0] == board[3] and board[3] == board[6]) or (board[1] == board[4] and board[4] == board[7]))

    return (horizontals or verticals or diagonals)

print(intro)
play = True
while (play):
    play = False
    player_one = True
    counter = 0
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while (not checkGame()):
        print_board()
        if (player_one):
            index = int(input("Player one, it's your turn." + question + "X:")) - 1
            board[index] = 'X'
        else:
            index = int(input("Player two, it's your turn." + question + "O:")) - 1
            board[index] = 'O'
        player_one = not player_one
        counter += 1
        if (counter > 8):
            break
    print_board()
    if (not checkGame()):
        print ("It's a tie!")
    elif (player_one):
        print ("Congratulations Player two!")
    else:
        print ("Congratulations Player one!")

    ask = input("Do you want to play another game? Y|N:")
    if ask == 'Y':
        play = True
    else:
        play = False
        print ("Thank you for playing!")
