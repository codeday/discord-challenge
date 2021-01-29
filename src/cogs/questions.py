import csv
import discord
from discord.ext import tasks, commands
from os import getenv


def read_csv():
    print("csv reading start")
    with open('Test Sheet.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=' ')
        lines = 0
        for row in csv_reader:
            if lines == 0:
                print(f'Column names are {",".join(row)}')
            else:
                print(
                    f'Difficulty:{row[0]}  Question: {row[1]}  Description: {row[2]}  Sample Answer: {row[3]} Answer: {row[4]} Id: {row[5]}')
                lines += 1
    return lines



def question_send(questions):


# Tasks: read_csv_task and question_send_task
