from csv import reader
import random


def pick_question():
    print("csv reading start")
    # split the string into questions
    splitquestion = []
    with open('Test Sheet.csv', newline='') as csvfile:
        questions = list(reader(csvfile))
        print(questions[0])
        del questions[0]
        question = random.choice(questions)
        for part in reader(question):
            splitquestion.append(part)
        question_answers = splitquestion[4]
    return splitquestion, question_answers
    #the var that I want


async def send_question(bot, channel, question):
    # doubled since list within list
    await channel.send("This is a " + str(question[0][0]) + " question.")
    await channel.send("Question: " + str(question[1][0]))
    await channel.send("Description: " + str(question[2][0]))
    await channel.send("Sample Answer: " + str(question[3][0]))

# TODO: send to log channel that question sent
