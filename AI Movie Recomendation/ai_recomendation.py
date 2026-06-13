import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore
init(autoreset=True)
try:
    df = pd.read_csv("imdb_top_1000.csv")
except FileNotFoundError:
      print(Fore.RED + "Error: File not found."); raise SystemExit
genres = sorted({g.strip() for xs in df["Genre"].dropna().str.split(",") for g in xs})
def get_genre():
    print(Fore.GREEN + "Available genres",end = " ")
    for i, g in enumerate(genres, 1):
        print(f"{Fore.CYAN}{i}. {g}")
    print()
    while True:
        x = input(Fore.YELLOW + "Enter the number or the name of your preferred genre: ").strip()
        if x.isdigit() and 1 <= int(x) <= len(genres):
            return genres[int(x) - 1]
        x = x.title()
        if x in genres:
            return x 
        print(Fore.RED + "Invalid input. Please try again.")
def dot():
    for _ in range(3):
        print(Fore.YELLOW + ".", end = " ", flush = True); time.sleep(0.5)
print(Fore.BLUE + "Welcome to your personal movie recommendation system! \n")
name = input(Fore.YELLOW + "What is your name? ").strip()
print(f"Great to meet you, {name}! \n")
print(Fore.BLUE + "Let's find the perfect movie for you.")
genre = get_genre()
mood = input(Fore.Yellow + "How are you feeling today? ").strip()
print(Fore.BLUE + "\n Analyzing your mood...",end = " ", flush = True); 
dot()
mp = TextBlob(mood).sentiment.polarity
md = "positive" if mp > 0 else "negative" if mp < 0 else "neutral"
print(f"\n{Fore.GREEN} your mood is {md} (polarity: {mp:.2f})")





      