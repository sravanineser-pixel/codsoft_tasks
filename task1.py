

print("ChatBot: Hello! I am a simple chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user == "hello" or user == "hi":
        print("ChatBot: Hello! How can I help you?")

    elif user == "how are you":
        print("ChatBot: I'm doing great! Thanks for asking.")

    elif user == "what is your name":
        print("ChatBot: My name is RuleBot.")

    elif user == "who created you":
        print("ChatBot: I was created using Python.")

    elif user == "what can you do":
        print("ChatBot: I can answer simple predefined questions.")

    elif user == "time":
        from datetime import datetime
        print("ChatBot: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        from datetime import datetime
        print("ChatBot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif user == "thanks" or user == "thank you":
        print("ChatBot: You're welcome!")

    elif user == "bye":
        print("ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")