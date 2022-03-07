from player import Player

# class Human:
#     def __init__(self):
#         self.name = "player"
#         super().__init__(self)

class Human(Player):
        def __init__(self):
            super().__init__()
            self.name = 
            pass

            
        def set_player_name(self):
            self.name = input (f' Please enter your name here')


        def choose_gesture(self):
            self.choice = int(input)
            allowed_nums = []
            if self.choice in allowed_nums:
                return self.gesture_list[self.choice -1]

            else:
                self.choice_gesture()



        def set_wins(self):
            self.wins += 1

        def _str_(self):
            return self.name

            