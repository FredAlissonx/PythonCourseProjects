from dice_game.die import Die
from dice_game.player import Player


class DiceGame:
    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def print_round_welcome(self):
        print("-------- New Round --------")
        input(" Press any key to roll the dice. \n")

    def play(self):
        print("""
========================================
    -- Welcome to Roll the Dice --
========================================
        """)

        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):

        self.print_round_welcome()
        # Roll the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        self.show_dice(player_value, computer_value)

        if player_value > computer_value:
            print("You won the round!")
            self.update_counters(winner=self._player, loser=self._computer)
        elif player_value < computer_value:
            print("The computer won this round. Try again!")
            self.update_counters(winner=self._computer, loser=self._player)
        else:
            print("It's a tie!")

        self.show_counters()

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")

    def update_counters(self, winner, loser):
        winner.increment_counter()
        loser.decrement_counter()

    def show_counters(self):
        print(f"You counter: {self._player.counter}")
        print(f"Computer counter: {self._computer.counter}\n")

    def check_game_over(self):
        if self._player.counter == 0:
            self.show_game_over(winner=self._player)
            return True
        elif self._computer.counter == 0:
            self.show_game_over(winner=self._computer)
            return True
        else:
            return False

    def show_game_over(self, winner):
        if winner.is_computer:
            print("""
\n======================
    G A M E  O V E R 
======================
The computer won the game.
======================            
            """)
        else:
            print("""
\n======================
    G A M E  O V E R 
======================
You won the game! Congratulations.
======================  
""")


player_die = Die()
computer_die = Die()
my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)
game = DiceGame(player=my_player, computer=computer_player)
game.play()