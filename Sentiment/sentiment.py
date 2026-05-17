import colorama
from textblob import TextBlob
from colorama import Fore, Style
colorama.init()
print(f"{Fore.CYAN} 🐍 Welcome to Sentiment Spy! 🐍{Style.RESET_ALL}")
user_name = input(f"{Fore.YELLOW}Enter your name: {Style.RESET_ALL}")
if not user_name.strip():
    user_name = "Mystery Spy"
conversation_history = []
print(f"{Fore.GREEN}Hello, {user_name}! Let's analyze some sentiments!{Style.RESET_ALL}")
print("Type a sentence and I will analyze your sentence with a TextBlob, and show you your sentiment.")
print("Type reset, history, or exit to quit.")
while True:
    user_input = input(f"{Fore.YELLOW}Enter a sentence: {Style.RESET_ALL}")
    if not user_input.strip():
        print(f"{Fore.RED}Please enter some text or valid command.{Style.RESET_ALL}")
        continue
    if user_input.lower() == "exit":
        print(f"{Fore.CYAN}Goodbye, {user_name}! Thanks for using Sentiment Spy!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.GREEN}Conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet!{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History: {Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, 1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW
                print(f"{color}{idx}. '{text}' - Polarity: {polarity:.2f} ({sentiment_type}){Style.RESET_ALL}")
        continue
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
    conversation_history.append((user_input, polarity, sentiment_type))
    print(f"{color}Sentiment: {sentiment_type} (Polarity: {polarity:.2f}){Style.RESET_ALL}")