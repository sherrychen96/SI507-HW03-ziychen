import random
def ask_question():
    question_inp = input("Please enter your question: ")
    return question_inp

magic_answer = ["It is certain.", "It is decidedly so.", "Without a doubt", "Yes - definitely.", "You may rely on it.", 
"As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", 
"Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", 
"Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

while True:
    ques = ask_question()
    if ques[-1] == "?":
        print(magic_answer[random.randint(0, len(magic_answer)-1)])
    elif ques == "quit":
        break
    else:
        print("I'm sorry, I can only answer questions.")
