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
        global rand_row_number
        rand_row_number = random.randrange(1, lines -1)
        print(rand_row_number)

    with open("Test Sheet.csv", newline='') as csvfile:
        index = 0
        for row in csvfile:
            index =+ 1
            print(lines)
            if index == rand_row_number:
                question = row
        return question






# Tasks: read_csv_task and question_send_task
