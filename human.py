from player import Player
import random

class Human(Player):
    def __init__(self):
        super().__init__()
        self.set_player_name()
            
    def set_player_name(self):
        self.name = input (f' Please enter your name here: ')


    def choose_gesture(self):
        self.choice = int(input(f'\n1-rock\n2-paper\n3-scissors\n4-lizard\n5-spock\nYour Choice (enter the digit next to your choice: '))
        allowed_nums = [1,2,3,4,5]
        if self.choice in allowed_nums:
            return self.gesture_list[self.choice -1]

        else:
            self.choose_gesture()

    

    def set_wins(self):
        self.wins += 1

    def _str_(self):
        return self.name

        # call_function = choose_gesture()
    
            