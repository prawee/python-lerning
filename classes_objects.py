lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (5, 9, 12, 3, 1, 21)
}

class LotterPlayer: 
    def __init__(self): 
        self.name = 'Rolf',
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)

player_one = LotterPlayer()
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotterPlayer()

# print(player_one.name)
# print(player_one.total())

# print(player_one.name == player_two.name)
print(player_one.numbers == player_two.numbers)

class Student: 
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school():
        print("I'm going to school.")

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")

anna.marks.append(56)
anna.marks.append(71)
Student.go_to_school()