from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("HighScoreFile.txt") as data:
            self.high_score = int (data.read())
        self.goto(0, 270)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score:{self.high_score} ", align=ALIGN, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.updatescore()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("HighScoreFile.txt", mode="w") as data:
                data.write (f"{self.high_score}")
        self.score = 0
        self.updatescore()


    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)






