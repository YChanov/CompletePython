class User():
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f'attacking with power arrow. Arrows left: {self.arrows}')


player1 = Wizard('Merlin', 50)
player1.attack()

player2 = Archer('Robin', 100)
player2.attack()