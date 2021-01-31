import csv
from csv import reader
import discord
from discord.ext import tasks, commands
from os import getenv
import random
import re

def pick_question():
    print("csv reading start")
    splitquestion = []
    with open('Test Sheet.csv', newline='') as csvfile:
        questions = list(reader(csvfile))
        print(questions[0])
        del questions[0]
        question = random.choice(questions)
        for part in reader(question):
            splitquestion.append(part)
    return splitquestion
    #split the string into questions

async def send_question(bot, channel, question):
    await channel.send("This is a " + str(question[0]) + " question.")
    await channel.send("Question: " + str(question[1]))
    await channel.send("Description: " + str(question[2]))
    await channel.send("Sample Answer: " + str(question[3]))
    #await channel.send()





# Tasks: read_csv_task and question_send_task
