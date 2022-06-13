class Banker:

    def __init__(self):
        self.shelved = 0
        self.balance = 0

    def shelf(self, shelved):
        self.shelved = int(shelved)

    def bank(self):

        self.balance += self.shelved
        self.shelf(0)
        return self.shelved