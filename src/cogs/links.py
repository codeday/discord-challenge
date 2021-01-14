#links to practice sites


import discord


def links_embed(self, ctx):
    embed = discord.Embed(title='Helpful Links', color=0xff686b, timestamp=ctx.message.created_at)

    embed.set_author(name="CodeDay", url="https://www.codeday.org/", icon_url= "https://f1.codeday.org/logo_heartonly_ff686b.png")

    embed.set_thumbnail(url="https://f1.codeday.org/logo_heartonly_ff686b.png") #insert pic

    embed.add_field(name="`Websites for practicing algorithms and data structures`", inline=False)

    embed.add_field(name="Leetcode, one of the most popular practice websites out there.", value='`https://leetcode.com/`', inline=False)

    embed.add_field(name="Coding Bat, with simple exercises on a wide variety of subjects.", value='`https://codingbat.com/java`', inline=False)

    embed.add_field(name="USACO, a US org for computer science olympiad. Practice lessons and competitions to test your skills.", value='`http://www.usaco.org/`', inline=False)

    embed.add_field(name="Project euler, a website for practicing math algorithms", value='`https://projecteuler.net/`', inline=False)

    embed.add_field(name="Hackerrank, another popular website for practicing, suited for interviews as well.", value='`https://www.hackerrank.com/dashboard`', inline=False)

    embed.set_footer(text='Be on the lookout for a challenge every week!')

    await ctx.send(embed=embed)
