from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}", align='center', font=("Arial", 24, 'normal'))


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align='center', font=("Arial", 24, 'normal'))





