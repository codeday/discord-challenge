import csv
import discord
from discord.ext import tasks, commands
from os import getenv


class QuestionReaderCog(commands.Cog, name="Question_Reader"):
    def __init__(self, bot):
        self.bot = bot
        # self.challenge_user_service = ChallengeUsersService()
        self.challenge_channel = getenv("CHALLENGE_CHANNEL", 790574063071789078)

    def read_csv(self, bot):
        with open('Test_Sheet.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=' ')

