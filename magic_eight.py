import random
def ask_question():
    question_inp = input("Please enter your question: ")
    return question_inp
<<<<<<< HEAD

while True:
    ques = ask_question()
    if ques[-1] == "?":
        print("Yes it's a question.")
    elif ques == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")
=======
magic_answer = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes - definitely.", "You may rely on it.", 
"As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", 
"Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", 
"Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
>>>>>>> d5f0b25f37660032e42d654eb6ed72756aab0ae5
