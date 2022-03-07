from ai import AI
from human import Human

class Showdown:
    def __init__(self):
        ai = AI
        human = Human

    def run_game(self):
        self.display_welcome

    def display_welcome(self):
        print("Lets get started, ready your hands.")
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock.")
        single_or_multi = input("Multiplayer or single player m/s: ")

    def battle(self):
        self.battle_ongoing = True
        while self.battle_ongoing == True:
            print("display gestures")
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