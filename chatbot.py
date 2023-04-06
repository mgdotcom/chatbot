# Import the necessary libraries
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new chatbot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train("chatterbot.corpus.english")

# Start a conversation with the chatbot
print('Hi! How can I help you today?')
while True:
    try:
        user_input = input()
        bot_response = chatbot.get_response(user_input)
        print(bot_response)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
