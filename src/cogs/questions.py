import csv
import discord
from discord.ext import tasks, commands
from os import getenv


def question_send():
    print("why doesnt this work?")

def read_csv():
    with open('Test_Sheet.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ')
        line = 0
        for row in csv_reader:
            if line == 0:
                print(f'Column names are {",".join(row)}')
                line += 1
            else:
                print(
                    f'Difficulty:{row[0]}  Question: {row[1]}  Description: {row[2]}  Sample Answer: {row[3]} Answer: {row[4]} Id: {row[5]}')
                line += 1
        print(f'There are {line} lines.')

# Tasks: read_csv_task and question_send_task


