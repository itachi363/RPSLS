
from ai import AI
from human import Human

class Showdown:
    def __init__(self):
        self.ai = AI()
        self.player_one = Human()
        self.player_two = None


    def run_game(self):
        self.human.choose_gesture()
        self.display_welcome()
        Human.set_player_name()
        AI.set_name()

    def display_welcome(self):
        print("Lets get started, ready your hands.")
        print("Rock crushes Scissors, Scissors cuts Paper, Paper covers Rock, Rock crushes Lizard, Lizard poisons Spock, Spock smashes Scissors, Scissors decapitates Lizard, Lizard eats Paper, Paper disproves Spock, Spock vaporizes Rock.")
        # single_or_multi = input("Multiplayer or single player m/s: ")


    def determine_game_type(self):
        game_choice = int(f'input{self.player_one}, Enter the number to choose your oppenent: \n1-Computer\n2-Human Oppenent\nYour Selection')
        allowed_nums = [1,2]
        if game_choice in allowed_nums:
            if (game_choice == 1):
                self.player_two = AI()
                print(f' Oppenets confirmend: {self.player_one} vs. {self.player_two}')
            elif(game_choice == 2):
                self.player_two = Human()
                print(f' Oppents confirmed {self.player_one} vs. {self.player_two}')

        else:
            self.determine_game_type


    def create_round(self):
        while (self.player_one.wins < 2 and self.player_two.wins < 2):
         p1_choice = self.player_one.choose_gesture()
         p2_choice = self.player_two.choose_gesture()
        print(f'\n {self.player_one} chooses {p2_choice}')
        print(f'{self.player_two} chooses {p2_choice}')
        self.round_winner(p1_choice, p2_choice)

        if(self.player_one.wins == 2 or self.player_two.wins == 2):
            self.overall_winner()



    def
            
            
            
            
            
            
                # def battle(self):
    #     self.battle_ongoing = True
    #     while self.battle_ongoing == True:
    #         self.ai_turn

    #     if (p1_choice == p2_choice):
    #         print(f'  Tie no points awarded')
    #     elif(p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")):
                
            
        
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