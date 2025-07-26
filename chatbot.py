def chatbot():
    print("🤖 Welcome to ChatBot! For any help type 'help' and type 'exit' to quit.")
    while True:
        user = input("You: ").lower()
        
        if user == "hello":
            print("Bot: Hi! How can I help you today?")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        elif user == "exit":
            print("Bot: Exiting...")
            break
        elif user == "help":
            print("Bot: Available commands: hello, how are you, bye, exit, help, what is your name, etc.")
        elif user == "what is your name":
            print("Bot: I am a chatbot created by CodeAlpha.")
        elif user == "what is your work":
            print("Bot: I am here to assist you with basic queries and provide information.")
        elif user == "what is your purpose":
            print("Bot: My purpose is to help you with your questions and provide assistance.")
        elif user == "what is your creator name":
            print("Bot: I was created by CodeAlpha.")
        else:
            print("Bot: I'm sorry, I didn't understand that. Please try again or type 'help' for assistance.")
    chatbot()
# chatbot.py
# This is a simple chatbot implementation in Python.
# It responds to basic commands and provides information about itself.
# To run this chatbot, simply execute the script in a Python environment.