import csv
import discord
from discord.ext import tasks, commands


class QuestionReaderCog(question_reader.Cog, name="Question_Reader"):
    def __init__(self, bot):
        self.bot = bot

    def read_csv(self, bot):
        with open('Test_Sheet.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ')

