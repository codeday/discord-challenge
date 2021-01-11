from os import getenv

from discord.ext import commands, tasks

from db.models import session_creator
from utils.challenge_users_service import ChallengeUsersService
import aiocron


class ChallengeCog(commands.Cog, name="Challenge"):

    def __init__(self, bot):
        self.bot = bot
        self.challenge_user_service = ChallengeUsersService()
        self.challenge_channel = getenv("CHALLENGE_CHANNEL", 790574063071789078)


def setup(bot):
    bot.add_cog(ChallengeCog(bot))
