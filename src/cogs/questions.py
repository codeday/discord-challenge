import csv
from csv import reader
import discord
from discord.ext import tasks, commands
from os import getenv
import random
import re

def pick_question():
    print("csv reading start")
    questions =[]
    with open('Test Sheet.csv', newline='') as csvfile:
        questions = csvfile.readlines()
    print(questions[0])
    del questions[0]
    question = []
    strquestion = random.choice(questions)
    for part in reader(strquestion):
        question.append(part)
    return question

async def send_question(bot, channel, question):
    for i in question:
        print(i)
    await channel.send("This is a " + question[0] + " question.")
    await channel.send("Question: " + question[1])
    await channel.send("Description: " + question[2])
    #await channel.send()





# Tasks: read_csv_task and question_send_task
