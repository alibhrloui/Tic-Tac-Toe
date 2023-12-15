def main():
  print("welcome to game :) !")

  while True:
      theBoard = 10*[' ']
      player1_marker,player2_marker = player_input()
      turn = choose_first()
      print(f"{turn} Will go first!")

      play_game = input("Are you ready to play soldier ? (yes/no) ").lower()

      if play_game[0] == 'y':
          game_on = True
      else:
          game_on = False
      while game_on:
          if turn == 'Player 1':
              display_board(theBoard)
              position = player_choice(theBoard)
              place_marker(theBoard,player1_marker,position)

              if win_check(theBoard,player1_marker):
                  display_board(theBoard)
                  print("congrats! player1 wins.")
                  game_on = False
              else:
                  if full_board_check(theBoard):
                      display_board(theBoard)
                      print("DRAW!")
                      break
                  else:
                      turn = 'Player 2'
          else:
              display_board(theBoard)
              position = player_choice(theBoard)
              place_marker(theBoard,player2_marker,position)

              if win_check(theBoard,player2_marker):
                  display_board(theBoard)
                  print("congrats! player2 wins.")
                  game_on = False
              else:
                  if full_board_check(theBoard):
                      display_board(theBoard)
                      print("DRAW!")
                      break
                  else:
                      turn = 'Player 1'
      if not replay():
          break
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])
def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
def place_marker(board, marker, position):
    
    board[position] = marker
def win_check(board, mark):
    
    return ((board[1] == mark and board[2]==mark and board[3]==mark)or
    (board[4] == mark and board[5]==mark and board[6]==mark)or
    (board[7] == mark and board[8]==mark and board[9]==mark)or
    (board[1] == mark and board[4]==mark and board[7]==mark)or
    (board[2] == mark and board[5]==mark and board[8]==mark)or
    (board[3] == mark and board[6]==mark and board[9]==mark)or
    (board[1] == mark and board[5]==mark and board[9]==mark)or
    (board[7] == mark and board[5]==mark and board[3]==mark))
import random

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'player 1'
    else:
        return 'player 2'   
def space_check(board, position):
    
    return board[position] == ' ' 
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def player_choice(board):
    
    position = 0 
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position: (1-9) '))
    return position
def replay():
    a = input('play again? (yes/no) ').lower().strip()
    return a[0] == 'y'  
main()               