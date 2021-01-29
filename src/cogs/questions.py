import csv
import discord
from discord.ext import tasks, commands
from os import getenv
import random

def pick_question():
    print("csv reading start")
    with open('Test Sheet.csv', newline='') as csvfile:
        lines = sum(1 for row in csvfile)
        for row in csvfile:
            if lines == 0:
                print(f'Column names are {",".join(row)}')
        global row_number
        row_number = random.randrange(1, lines)

    with open("Test Sheet.csv", newline='') as csvfile:
        file = csv.reader(csvfile)

        question = next(row for row_number, row in enumerate(file) if row_number == lines)

        return

        print(question)
    return question





# Tasks: read_csv_task and question_send_task
