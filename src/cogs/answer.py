from discord.ext import commands
from os import getenv


# user_answer = input/submission
# questions_answer:
# > defined answers for question
# > list in case differences between answers
# > Example: daft Punk and DAFT PUNK
# make answers spoilers

class AnswerCog(commands.Cog, name="Answer"):
    def __init__(self, bot, user_answer, question_answers):
        self.question_answers = []
        self.user_answer = user_answer
        self.bot = bot
        self.challenge_channel = getenv("CHALLENGE_CHANNEL", 790574063071789078)

    # compares answer to real answer, with leniency

    # splits question answers between numbers and strings
    # ideally done once a week
    def answer_type(self, question_answers, user_answer):
        try:
            for q in question_answers:
                check = int(q)
            self.num_compare(user_answer, question_answers)
        except ValueError:
            self.string_compare(self)

    def num_compare(self, user_answer, question_answers):
        difference = 0
        diff_list = []
        for i in question_answers:
            temp_diff = user_answer - i
            if difference > 0:
                diff_list.append(temp_diff)
            difference = diff_list[0]
            for n in diff_list:
                if abs(n) <= difference:
                    difference = n

        for i in question_answers:
            if user_answer == i:
                print("Exactly correct")  # change to discord way of course :)
            elif difference < 1:  # this value can/should be changed
                print("Your answer is very close")
            else:
                print("Good try")

    # ensure that capitalization/ spelling mistakes don't stop answers
    def string_compare(self, user_answer, question_answers):
        answer_found = False
        # lowercases everything-> issue in some questions?

        user_answer.lower()
        for ans in question_answers:
            ans.lower()
        while not answer_found:
            if user_answer == [ans for ans in question_answers]:
                print("Your answer is correct")
            elif user_answer == [ans.strip() for ans in question_answers]:
                print("Your answer is correct without spaces")  # likely unneccessary
            else:
                print("Your answer is incorrect")


    #call badge command, send dm
    #get user id that sent the message
    #add reaction to command that was sent
    #def correct_answer(self):

ctx.author.send

   # def wrong_answer(self):


def setup(bot):
    bot.add_cog(AnswerCog(bot))
