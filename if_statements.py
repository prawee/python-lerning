# should_continue = True
# if should_continue:
#     print("Hello")

# know_people = ["John", "Anna", "Mary"]
# person = input("Enter the person you know: ")
# if person in know_people:
#     print("You know {}!".format(person))

# if person not in know_people:
#     print("You don't {}!".format(person))

## Exercise
def who_do_you_know():
    people = input("Enter the names of people you know, separated by commas: ")
    people_list = people.split(",")
    
    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())
    
    return people_list

def ask_user():
    person = input("Enter a name of someone you know: ")
    if person in who_do_you_know():
        print("You know this person!")

ask_user()