import random
def ask_question():
    question_inp = input("Please enter your question: ")
    return question_inp

while True:
    ques = ask_question()
    if ques[-1] == "?":
        print("Yes it's a question.")
    elif ques == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")