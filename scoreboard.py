from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Monospace", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 330)
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())

        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()

