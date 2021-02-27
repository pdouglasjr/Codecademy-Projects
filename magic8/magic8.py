# Name:     magic8.py
# Author:   Phillip Douglas

import random

choices = [
    "Yes - definitely.",
    "It is decidedly so.",
    "Without a doubt.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",
    "Indubitably",
]

name = input("Hi! What is your name? ")

while True:
    # question_prompt = len(name) == 0 ? "What is your question? " : f"What is your question, {name}? "

    if len(name) < 1:
        question_prompt = "What is your question? " 
    else:
        question_prompt = f"What is your question, {name}? "
    
    question = input(question_prompt)

    # Check for empty questions
    while len(question) < 1:
        print("Your question is blank. Please ask a question.")
        question = input(question_prompt)

    print()

    if len(name) < 1:
        print(f"Question: {question}")
    else:
        print(f"{name} asks: {question}")

    print(f"Magic 8-Ball's answer: {choices[random.randint(0, len(choices) - 1)]}")
    print()

    if len(name) < 1:
        response_prompt = "Do you want to ask another question (y/N)? "
    else:
        response_prompt = f"Do you want to ask another question, {name} (y/N)? "

    response = input(response_prompt).upper()

    print()

    if response != "Y":
        print("Have a good one! ;-)")
        break