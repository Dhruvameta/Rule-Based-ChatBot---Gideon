# Gideon - Rule-Based Python ChatBot

## Overview

Gideon is a beginner-friendly rule-based chatbot developed in Python. It is designed to answer a variety of predefined questions using a dictionary-based response system. The chatbot demonstrates the fundamentals of Natural Language Processing (NLP) concepts, keyword matching, conditional logic, and conversational flow without relying on external AI libraries or machine learning models.

This project serves as an excellent introduction to chatbot development and showcases how conversational systems can be built using simple Python programming techniques.

---

## Features

### Conversational Greetings

Gideon can recognize and respond to common greetings such as:

* Hi
* Hello
* Hey
* Good Morning
* Good Afternoon
* Good Evening

### Identity & Information

Users can ask questions about the chatbot itself, including:

* What is your name?
* Who are you?
* Who created you?
* Are you human?

### Status Queries

The chatbot can answer questions regarding its operational status:

* How are you?
* Are you okay?
* What are you doing?
* Are you busy?

### Educational Responses

Gideon provides basic information on several subjects:

#### Programming

* Python
* Java
* JavaScript
* Algorithms
* Artificial Intelligence
* Coding Concepts

#### Science

* Gravity
* The Sun
* The Moon
* Water
* Why the sky is blue

#### Technology

* Computers
* Internet
* Wi-Fi
* Smartphones

#### Mathematics

* Addition
* Subtraction
* Multiplication
* Division

### General Knowledge

The chatbot can answer common fact-based questions such as:

* Capital of India
* Capital of France
* Largest Planet
* Largest Ocean
* Fastest Land Animal

### Motivation & Encouragement

Gideon includes supportive and motivational responses:

* Motivate me
* Encourage me
* I am tired
* I feel sad

### Fun Interactions

Users can enjoy lighthearted conversations:

* Tell me a joke
* Make me laugh
* Do you like pizza?

### Personal Questions

The chatbot can answer simple personal-style questions:

* Where do you live?
* Do you sleep?
* Do you eat?
* Do you dream?

### Conversation Termination

The chatbot supports exit commands such as:

* Bye
* Goodbye
* Exit
* Quit

---

## How It Works

The chatbot stores predefined questions and responses inside a Python dictionary.

```python
responses = {
    "what is python": "Python is a versatile and beginner-friendly programming language.",
    "how are you": "I'm functioning perfectly."
}
```

When a user enters a query:

1. The input is converted to lowercase.
2. The chatbot searches through all predefined keywords.
3. If a matching keyword is found, the corresponding response is returned.
4. If no match exists, Gideon displays a fallback response indicating that it does not know the answer.

The chatbot continuously runs inside a loop until the user chooses to end the conversation.



## Technologies Used

* Python 3
* Dictionaries
* Functions
* Loops
* Conditional Statements
* String Matching


## Example Conversation

text
Hey There! I am Gideon, Your Personalized Rule Based ChatBot.
I'm here to assist you with your Basic Questions.

Please ask your question:
> what is python

Bot Response:
Python is a versatile and beginner-friendly programming language.

Please ask your question:
> tell me a joke

Bot Response:
Why do programmers hate nature? Too many bugs.

Please ask your question:
> bye

Bot Response:
Goodbye!

## Limitations

Since Gideon is a rule-based chatbot:

* It cannot learn from conversations.
* It cannot generate new responses.
* It depends entirely on predefined keywords.
* It may fail to understand complex or differently phrased questions.
* It does not use Machine Learning or Natural Language Processing models.

## Future Improvements

Possible enhancements for future versions include:

* Adding Natural Language Processing (NLP)
* Integrating Machine Learning models
* Connecting to APIs for real-time information
* Storing conversation history
* Expanding the knowledge base

## Learning Objectives

This project was created to practice:

* Python fundamentals
* Dictionaries and data structures
* Functions and loops
* User input handling
* Basic chatbot architecture
* Rule-based conversational systems

## Author: Dhruv Ameta

*"Every intelligent system starts with simple rules. Gideon is the first step toward building more advanced conversational AI systems."*
