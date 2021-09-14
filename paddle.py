from turtle import Turtle

START_P1 = (350, 0)
START_CPU = (-350, 0)
MOVEMENT = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        # self.setheading(90)
        self.goto(position)
        self.shape("square")
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()


    def move_up(self):
        self.goto(self.xcor(), self.ycor()+MOVEMENT)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-MOVEMENT)
