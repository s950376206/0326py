class Member:
    def __init__(self, new_gender, new_major, new_id):
        self.__gender = new_gender  #gender>>private
        self.major = new_major
        self.id = new_id

    def join_class(self):
        pass

    def quit_class(self):
        pass

    def set_gender(self, new_gender):
        if new_gender == 'M' or new_gender == 'F':
            self.__gender = new_gender
        else:
            print('請輸入M或F')

    def get_gender(self):
        return self.__gender

    def borrow_resources(self):
        print('someone borrow')


class Student(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def join_class(self):
        pass

    def quit_class(self):
        pass

    def borrow_resources(self):
        print('student borrow')

class Professor(Member):
    def __init__(self, new_gender, new_major, new_id):
        super().__init__(new_gender, new_major, new_id)

    def borrow_resources(self):
        print('professor borrow')


studentA = Student('M', '工設系', 'B10721025')
studentB = Student('F', '創設系', 'B10711021')
profeccorA = Professor('F', '工管系', 'B10721139')
profeccorB = Professor('M', '工管系', 'B10721001')

Is = [studentA, studentB, profeccorA, profeccorB]

for item in Is:
    item.borrow_resources()
    print(item)