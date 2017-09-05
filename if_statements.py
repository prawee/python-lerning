# should_continue = True
# if should_continue:
#     print("Hello")

know_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")
if person in know_people:
    print("You know {}!".format(person))

if person not in know_people:
    print("You don't {}!".format(person))