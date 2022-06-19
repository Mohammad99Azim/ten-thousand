from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker


class Game:
    def __init__(self):
        self.zilch = None

    @staticmethod
    def zilch():
        print("###########################################")
        print("###        Zilch!! Round over :(        ###")
        print("##########################################")

    def play(self, roller=GameLogic.roll_dice):
        round_counter = 1
        print('Welcome to Ten Thousand')
        print('(y)es to play or (n)o to decline')
        user_answer = input('> ')
        if user_answer == 'n':
            print('OK. Maybe another time')
        else:
            new_roller = Game.start_round_and_roll_dice(6, round_counter, roller)
            print('Enter dice to keep, or (q)uit:')
            user_answer = input('> ')
            if user_answer == 'q':
                print('Thanks for playing. You earned 0 points')
            else:
                shelved_amount = Banker()
                round_score = GameLogic.calculate_score(tuple(user_answer))
                shelved_amount.shelf(round_score)
                print(f'You have {round_score} unbanked points and '
                      f'{len(new_roller) - len(tuple(user_answer))} dice remaining')
                dice_remaining = len(new_roller) - len(tuple(user_answer))
                print('(r)oll again, (b)ank your points or (q)uit:')
                user_answer = input('> ')
                if user_answer == 'q':
                    print(f'Thanks for playing. You earned {round_score} points')
                if user_answer == 'b':
                    shelved_amount.bank()
                    print(f'You banked {round_score} points in round {round_counter}')
                    round_counter += 1
                    print(f'Total score is {shelved_amount.balance} points')
                    Game.start_round_and_roll_dice(6, round_counter, roller)
                    print('Enter dice to keep, or (q)uit:')
                    user_answer = input('> ')
                    if user_answer == 'q':
                        print(f'Thanks for playing. You earned {round_score} points')
                        return

                    # bank_first_for_two_rounds
                    round_score = GameLogic.calculate_score(tuple(user_answer))
                    shelved_amount.shelf(round_score)
                    print(f'You have {round_score} unbanked points and '
                          f'{len(new_roller) - len(tuple(user_answer))} dice remaining')
                    dice_remaining = len(new_roller) - len(tuple(user_answer))
                    print('(r)oll again, (b)ank your points or (q)uit:')
                    user_answer = input('> ')
                    if user_answer == 'q':
                        print(f'Thanks for playing. You earned {round_score} points')

                    if user_answer == 'b':
                        shelved_amount.bank()
                        print(f'You banked {round_score} points in round {round_counter}')
                        round_counter += 1
                        print(f'Total score is {shelved_amount.balance} points')
                        Game.start_round_and_roll_dice(6, round_counter, roller)
                        print('Enter dice to keep, or (q)uit:')
                        user_answer = input('> ')
                        if user_answer == 'q':
                            print(f'Thanks for playing. You earned {shelved_amount.balance} points')
                            return

                # repeated_roller
                if user_answer == 'r':
                    new_roller2 = Game.repeat_roller(dice_remaining, roller)
                    print('Enter dice to keep, or (q)uit:')
                    user_answer = input('> ')
                    if user_answer == 'q':
                        print(f'Thanks for playing. You earned {round_score} points')
                    else:
                        shelved_amount = Banker()
                        round_score += GameLogic.calculate_score(tuple(user_answer))
                        shelved_amount.shelf(round_score)
                        print(f'You have {round_score} unbanked points and '
                              f'{len(new_roller2) - len(tuple(user_answer))} dice remaining')
                        print('(r)oll again, (b)ank your points or (q)uit:')
                        user_answer = input('> ')
                        if user_answer == 'b':
                            shelved_amount.bank()
                            print(f'You banked {round_score} points in round {round_counter}')
                            round_counter += 1
                            print(f'Total score is {round_score} points')
                            Game.start_round_and_roll_dice(6, round_counter, roller)
                            print('Enter dice to keep, or (q)uit:')
                            user_answer = input('> ')
                            if user_answer == 'q':
                                print(f'Thanks for playing. You earned {round_score} points')

    @classmethod
    def start_round_and_roll_dice(cls, dice_roll_num, round_number, roller):
        print(f'Starting round {round_number}')
        print('Rolling 6 dice...')
        new_roller = roller(dice_roll_num)
        formatted_roller = ' '.join([str(i) for i in new_roller])
        print(f'*** {formatted_roller} ***')
        cls.zilch = cls.game_logic.calculate_score(cls.new_roller)
        if cls.zilch == 0:
            Game.zilch()
            cls.banker.clear_shelf()
        if cls.zilch != 0:
            print("Enter dice to keep, or (q)uit:")


        return new_roller

    @classmethod
    def repeat_roller(cls, dice_roll_num, roller):
        print(f'Rolling {dice_roll_num} dice...')
        new_roller2 = roller(dice_roll_num)
        formatted_roller = ' '.join([str(i) for i in new_roller2])
        print(f'*** {formatted_roller} ***')

        return new_roller2


if __name__ == '__main__':
    game = Game()
    game.play()
