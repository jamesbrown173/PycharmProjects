#
# class User:
#
#     def __init__(self, user_id, userlame):
#         self.id = user_id
#         self.username = userlame
#
# user_1 = User("001", "angela")
#
# print(user_1.id)


class Question:
    def __init__(self, qtext, qanswer):
        self.text = qtext
        self.answer = qanswer

question_1 = Question("What's the first letter of the alphabet?","A")

print(question_1.text)
print(question_1.answer)



