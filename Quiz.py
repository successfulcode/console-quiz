from color_console import Color


questions = [ 
    { "question": "Who was the first president of the United States?", "answer": "George Washington"},
    { "question": "What is the capital of France?", "answer": "Paris"}, 
    { "question": "Who wrote the famous play Hamlet?", "answer": "Pacific Ocean"},
    { "question": "Who painted the famous artwork The Starry Night?", "answer": "Vincent van Gog"},
    { "question": "Who is known as the father of modern physics?", "answer": "Albert Einstein"}
]


def print_text(text, colorType):
      with colorType:
        print(text)


print_text("Welcome to my quiz. I hope that you will have a good time together.", Color.info)

startPlay = input("Do you want to play? ")


if startPlay.lower() == 'yes' or startPlay.lower() == 'ok' or startPlay.lower() == 'true':
    print_text("Ok! Let's go! Enjoy this moment!", Color.success)
    gamePoints = 0
else:
    print_text("Bye!!!", Color.success)
    quit()


def set_question(question, answer):

    global gamePoints

    question = input(question + " ")

    if question.lower() == answer.lower():
        print_text("Correct answer!", Color.success)
        gamePoints = gamePoints + 4
    else:
        print_text("Sorry, but it is incorrect answer!", Color.warning)


for item in questions:
    set_question(item['question'], item['answer'])


finalText = "Congratulations you got " + str(gamePoints) + " points!!!"

print_text(finalText, Color.info)