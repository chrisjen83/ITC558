# Question 8

class ShortQuestion:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def get_question(self):
        return self.question

    def check_answer(self, attempt):
        if attempt == self.answer:
            result = True
        else:
            result = False

        return result
