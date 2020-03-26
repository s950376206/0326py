class Pokemon:
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        self.__name = new_name
        self.__weight = new_weight
        self.__height = new_height
        self.__food = new_food
        self.__cp = new_cp

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_weight(self, new_weight):
        self.__weight = new_weight

    def get_weight(self):
        return self.__weight

    def set_height(self, new_height):
        self.__height = new_height

    def get_height(self):
        return self.__height

    def set_food(self, new_food):
        self.__food = new_food

    def get_food(self):
        return self.__food

    def set_cp(self, new_cp):
        self.__cp = new_cp

    def get_cp(self):
        return self.__cp

    def eat(self):
        print(f'The pokemon is eating{self.__food()}.')

    def make_noise(self):
        print('The pokemon is wow wow wow!')

class Pikachu(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        super().__init__(new_name, new_weight, new_height, new_food, new_cp)



    def eat(self):
        print(f'The {self.get_name()} is eating{self.get_food()}.pika')

    def make_noise(self):
        print(f'{self.get_name()} pika pika chu!')

class Squirtle(Pokemon):
    def __init__(self, new_name, new_weight, new_height, new_food, new_cp):
        super().__init__(new_name, new_weight, new_height, new_food, new_cp)



    def eat(self):
        print(f'The {self.get_name()} is eating{self.get_food()}.jenny jenny')

    def make_noise(self):
        print(f'{self.get_name()} jenny jenny!')


p = Pokemon('小邱', '50', '180', '飯', '0')
pp = Pikachu('皮卡丘', '10', '60', '水果', '50')
j = Squirtle('傑尼龜', '20', '50', '肉', '30')

ls = [p, pp, j]

for item in ls:
    item.make_noise()
