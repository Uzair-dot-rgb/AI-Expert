import random
from colorama import Fore, Style, init

init(autoreset=True)

def player_choice():
    choice = ' '
    valid_choices = ['rock', 'paper', 'pencil', 'scissors']
    while choice not in valid_choices:
        choice = input(Fore.GREEN + "Choose your weapon (Rock, Paper, Pencil, Scissors): " + Style.RESET_ALL).lower()
    return choice

def check_win(player, ai):
    if player == ai:
        return 'draw'
    
    # Win conditions
    if player == 'rock' and ai in ['scissors', 'pencil']:
        return 'player'
    if player == 'paper' and ai == 'rock':
        return 'player'
    if player == 'pencil' and ai == 'paper':
        return 'player'
    if player == 'scissors' and ai == 'paper':
        return 'player'
        
    return 'ai'

def coloured_text(text, color_choice):
    colors = {
        'rock': Fore.RED,
        'paper': Fore.BLUE,
        'pencil': Fore.YELLOW,
        'scissors': Fore.CYAN
    }
    return colors.get(text, Fore.WHITE) + text.capitalize() + Style.RESET_ALL

def rpsps_game():
    print("Welcome to Rock, Paper, Pencil, Scissors!")
    player_name = input(Fore.GREEN + "Please enter your name: " + Style.RESET_ALL)
    
    # Score Tracking
    p_score = 0
    ai_score = 0
    
    while True:
        player = player_choice()
        ai = random.choice(['rock', 'paper', 'pencil', 'scissors'])
        
        print()
        print(f"{player_name} chose: {coloured_text(player, 'player')}")
        print(f"AI chose: {coloured_text(ai, 'ai')}")
        
        result = check_win(player, ai)
        
        if result == 'draw':
            print(Fore.YELLOW + "It's a draw!" + Style.RESET_ALL)
        elif result == 'player':
            print(Fore.GREEN + f"Congratulations {player_name}, you win the round!" + Style.RESET_ALL)
            p_score += 1
        else:
            print(Fore.RED + "AI wins the round! Better luck next time." + Style.RESET_ALL)
            ai_score += 1
            
        print(Fore.WHITE + f"\nScore -> {player_name}: {p_score} | AI: {ai_score}" + Style.RESET_ALL)
        
        play_again = input(Fore.GREEN + "\nDo you want to play again? (y/n): " + Style.RESET_ALL).lower()
        if play_again != 'y':
            print(Fore.GREEN + f"\nThanks for playing! Final Score -> {player_name}: {p_score} | AI: {ai_score}" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    rpsps_game()
