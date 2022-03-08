from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "Computer"
   

    def choose_gesture_player_two(self):
        self.choice = random.choice(self.gesture_list)
        return self.choice

    def set_wins(self):
        self.wins += 1

    def _str_(self):
        return self.name    

    

