import random
from colorama import Fore, Style, init
init(autoreset=True)




def player_choice():
    symbol = ' '
    while symbol not in ['X', 'O']:
        symbol = input(Fore.GREEN + "Choose your symbol (X/O): " + Style.RESET_ALL).upper()
    if symbol == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'





def display_board(board):
    print()
    def coloured(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL
        
    print(' ' + coloured(board[0]) + ' | ' + coloured(board[1]) + ' | ' + coloured(board[2]))
    print('---+---+---')
    print(' ' + coloured(board[3]) + ' | ' + coloured(board[4]) + ' | ' + coloured(board[5]))
    print('---+---+---')
    print(' ' + coloured(board[6]) + ' | ' + coloured(board[7]) + ' | ' + coloured(board[8]))




    
def player_move(board, symbol):
    move = -1
    while move not in range(1, 10) or not board[move - 1].isdigit():
        try:
            move = int(input("Enter your move (1-9): "))
        except ValueError:
            print("Please enter a valid number between 1 to 9.")
    board[move - 1] = symbol






def check_win(board, symbol):
    wining_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), #Horizontal
                         (0, 3, 6), (1, 4, 7), (2, 5, 8), #Vertical
                         (0, 4, 8), (2, 4, 6)  #Diagonal
    ]
    for condition in wining_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False
    






def full_board(board):
    return all(not cell.isdigit() for cell in board)








def ai_move(board, ai_symbol, player_symbol):
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
        








def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    player_name = input(Fore.GREEN + "Please enter your name: " + Style.RESET_ALL)
    while True:
        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        player_symbol, ai_symbol = player_choice()
        turn = 'Player'
        game_on = True
        
        while game_on:
            display_board(board)
            if turn == 'Player':
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations {player_name}, you win!" + Style.RESET_ALL)
                    game_on = False
                else:
                    if full_board(board):
                        display_board(board)
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                        break
                    turn = 'AI'
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI wins! Better luck next time." + Style.RESET_ALL)
                    game_on = False
                else:
                    if full_board(board):
                        display_board(board)
                        print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
                        break
                    turn = 'Player'
        play_again = input(Fore.GREEN + "Do you want to play again? (y/n): " + Style.RESET_ALL).lower()
        if play_again != 'y':
            print(Fore.GREEN + "Thanks for playing! Goodbye!" + Style.RESET_ALL)
            break
                
                



if __name__ == "__main__":
    tic_tac_toe()
    