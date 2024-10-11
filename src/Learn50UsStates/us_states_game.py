from turtle import Turtle, Screen
import pandas as pd
from constants import *


class UsStatesGame:
    screen: Screen
    text: Turtle
    correct_answers: int

    def __init__(self):
        self.data_us_states = pd.read_csv(STATES_FILE)
        self.all_state_list = self.data_us_states["state"].to_list()
        self.screen = Screen()
        self.screen.title("Learn U.S. states game")
        self.screen.setup(725, 491)
        self.screen.tracer(0)
        self.screen.bgpic(STATES_IMAGE_FILE)
        self.text = Turtle()

        self.text.hideturtle()
        self.text.penup()
        self.correct_answers = 0

    def update(self, answer="") -> bool:
        if answer == "":
            answer = self.screen.textinput(
                f"{self.correct_answers}/50 states correct",
                "What's another state name?",
            )
        if answer is None:
            new_data = pd.DataFrame(self.all_state_list)
            new_data.to_csv(STATES_MISSED_FILE)
            print(new_data)
            return False

        answer = answer.title()
        if answer in self.all_state_list:

            self.all_state_list.remove(answer)
            state_data = self.data_us_states[self.data_us_states.state == answer]
            self.text.goto(int(state_data.x.item()), int(state_data.y.item()))
            self.text.write(answer, move=True, align="left")
            self.correct_answers += 1
            if self.correct_answers == 50:
                return False
        else:
            print(f"wrong answer {answer}")
        self.screen.update()
        return True

    def run(self) -> None:
        is_game_on = True
        while is_game_on:
            is_game_on = self.update()
