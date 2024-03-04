while True:
    answer = input("Enter 'exit' to stop or press 'Enter' to continue: ")
    if answer == "exit":
        break

    while True:
        choice = input("Choose: \n1 if mile -> km, \n2 if km -> mile: \nEnter your choice: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "5":
            break
        print("You entered wrong number:", choice)

    a = int(input("Add first Number: "))
    b = int(input("Add second Number: "))
    sign = input("Enter sign: ")

    if sign == "+":
        print(a + b)
    elif sign == "-":
        print(a - b)
    elif sign == "/":
        if b == 0:
            print("You can't divide by 0")
        else:
            print(a / b)
    elif sign == "*":
        print(a * b)
    else:
        print("Invalid sign")

print("Thank you for using my calculator")

# == равно
# != не равно
# > больше
# < меньше
# >= больше или равно
# <= меньше или равно

# a = True
#
# if a:  # if a == True
#     print("a is True")
#
# if not a:  # if a == False
#     print("a is False")

# =============================================

# user_input = int(input("Enter your age: "))
#
# if user_input < 21:
#     print("You are not allowed to drink alcohol")
# elif user_input >= 21 and user_input < 65:
#     print("You are allowed to drink alcohol")
# else:
#     print("Too late")

# And
# True and True   -> True
# True and False  -> False
# False and True  -> False
# False and False -> False

# Or
# True or True   -> True
# True or False  -> True
# False or True  -> True
# False or False -> False

# Not
# not True  -> False

"""
Don't
Repeat
Yourself
"""
#         True                  False -> True
# if user_input > 21 and not user_input > 65:
#     print("You are not allowed to drink alcohol")
#
#         True                  True -> False
# if user_input > 21 and not user_input > 65:
#     print("You are not allowed to drink alcohol")
#
#  3        False                       True
#                             False           True
# if user_input > 21 and user_input > 65 or user_input < 5:
#     print("You are not allowed to drink alcohol")
#
#                 False                           True
#   3        False          False
# if (user_input > 21 and user_input > 65) or user_input < 5:
#     print("You are not allowed to drink alcohol")

