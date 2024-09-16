# both are ways to add logic inside a class, but can be called without instantiating the class
# classmethod has access to the class itself (cls)
# staticmethod does not have access ti the class

class PlayerCharacter:
    membership = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    def run(self):
        print('run')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Yavor', 30)

print(player1.adding_things(2,5))
print(PlayerCharacter.adding_things(2,8))