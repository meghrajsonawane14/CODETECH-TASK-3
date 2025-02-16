import nltk 
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you with your college admission inquiries?']),
    (r'what courses do you offer?', ['We offer various undergraduate and postgraduate courses. Please visit our website for more details.']),
    (r'what is the admission process?', ['The admission process typically involves an online application, submission of transcripts, and an entrance exam.']),
    (r'what is the eligibility criteria?', ['Eligibility criteria vary by course. Please check the specific course page for details.']),
    (r'how can I apply?', ['You can apply online through our admissions portal.']),
    (r'what are the important dates?', ['Important dates for admissions are usually posted on our website.']),
    (r'quit', ['Goodbye! Feel free to reach out if you have more questions.']),
    (r'(.*)', ['Sorry, I do not have information about that.'])
]


chatbot = Chat(pairs, reflections)

def chat_with_bot():
    print("Chatbot is ready to assist you with college admission inquiries! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

chat_with_bot()
