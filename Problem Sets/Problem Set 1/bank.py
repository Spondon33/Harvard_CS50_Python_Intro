user_greeting = input("Greeting: ").title().strip()
if user_greeting == "Hello":
    print("$0")
elif user_greeting == "Hello, Newman":
    print("$0")
elif user_greeting[0] == "H":
    print("$20")
else:
    print("$100")
