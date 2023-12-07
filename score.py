from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.left_score_count = 0
        self.right_score_count = 0
        self.penup()
        self.update_score()


    def update_score(self):
        self.goto(x=-100, y=220)
        self.write(self.left_score_count, False, align="center", font=('Courier', 50, 'bold'))
        self.goto(x=100, y=220)
        self.write(self.right_score_count, False, align="center", font=('Courier', 50, 'bold'))



    def left_keep_score(self):
        self.clear()
        self.left_score_count += 1
        self.update_score()


    def right_keep_score(self):
        self.clear()
        self.right_score_count += 1
        self.update_score()
