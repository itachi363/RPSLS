from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"
    #     self.name = ""
    #     self.set_name


    # def set_name(self):
    #     self.name = "Computer"

    def choose_gesture(self):
        self.choice = random.choice(self.gesture_list)
        return self.choice

    def set_wins(self):
        self.wins += 1

    def _str_(self):
        return self.name    

