print('Welcome to Tic Tac Toe!')

#functions are here
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' '*3+'|'+' '*3+'|'+' '*3)
    print(' '+board[7]+' '+'|'+' '+board[8]+' '+'|'+' '+board[9]+' ')
    print('_'*3+'|'+'_'*3+'|'+'_'*3)
    print(' '+board[4]+' '+'|'+' '+board[5]+' '+'|'+' '+board[6]+' ')
    print('_'*3+'|'+'_'*3+'|'+'_'*3)
    print(' '+board[1]+' '+'|'+' '+board[2]+' '+'|'+' '+board[3]+' ')
    
def player_input():
    player1 = ''
    player2 = ''
    while not (player1 in ['X','O']):
        player1 = input("Please pick a marker 'X' or 'O': ")
        player2 = [x for x in ['X','O'] if x != player1][0]
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker
    return board

def win_check(board, mark):
    d = {"position":[]}
    for index, chess in enumerate(board):
        if chess == mark:
            d["position"].append(index)
        else:
            pass
    win_pattern = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in win_pattern:
        if set(i) < set(d["position"]):
            return True
        else:
            pass
    return False

import random

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for position in board:
        if position == ' ':
            return False
        else:
            pass
    return True

def player_choice(board):
    ask = True
    while ask:
        position = int(input('Please enter a number: '))
        if space_check(board, position):
            return position
            ask = False
        else:
            print("This position has been taken...")
    
def replay():
    answer = input('Do you want to play again? Y or N?')
    return answer == 'Y' 
# main
play = True


    # Set the game up here
board = [' ']*10
display_board(board)
player1_marker, player2_marker = player_input()
    
turn = choose_first()
print(turn)

while play:
    
    if turn == "Player 1":
        #Player 1 Turn   
        
        pos = player_choice(board)
        board = place_marker(board, player1_marker, pos)
        display_board(board)
        
        if win_check(board, player1_marker):
            print('You win!')
            play = False
        else:
            if full_board_check(board):
                display_board(board)
                print("Tied game!")
                play = False
            else:
                turn = "Player 2"
        
        # Player2's turn
    else:
        pos = player_choice(board)
        board = place_marker(board, player2_marker, pos)
        display_board(board)

        if win_check(board, player2_marker):
            print('You win!')
            play = False
        else:
            if full_board_check(board):
                display_board(board)
                print("Tied game!")
                play = False
            else:
                turn = "Player 1"    
    
    if not replay():
        play = False