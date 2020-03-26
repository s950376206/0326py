class Drink:
    def __init__(self, new_name, new_price):
        self.__name = new_name
        self.__price = new_price

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def set_price(self, new_price):
        self.__price = new_price

    def get_price(self):
        return self.__price