my_variable = "hello"

# grade_one = 77
# grade_two = 80
# grade_three = 90
# grade_four = 95
# grade_five = 100
# print((grade_one + grade_two + grade_three + grade_four + grade_five) / 5)

grades = [77, 80, 90, 95, 100, 105, 107]
tuple_grades = (77, 80, 90, 95, 100, 105, 107, 108, 109) #immutable
set_grades = {77, 80, 90, 100, 100} #unique & unrodered

# print(sum(grades) / len(grades))
# print(tuple_grades)
# print(set_grades)

# grades.append(99)
# tuple_grades = tuple_grades + (100,)

set_grades.add(55)
set_grades.add(33)
# print(set_grades)

## set operations

your_lottery_numbers = {1,2,3,4,5}
winning_number = {1,3,5,7,9,11}

# print(your_lottery_numbers.intersection(winning_number))
# print(your_lottery_numbers.union(winning_number))
# print({1,2,3,4}.difference({1,2}))