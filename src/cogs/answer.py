from discord.ext import commands
from os import getenv


# user_answer = input/submission
# questions_answer:
# > defined answers for question
# > list in case differences between answers
# > Example: daft Punk and DAFT PUNK
# make answers spoilers


class AnswerCog(commands.Cog, name="Answer"):
    def __init__(self, bot):
        self.question_answers = [] #add here, passed as list due to some questions having multiple
        self.user_answer = "test value" #included in call, ends error
        self.bot = bot #check this
        self.challenge_channel = getenv("CHALLENGE_CHANNEL", 790574063071789078)

# compares answer to real answer, with leniency

    # splits question answers between numbers and strings
    def answer_type(self, bot, question_answers, user_answer):
        try:
            for q in question_answers:
                check = int(q)
            self.num_compare(user_answer, question_answers) #checks if num
        except ValueError:
            self.string_compare(self, bot, user_answer, question_answers)

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
                correct_answer()
            elif difference < 1:  # this value can/should be changed
                close_answer()
            else:
                wrong_answer()

    # ensure that capitalization/ spelling mistakes don't stop answers
    def string_compare(self, bot, user_answer, question_answers):
        answer_found = False
        # lowercases everything-> issue in some questions?

        user_answer.lower()
        for ans in question_answers:
            ans.lower()
        while not answer_found:
            if user_answer == [ans for ans in question_answers]:
                correct_answer(bot)
            elif user_answer == [ans.strip() for ans in question_answers]:
                close_answer(bot)  # likely unneccessary
            else:
                wrong_answer(bot)


#call badge command, send dm
#get user id that sent the message
#add reaction to command that was sent

async def correct_answer(bot):
    user = bot.get_author()
    await user.send('Your answer was correct!')
    #send user the amount of badges they have earned
    #one of you good coders can fill in some majic graph ql here
    correct_answers = 0
    await user.send(f'You have answered {correct_answers} questions.')

async def close_answer(bot):
    user = bot.get_author()
    await user.send("Your answer didn\'t perfectly match with the answer we have. Check if your format is off, and if you\'re sure it\'s right, please let us know.")

async def wrong_answer(bot):
    user = bot.get_author()
    await user.send('Your answer is incorrect!')
    await user.send('If you need help, ask in #help-desk.')

def setup(bot):
    bot.add_cog(AnswerCog(bot))
