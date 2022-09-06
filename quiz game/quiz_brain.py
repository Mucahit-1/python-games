class QuizBrain:
    def __init__(self , q_list):

        self.question_list = q_list
        self.question_num = 0
        self.score = 0

    def still_has_question(self):
        return self.question_num < len(self.question_list)



    def next_question(self):
            current_q = self.question_list[self.question_num]
            self.question_num += 1
            answer = input(f"Q.{self.question_num} : {current_q.text} ? (True/False): ")
            self.check_answer(answer,  current_q.answer)


    def check_answer(self, answer , correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"you got it")
        else:
            print(f"worng the correct answer was {correct_answer}")
        print(f"your current score is {self.score}/{self.question_num}")
        print("\n")