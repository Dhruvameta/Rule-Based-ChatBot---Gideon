print("Hey There! I am Gideon, Your Personalized Rule Based ChatBot,")
print("Im here to assist you with your Basic Questions.")

# Chat Bot Memory Creation [ using dictionary for a response ]

responses = {

    # Greetings
    "Hello:": "Hi, Welcome. How can I Help You Today?",
    "How are you":"I am Grateful to serve You",
    "Who are You":"I am a rule based Smart ChatBot, My name is Gideon.",  
    "hi": "Hi there!",
    "hey": "Hey! What can I do for you?",
    "good morning": "Good morning! Ready for a productive day?",
    "good afternoon": "Good afternoon! How can I help?",
    "good evening": "Good evening! What would you like assistance with?",
    "nice to meet you": "Nice to meet you too!",
    "welcome": "Thank you!",

    #  Identity
    "what is your name": "My name is Gideon.",
    "who are you": "I am Gideon, your AI assistant.",
    "who created you": "I was created by my developer.",
    "what are you": "I am a Python-based chatbot designed to help users.",
    "are you human": "No, I am an AI assistant.",
    "are you real": "I am a virtual assistant, but our conversation is real.",

    # Status
    "how are you": "I'm functioning perfectly.",
    "how do you feel": "I don't have feelings, but I'm operating normally.",
    "are you okay": "Everything is running smoothly.",
    "what are you doing": "Waiting to assist you.",
    "are you busy": "Never too busy to help.",

    # Time & Date
    "what time is it": "I can provide the current time if connected to a clock module.",
    "what day is today": "I can determine today's date if connected to a date module.",
    "what is today's date": "I can check the current date when integrated with the system clock.",

    # Help
    "help": "You can ask me questions, request information, or use available commands.",
    "what can you do": "I can answer questions, perform tasks, and assist with information.",
    "show commands": "Available commands depend on how I am configured.",
    "assist me": "Of course. Tell me what you need.",

    # Programming
    "what is python": "Python is a versatile and beginner-friendly programming language.",
    "what is java": "Java is a widely used object-oriented programming language.",
    "what is javascript": "JavaScript is commonly used for web development.",
    "what is coding": "Coding is the process of writing instructions for computers.",
    "what is an algorithm": "An algorithm is a step-by-step procedure for solving a problem.",
    "what is ai": "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",

    # Science
   "what is gravity": "Gravity is the force that attracts objects toward each other.",
   "what is the sun": "The Sun is the star at the center of our solar system.",
   "what is the moon": "The Moon is Earth's natural satellite.",
   "why is the sky blue": "The sky appears blue due to the scattering of sunlight in Earth's atmosphere.",
   "what is water": "Water is a chemical compound made of hydrogen and oxygen.",

    # Technology
    "what is a computer": "A computer is an electronic device that processes data.",
    "what is the internet": "The internet is a global network connecting millions of computers.",
    "what is wifi": "Wi-Fi is a technology that allows wireless internet communication.",
    "what is a smartphone": "A smartphone is a mobile device with advanced computing capabilities.",

    # Math
    "what is addition": "Addition is the process of combining numbers.",
    "what is subtraction": "Subtraction is finding the difference between numbers.",
    "what is multiplication": "Multiplication is repeated addition.",
    "what is division": "Division is splitting a quantity into equal parts.",

    # General Knowledge
    "capital of india": "The capital of India is New Delhi.",
    "capital of france": "The capital of France is Paris.",
    "largest planet": "Jupiter is the largest planet in our solar system.",
    "fastest land animal": "The cheetah is the fastest land animal.",
    "largest ocean": "The Pacific Ocean is the largest ocean on Earth.",

    # Motivation
    "motivate me": "Every expert was once a beginner. Keep going.",
    "i am tired": "Rest if you need to, but don't give up.",
    "i feel sad": "I'm sorry you're feeling down. Talking about it may help.",
    "encourage me": "Small progress is still progress.",
    "give me a quote": "Success is the sum of small efforts repeated daily.",

    # Fun
    "tell me a joke": "Why do programmers hate nature? Too many bugs.",
    "tell another joke": "Why did the computer go to therapy? It had too many issues.",
    "make me laugh": "Debugging: where you spend hours fixing a typo.",
    "do you like pizza": "I don't eat, but pizza seems very popular.",

    # Personal Questions
    "where do you live": "I exist wherever my code is running.",
    "do you sleep": "No, I am always ready.",
    "do you eat": "No, I don't require food.",
    "do you dream": "I don't dream, but I can imagine possibilities.",

    # Farewell
    "bye": "Goodbye!",
    "goodbye": "See you next time.",
    "see you later": "Take care!",
    "exit": "Conversation ended.",
    "quit": "Goodbye and have a great day.",
    
}

# Take user input to get response of chatBot

def getResponseBot(userQusetion):
    userQusetion = userQusetion.lower()
    for eachkey in responses:
        if eachkey in userQusetion:
            return responses[eachkey]
        

    return "sorry i am not able to find an answer for this specific question, " \
    "I have a  limited range of data at my disposal right now. " \
    "i am still learning. HAHA :)"


while True:
    userInput = input("Please ask your question:")
    reply = getResponseBot(userInput)
    print("Bot Response:", reply)

    if "Bye" in userInput.lower():
        break

