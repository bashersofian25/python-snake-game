from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

    def write_score(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"score : {self.score} ", False, "center", font=('Arial', 20, 'normal'))
        self.hideturtle()

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"score : {self.score} ", False, "center", font=('Arial', 20, 'normal'))
        self.hideturtle()


    def write_gg(self):
        self.penup()
        self.goto(0, 0)
        self.pencolor("white")
        self.write(f"GAME OVER\nyour score is : {self.score}", False, "center", font=('Arial', 30, 'normal'))










