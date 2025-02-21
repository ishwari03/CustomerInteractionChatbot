import nltk
from nltk.chat.util import Chat, reflections
import random

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Define patterns and responses for customer support
patterns_responses = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hi! How can I help you today?']),
    (r'how are you?', ['I am doing great, thank you for asking!']),
    (r'what is your name?', ['I am a chatbot created to help you with your queries!']),
    
    # Product or service related queries
    (r'can you tell me about your products?|what products do you offer?', 
     ['We offer a wide range of products including electronics, home appliances, and more. How can I help you with a specific product?']),
    
    (r'how do I place an order?| how to place an order?', 
     ['To place an order, just visit our website and select the product you want. Add it to your cart, and proceed to checkout. Do you need help with this process?']),
    
    (r'what is your return policy?', 
     ['Our return policy allows you to return products within 30 days of purchase. Would you like more details on how to return a product?']),
    
    # Customer support or service related queries
    (r'help|assist me|support', 
     ['I am here to assist you! What kind of help do you need?']),
    
    (r'how do I contact customer support?', 
     ['You can contact our customer support team by visiting the "Contact Us" page on our website or call us at 1-800-123-4567.']),
    
    (r'where are you located?', ['We are located at 123 Main Street, Springfield, USA. Feel free to visit us or reach out for more details!']),

    # Order status check
    (r'where is my order?|track my order', 
     ['Can you please provide your order number, so I can check the status for you?']),
    
    # Frequently Asked Questions (FAQs)
    (r'what are your business hours?', 
     ['We are open from 9 AM to 5 PM, Monday to Friday.']),
    
    (r'(.*)(thank you|thanks)', 
     ['You’re welcome! If you have more questions, feel free to ask.']),
    
    # If no match, fallback response
    (r'(.*)', 
     ['Sorry, I did not understand that. Could you please rephrase?'])
]

# Initialize the chatbot
chatbot = Chat(patterns_responses, reflections)

# Function to interact with the chatbot
def chat():
    print("Hello! I am your customer support chatbot. Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Feel free to reach out anytime.")
            break
        response = chatbot.respond(user_input)
        
        # If the chatbot doesn't respond, add a fallback response
        if not response:
            response = random.choice(['I am sorry, I didn’t quite catch that. Could you rephrase your question?',
                                      'Could you provide more details or ask something else?'])
        
        print(f"Bot: {response}")

# Start the chat
if __name__ == "__main__":
    chat()

    