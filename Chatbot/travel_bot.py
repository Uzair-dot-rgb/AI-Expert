import re, random
from colorama import Fore, init
init(autoreset=True)
destinations = {
    "beaches" : ["Bali", "Maldives", "Phuket"],
    "mountains" : ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities" :["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]
def show_help():
    print("\nI can:")
    print("- Suggest travel spots (say 'recommendations')")
    print("- Tell you a travel joke (say 'joke')")
    print("- Offer packing tips (say 'packing tips')")
    print("- Exit the chat (say 'exit')\n")

def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.strip().lower())    

def recommend():
    category = input("What type of destination are you interested in? (beaches/mountains/cities) ")
    category = normalize_input(category)
    if category in destinations:
        suggestions = random.choice(destinations[category])
        print(f"I recommend visiting {Fore.CYAN}{suggestions}{Fore.RESET} for a great {category} experience!")
        print("Did you like it? (yes/no)")
        answer = input(Fore.YELLOW + "Your answer: " + Fore.RESET).strip().lower()
        if answer == "yes":
            print("Awesome! I hope you have a fantastic trip!")
        elif answer == "no":
            print("No worries! I can suggest something else next time.")
            recommend()
        else:
            print("I didn't understand that. Let's try again.")
            recommend()
    else:
        print("Sorry, I don't have recommendations for that category. Please choose from beaches, mountains, or cities.")
        recommend()

def tell_joke():
    print(f"TravelBot: {random.choice(jokes)}")

def packing_tips():
    print("TravelBot: Where to?")
    location = normalize_input(input("Your destination: "))
    print("TravelBot: How many days?")
    days = input("Number of days: ")
    print(f"TravelBot: Packing tips for {days} days in {location}:")
    print("- Pack versatile clothing that can be layered.")
    print("- Don't forget chargers and adapters.")
    print("- Bring a reusable water bottle.")

def chat():
    print("Hello! I am a TravelBot.")
    name = input("Your name? ")
    print(f"Nice to meet you, {name}!")
    show_help()
    while True:
        user_input = input(f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "recommendations" in user_input or "suggest" in user_input:
           recommend()
        elif "joke" in user_input or "funny" in user_input:
            tell_joke()
        elif "packing tips" in user_input or "pack" in user_input:
            packing_tips()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "quit" in user_input:
            print("Goodbye! Safe travels!")
            break
        else:
            print("Sorry, I didn't understand that. Type 'help' for options.")
if __name__ == "__main__":
    chat()