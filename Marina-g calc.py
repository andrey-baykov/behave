# while True:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     sign = input("Enter sign: ")
#
#     if sign == "+":
#         print(a + b)
#     elif sign == "-":
#         print(a - b)
#     elif sign == "/":
#         if b == 0:
#             print("You can't divide by zero")
#         else:
#             print(a / b)
#     elif sign == "*":
#         print(a * b)
#     else:
#         print("Invalid sign")
#     user_input = input("exit: ")
#     if user_input == "Yes":
#         break
# print("Thank you for using")

# ===============================================================
# user_input = int(input("Enter your age: "))

# if user_input <21:
#     print("You are prohibited to drink alcohol")
# elif user_input >= 21 and user_input <65:
#     print("You are allowed to drink alcohol")
# else:
#     print("Too late")
# =============================================================
# for i in range(1, 100):
#     print(i)
#
# print("End of the loop")
# ==============================================================
# user_input = ""
# while user_input != "exit":
#     user_input = input("Enter something: ")
#     print("You entered:", user_input)
#
# print("End of while loop")
# =============================================================
#
# while True:
#     user_input = input("Enter something: ")
#     print("You entered: ", user_input)
#     if user_input == "exit":
#         break
#
# print("End of programme")
#
# ==============================================================

while True:
    answer = input(" Are you ready?: ")
    if answer == "no":
        print("Thank you for using")
        break
    while True:
        choice = input("Choose: \n1 if km -> miles, \n2 if miles -> km, \n3 if c -> f, \n4 if f -> c:"
                       " \nEnter you number : ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            break
        print("Mistake:", choice)
    if choice == "1":
        km = float(input("Enter the kilometers: "))
        ml = km / 1.609
        print("Miles", ml)
    elif choice == "2":
        ml = float(input("Enter the miles: "))
        kl = ml * 1.609
        print("Kilometers", kl)
    elif choice == "3":
        c = float(input("Enter the celsius: "))
        f = (c * 9 / 5) + 32
        print("Fahrenheit", f)
    else:
        f = float(input("Enter the fahrenheit: "))
        c = (f - 32)* 5/9
        print("Celsius", c)
