import csv
import discord
from discord.ext import tasks, commands
from os import getenv
import random



def pick_question():
    print("csv reading start")
    questions =[]
    with open('Test Sheet.csv', newline='') as csvfile:
        questions = csvfile.readlines()
    print(questions[0])
    del questions[0]
    question = random.choice(questions)
    send_question(question)

def send_question(bot)
    print(question)





# Tasks: read_csv_task and question_send_task
