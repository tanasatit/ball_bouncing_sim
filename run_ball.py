import turtle
from ball import Balls
import random


class Simulator:
    def __init__(self):
        self.balls = []
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.speed = 0
        self.ball_radius = 0
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]

    def random(self, num_balls, ball_speed, size_balls):
        for i in range(num_balls):
            self.xpos.append(random.randint(-1 * self.canvas_width + size_balls, self.canvas_width - size_balls))
            self.ypos.append(random.randint(-1 * self.canvas_height + size_balls, self.canvas_height - size_balls))
            self.vx.append(ball_speed)
            self.vy.append(ball_speed)
            self.ball_color.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.speed = ball_speed
            self.ball_radius = size_balls
        return self.xpos, self.ypos, self.vx, self.vy, self.ball_color, self.speed, self.ball_radius


ball_num = int(input("Number of balls to simulate: "))
ball_speed = int(input("The speed for balls: "))
ball_size = int(input("The size for the balls: "))


test1 = Simulator()
xpos, ypos, vx, vy, color, speed_ball, size_ball = test1.random(ball_num, ball_speed, ball_size)
ball1 = Balls(xpos, ypos, vx, vy, color, ball_size, ball_num)

while True:
    turtle.clear()
    for i in range(ball_num):
        b = ball1.draw_circle(i)
        ball1.move_circle(i)
        test1.balls.append(b)

    turtle.update()

turtle.done()
