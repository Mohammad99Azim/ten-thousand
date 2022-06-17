from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:

    def __init__(self):
        self.round_counter = 0
        self.player_bank = Banker()
        self.dice_number = 6

    def play(self, roller=GameLogic.roll_dice):

        print('''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
        start_play = input('> ')
        if start_play[0] == 'n':
            print('OK. Maybe another time')
            return

        ###

        self.rolling_dice_text(self.dice_number, roller)
        self.user_input_handler(roller)

    def rolling_dice_text(self, dice_num, roller, print_start_round=1):
        if print_start_round == 1:
            self.round_counter += 1
            print(f'Starting round {self.round_counter}')
        random_dices = roller(dice_num)
        text = "*** "
        for x in random_dices:
            text += str(x) + " "
        text += "***"
        print(f'''Rolling {dice_num} dice...
{text}
Enter dice to keep, or (q)uit:''')

    def user_input_handler(self, roller):
        user_input_var = input("> ")
        if user_input_var == 'q':
            self.user_choose_quit()
        elif user_input_var == 'b':
            self.user_input_bank(roller)
            self.user_input_handler(roller)
        elif user_input_var == 'r':
            self.user_input_roll(roller)
            self.user_input_handler(roller)
        else:
            self.user_input_dice(user_input_var)
            self.user_input_handler(roller)

    def user_choose_quit(self):
        self.dice_number = 6
        print(f"Thanks for playing. You earned {self.player_bank.bank()} points")
        return

    def user_input_bank(self, roller):
        print(f'''You banked {self.player_bank.shelved} points in round {self.round_counter}
Total score is {self.player_bank.bank()} points''')
        self.dice_number = 6
        self.rolling_dice_text(self.dice_number, roller)

    def user_input_roll(self, roller):
        self.rolling_dice_text(self.dice_number, roller, 0)

    def user_input_dice(self, dice_picked):
        user_input_var = tuple(map(int, dice_picked))
        score_now = GameLogic.calculate_score(user_input_var)
        self.player_bank.shelf(score_now)
        self.dice_number -= len(user_input_var)
        print(f'''You have {self.player_bank.shelved} unbanked points and {self.dice_number} dice remaining
(r)oll again, (b)ank your points or (q)uit:''')


if __name__ == '__main__':
    one = Game()
    one.play()
    # rolling_dice_text(5)
