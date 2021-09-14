from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.shape('circle')
        self.color('white')
        self.penup()
        self.setheading(45)
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.06

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def speed_up(self):
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.06
        self.bounce_x()  # change player first turn


