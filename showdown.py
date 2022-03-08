
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


    def create_round(self): # creates a round of gameplay. Best of 3
        while (self.player_one.wins < 2 and self.player_two.wins < 2):
            p1_choice = self.player_one.choose_gesture()
            p2_choice = self.player_two.choose_gesture()
            print(f'\n {self.player_one} chooses {p1_choice}')
            print(f'{self.player_two} chooses {p2_choice}')
            self.round_winner(p1_choice, p2_choice)

        if(self.player_one.wins == 2 or self.player_two.wins == 2):
            self.overall_winner()



    def round_winner(self, p1_choice, p2_choice): # Determine winner based on input
        if (p1_choice ==  p2_choice):
            print(f'  Tie no points awarded')
        elif(p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")):
            self.p1.wins(p1_choice, p2_choice)
        elif(p1_choice == "Paper" and (p2_choice == "Rock" or p2_choice == "Spock")):
            self.p1_wins(p1_choice, p2_choice)
        elif(p1_choice == "Scissors" and (p2_choice == "Paper" or p2_choice == "Lizard")):
            self.p1_wins(p1_choice, p2_choice)
        elif(p1_choice == "Lizard" and (p2_choice == "Paper" or p2_choice == "Spock")):
            self.p1_wins(p1_choice, p2_choice)  
        elif(p1_choice == "Spock" and (p2_choice == "Rock" or p2_choice == "Scissors")):
            self.p1_wins(p1_choice, p2_choice)   
        else:
            self.p2_wins(p1_choice, p2_choice)

    
    def p1_wins(self, p1_choice, p2_choice): # Selects winner output and win counter
        print(f'{p2_choice} beats {p1_choice}. {self.player_two} wins this round ! ')
        self.player_one.set_wins()  
            
            

    def p2_wins(self, p1_choice, p2_choice):
        print(f'{p2_choice} beats {p1_choice}. {self.player_one} wins this round ! ')
        self.player_two.set_wins()



    def overall_winner(self):
        if(self.player_one.wins == 2):
            print(f'{self.player_one} wins the game!')
        else:
            print(f'{self.player_two} wins the game!')
        self.play_again()


    def play_again(self): 
        decision = input('\n\nDo you want to play again? Y/N ')
        allowed_inputs = ['Y', 'y', 'N', 'n']
        if decision in allowed_inputs:
            if decision == 'Y' or decision == 'y':
                self.run_game()
            else:
                exit    
                
            
        
    # def ai_turn(self, ai):
    #     ai = self.ai.name
    #     self.ai.choose_gesture()
        

    # def human_turn(self, human):
    #     human = self.human.name
    #     self.human.choose_gesture()

    # def show_ai_options(self):
    #     pass

    # def show_human_options(self):
    #     pass

    # def display_winners(self):
    #     pass