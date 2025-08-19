import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only needed the first time)
nltk.download('punkt')

pairs = [
    ["hi|hello|hey", ["Hello there!", "Hi!", "Hey!"]],
    ["how are you ?", ["I'm fine, thank you.", "Doing great, how about you?"]],
    ["what is your name ?", ["I'm Mikasa the Chatbot!", "Call me Mikasa."]],
    ["bye|goodbye", ["Goodbye!", "See you soon!", "Bye, take care!"]],
]

def simple_chatbot():
    print("Hi, I'm Mikasa the chatbot! Type 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    simple_chatbot()
