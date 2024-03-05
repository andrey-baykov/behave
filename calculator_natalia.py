print("My converter")

while True:
    user_input = input("Type 1 to convert miles to kilometers, \nType 2 to convert kilometers to miles, \nType 3 to "
                       "convert celsius to fahrenheit, \nType 4 to convert fahrenheit to celsius, \nEnter your choice: ")

    if user_input == "1":
        miles = float(input("Enter miles: "))
        print("The result is ", miles * 1.8, "kilometers")
    elif user_input == "2":
        km = float(input("Enter kilometers: "))
        print("The result is ", km * 0.621371, "miles")
    elif user_input == "3":
        celsius = float(input("Enter celsius: "))
        print("The result is ", celsius * 9 / 5 + 32, "fahrenheit")
    elif user_input == "4":
        fahrenheit = float(input("Enter fahrenheit: "))
        print("The result is ", (fahrenheit - 32) / 1.8, "celsius")
    else:
        print("You entered wrong number: ", user_input)

    if input("Enter 'exit' to exit: ") == "exit":
        break

print("Thank you for using converter")
