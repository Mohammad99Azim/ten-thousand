from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
from collections import Counter


class Game:

    def __init__(self):
        self.round_counter = 0
        self.player_bank = Banker()
        self.dice_number = 6
        self.random_dice = []


    def zilch(self,roller):
        self.dice_number = 6
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        self.player_bank.clear_shelf()
        self.user_input_bank(roller)


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
        self.random_dice = roller(dice_num)
        ###$random_dices = roller(dice_num)

        text = "*** "
        for x in self.random_dice:
            text += str(x) + " "
        text += "***"
        print(f'''Rolling {dice_num} dice...
{text}''')
        if GameLogic.calculate_score( self.random_dice) == 0:
            self.zilch(roller)
        else:
            print(f'''Enter dice to keep, or (q)uit:''')



    def check_hot_dice(self, roller):
        filter_roller = []
        if len(roller) > 2:
            if sorted(roller) == [1, 2, 3, 4, 5, 6]:
                self.dice_number = 6
                return
            if GameLogic.is_three_pairs(sorted(roller)):
                self.dice_number = 6
                return
            for element in roller:
                if element != 1 and element != 5:
                    filter_roller.append(element)
                    return
            if len(filter_roller) == 0:
                self.dice_number = 6
                return
            if GameLogic.count_of_sets(filter_roller) != 0:
                self.dice_number = 6
                return

    def user_input_handler(self, roller):
        user_input_var = input("> ")
        user_input_var = user_input_var.replace(" ", "")
        if user_input_var == 'q':
            self.user_choose_quit()
        elif user_input_var == 'b':
            self.user_input_bank(roller)
            self.user_input_handler(roller)
        elif user_input_var == 'r':
            self.user_input_roll(roller)
            self.user_input_handler(roller)
        else:
            self.user_input_dice(user_input_var, roller)
            self.check_hot_dice([int(i) for i in list(user_input_var)])
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

    def user_input_dice(self, dice_picked, roller):
        user_input_var = tuple(map(int, dice_picked))
        # cheating
        random_dice = self.random_dice
        int_roller_input = self.intersect_with_dup(random_dice, user_input_var)
        # print(random_dice)
        # print(int_roller_input)
        # print(list(user_input_var))
        if sorted(int_roller_input) != sorted(list(user_input_var)):
            print('Cheater!!! Or possibly made a typo...')
            text = "*** "
            for x in random_dice:
                text += str(x) + " "
            text += "***"
            print(text)
            print('Enter dice to keep, or (q)uit:')
            return self.user_input_handler(roller)

        score_now = GameLogic.calculate_score(user_input_var)
        self.player_bank.shelf(score_now)
        self.dice_number -= len(user_input_var)
        print(f'''You have {self.player_bank.shelved} unbanked points and {self.dice_number} dice remaining
(r)oll again, (b)ank your points or (q)uit:''')


    def intersect_with_dup(self, list1, list2):
        freq_random_dice = Counter(list1)
        freq_user_input = Counter(list2)
        set1 = set(list1)
        set2 = set(list2)
        list3 = list(set1 & set2)
        list4 = []
        for i in list3:
            list4.extend([i] * min(freq_random_dice[i], freq_user_input[i]))
        return list4

    # def cheat_detector(self,user_input_dice, roller):
    #     int_roller_input = tuple(set(user_input_dice) & set(roller))
    #     if int_roller_input != user_input_dice:
    #         print('Cheater!!! Or possibly made a typo...')


if __name__ == '__main__':
    one = Game()
    one.play()
    # rolling_dice_text(5)
    # print(one.check_hot_dice((1,2,3,4,5,6)))
