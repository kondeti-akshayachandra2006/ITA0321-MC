
from nltk.chat.util import Chat, reflections

# Define chatbot responses
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],
    [r"what is your name", ["I am a simple chatbot."]],
    [r"how are you", ["I am fine. How are you?"]],
    [r"what is python", ["Python is a programming language."]],
    [r"bye|goodbye", ["Goodbye! Have a nice day."]],
    [r"(.*)", ["Sorry, I don't understand."]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

print("Chatbot: Hello! Type 'bye' to exit.")

# Start conversation
chatbot.converse()
