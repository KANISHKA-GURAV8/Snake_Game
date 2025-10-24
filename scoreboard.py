from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open('data.txt') as file:
            self.high_score= int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_sb()

    def update_sb(self):
        self.clear()
        self.write(f"score:{self.score}, High-Score:{self.high_score}", align='center', font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
            with open('data.txt','w')as file:
                file.write(f"{self.high_score}")

        self.score=0
        self.update_sb()

    """def game_over(self):
        self.goto(0,0)
        self.write(f"game over", align='center', font=("Arial", 24, "normal"))"""

    def increase_sb(self):
        self.score+=1
        self.clear()
        self.update_sb()




