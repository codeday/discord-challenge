from os import getenv

from discord.ext import commands, tasks

import discord

#from db.models import session_creator
#from utils.challenge_users_service import ChallengeUsersService


class ChallengeCog(commands.Cog, name="Challenge"):
    def __init__(self, bot):
        self.bot = bot
        #self.challenge_user_service = ChallengeUsersService()
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
    async def links(self, ctx): #needs to be fixed
        embed = discord.Embed(title='Helpful Links', color=0xff686b, timestamp=ctx.message.created_at)

        embed.set_author(name="CodeDay", url="https://www.codeday.org/",
                         icon_url="https://f1.codeday.org/logo_heartonly_ff686b.png")

        embed.set_thumbnail(url="https://f1.codeday.org/logo_heartonly_ff686b.png")  # insert pic

        embed.add_field(name="Leetcode, one of the most popular practice websites out there.",
                        value='https://leetcode.com/', inline=False)

        embed.add_field(name="Coding Bat, with simple exercises on a wide variety of subjects.",
                        value='https://codingbat.com/java', inline=False)

        embed.add_field(
            name="USACO, a US org for computer science olympiad. Practice lessons and competitions to test your skills.",
            value='http://www.usaco.org/', inline=False)

        embed.add_field(name="Project euler, a website for practicing math algorithms",
                        value='https://projecteuler.net/', inline=False)

        embed.add_field(name="Hackerrank, another popular website for practicing, suited for interviews as well.",
                        value='https://www.hackerrank.com/dashboard', inline=False)

        embed.set_footer(text='Be on the lookout for a challenge every week!')

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ChallengeCog(bot))
