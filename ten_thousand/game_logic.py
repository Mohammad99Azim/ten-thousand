import random


class GameLogic:

    @staticmethod
    def create_obj_template(obj, tup):
        """
        Used to fill the obj dictionary with the base template for the numbers from 1-6, and counting the occurrences
            :param obj: dictionary
            :param tup: tuple
            :return: nothing
        """
        for i in range(1, 7):
            obj[f'num{i}'] = 0

        for i in tup:
            obj[f'num{i}'] += 1

    @staticmethod
    def calculate_score(tup):  # O(n) for time and space
        """
        This function takes a tuple of numbers from 1-6 and gives score on them according to the provided rules.
            :param tup: tuple of numbers
            :return: number
        """
        obj = {}
        score = 0
        straight_counter = 0
        three_pairs_counter = 0

    # Filling the obj dictionary with the base template for the numbers from 1-6, and counting the occurrences
        GameLogic.create_obj_template(obj, tup)

    # Conditions

        if obj['num1'] < 3:
            score += 100 * obj['num1']

        if obj['num1'] >= 3:
            score += (obj['num1'] - 2) * 1000

        if obj['num5'] < 3:
            score += 50 * obj['num5']

        for i in range(2, 7):
            if obj[f'num{i}'] >= 3:
                score += (100 * i) * (obj[f'num{i}'] - 2)

        for i in obj:
            if obj[i] == 1:
                straight_counter += 1
            if obj[i] == 2:
                three_pairs_counter += 1

        if straight_counter == 6:
            score = 1500

        if three_pairs_counter == 3:
            score = 1500

        return score

    @staticmethod
    def roll_dice(dice):
        """
        This method returns a tuple of randomly generated dice set.
        in this method used random module and use randint function to choose number between 1-6 randomly

        """

        if dice >=1 & dice <=6:

            dice_arr = []

            for i in range(dice):
                dice_num = random.randint(1, 6)
                dice_arr.append(dice_num)
            dice_tuple = tuple(dice_arr)
            return dice_tuple

