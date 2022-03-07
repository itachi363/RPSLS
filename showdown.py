from ai import AI
from human import Human

class Showdown:
    def __init__(self):
        self.ai = AI()
        self.human = Human()

    def run_game(self):
        self.human.choose_gesture()
        self.display_welcome()
        Human.set_player_name()
        AI.set_name()

    def display_welcome(self):
        print("Lets get started, ready your hands.")
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock.")
        single_or_multi = input("Multiplayer or single player m/s: ")

    def battle(self):
        self.battle_ongoing = True
        while self.battle_ongoing == True:
            self.ai_turn

        if (p1_choice == p2_choice):
            print(f'  Tie no points awarded')
            # elif(p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")):
            
        
    def ai_turn(self, ai):
        ai = self.ai.name
        self.ai.choose_gesture()
        

    def human_turn(self, human):
        human = self.human.name
        self.human.choose_gesture()

    def show_ai_options(self):
        pass

    def show_human_options(self):
        pass

    def display_winners(self):
        pass