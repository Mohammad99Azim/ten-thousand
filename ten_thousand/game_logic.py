import random


class GameLogic:

    @classmethod
    def is_three_pairs(cls, sorted_list_to_check):
        listee = sorted_list_to_check
        if len(sorted_list_to_check) == 6:
            x = listee.count(listee[0])
            y = listee.count(listee[2])
            z = listee.count(listee[4])
            if x == 2 and y == 2 and z == 2:
                return True
        return False

    @classmethod
    def count_of_sets(cls, my_list):
        cunt_score = 0

        count_1_sets = my_list.count(1)
        count_2_sets = my_list.count(2)
        count_3_sets = my_list.count(3)
        count_4_sets = my_list.count(4)
        count_5_sets = my_list.count(5)
        count_6_sets = my_list.count(6)

        if count_1_sets > 2:
            cunt_score += (count_1_sets - 2) * 1000
        if count_2_sets > 2:
            cunt_score += (count_2_sets - 2) * 200
        if count_3_sets > 2:
            cunt_score += (count_3_sets - 2) * 300
        if count_4_sets > 2:
            cunt_score += (count_4_sets - 2) * 400
        if count_5_sets > 2:
            cunt_score += (count_5_sets - 2) * 500
        if count_6_sets > 2:
            cunt_score += (count_6_sets - 2) * 600

        return cunt_score

    @classmethod
    def count_one_and_five(cls, my_list):
        my_score = 0
        count_1_sets = my_list.count(1)
        count_5_sets = my_list.count(5)

        if 0 < count_1_sets < 3:
            my_score += count_1_sets * 100

        if 0 < count_5_sets < 3:
            my_score += count_5_sets * 50

        return my_score

    @staticmethod
    def calculate_score(roll_dice):
        score = 0
        roll_dice = sorted(roll_dice)

        if roll_dice == [1, 2, 3, 4, 5, 6]:
            score += 1500
            return score
        elif GameLogic.is_three_pairs(roll_dice):
            score += 1500
            return score

        score += GameLogic.count_of_sets(roll_dice)

        score += GameLogic.count_one_and_five(roll_dice)

        return score

    @staticmethod
    def roll_dice(num):
        rolling = []
        rolling = [random.randint(1, 6) for x in range(0, num)]
        return rolling
