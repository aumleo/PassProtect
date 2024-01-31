question_data = [
{"text": "A slug's blood is green.", "answer": "True"},
{"text": "The loudest animal is the African Elephant.", "answer": "False"},
{"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
{"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
{"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
{"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
{"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
{"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
{"text": "Google was originally called 'Backrub'.", "answer": "True"},
{"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
{"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
{"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

#TO GET TEXT AND ANS
class Question:
    def __init__ (self, text, answer): 
        self.text=text
        self.answer=answer

#STORING THE Q
bank=[]
for question in question_data:
    q_text = question['text']
    q_ans = question['answer']
    new_q = Question(q_text, q_ans)
    
    bank.append(new_q)

#THE WORKING
class Quiz:
    def __init__(self, q_list):
        self.q_list= q_list
        self.q_no=0
        self.score=0

    def question_left(self):
        return self.q_no < len(self.q_list)
    
    def next_question(self):
        current_q = self.q_list[self.q_no]
        self.q_no += 1
        user_ans = input(f'Q.{self.q_no}: {current_q.text} (True/False): ')
        self.check_ans(user_ans, current_q.answer)

    def check_ans(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("That's right")
            self.score += 1
        else:
            print ("Wrong")
        print(f"The answer is : {correct_ans}")
        print(f"Your Score: {self.score}/{self.q_no}")
        print('\n')

#EXECUTE THE GAME
game = Quiz(bank)
while game.question_left():
    game.next_question()

print('Quiz Completed')
print(f'Score = {game.score}/{len(bank)}')
