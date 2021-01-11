from os import getenv

from discord.ext import commands, tasks

from db.models import session_creator
from utils.challenge_users_service import ChallengeUsersService


class ChallengeCog(commands.Cog, name="Challenge"):

    def __init__(self, bot):
        self.bot = bot
        self.challenge_user_service = ChallengeUsersService()
        self.challenge_channel = getenv("CHALLENGE_CHANNEL", 790574063071789078)

    @commands.command(brief='Answer the weekly coding challenge (make sure to have dms on)!',
                      description='Answer the weekly coding challenge (make sure to have dms on)!')
    async def answer(self, ctx):
        await ctx.send("answer command placeholder")

    @commands.command(brief='Check your progress to different challenge milestones.',
                      description='Check your progress to different challenge milestones.')
    async def progress(self, ctx):
        await ctx.send("progress command placeholder")

    @commands.command(brief='Check what challenge badges you have.', description='Check what challenge badges you have.')
    async def badges(self, ctx):
        await ctx.send("badges command placeholder")

    @commands.command(brief='A nice list of resources to help you on your journey.',
                      description='A nice list of resources to help you on your journey.')
    async def links(self, ctx):
        await ctx.send("links command placeholder")


def setup(bot):
    bot.add_cog(ChallengeCog(bot))
