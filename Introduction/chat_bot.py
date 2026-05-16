print("Hello! I am a AI bot. What is your name?")
name = input()
print(f"Nice to meet you {name}!")
print("How are you feeling today? (good/bad)")
feeling = input().lower()
if feeling == "good":
    print("I am glad to hear that!")
elif feeling == "bad":
    print("I am sorry to hear that. I hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")
print(f"It was nice chatting with you {name}. Have a nice day!")