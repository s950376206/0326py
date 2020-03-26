
class Pikachu(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        super().__init__(new_name, new_weight, new_height, new_food, new_cp)

    def eat(self):
        print(f'The {self.__name()} is eating{self.__food()}.pika')

    def make_noise(self):
        print(f'{self.__name()} pika pika chu!')