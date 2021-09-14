from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l_points = 0
        self.r_points = 0

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f'{self.l_points}', align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f'{self.r_points}', align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_points += 1

    def r_point(self):
        self.r_points += 1
