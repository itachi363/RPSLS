import imp
from scissors import Scissors
from paper import Paper
from rock import Rock
from lizard import Lizard
from spock import Spock
from ai import AI
from human import Human

class Showdown:
    def __init__(self):
        scissor = Scissors
        paper = Paper
        rock = Rock
        lizard = Lizard
        spock = Spock
        ai = AI
        human = Human

    def run_game(self):
        self.display_welcome

    def display_welcome(self):
        print("Lets get started, ready your hands.")

    def battle(self):
        self.battle_ongoing = True
        while self.battle_ongoing == True:
            pass

    def ai_turn(self, AI):
        pass

    def human_turn(self, human):
        pass

    def show_ai_options(self):
        pass

    def show_human_options(self):
        pass

    def display_winners(self):
        pass