from common import function

print("My converter")


def calculate(data):
    print("The result is", data)


while True:
    user_input = input("Type 1 to convert miles to kilometers, \nType 2 to convert kilometers to miles, \nType 3 to "
                       "convert celsius to fahrenheit, \nType 4 to convert fahrenheit to celsius, \nEnter your choice: ")
    if user_input == "1":
        miles = float(input("Enter miles: "))
        result = miles * 1.8
        calculate(result)
    elif user_input == "2":
        km = float(input("Enter kilometers: "))
        result = km * 0.621371
        calculate(result)
    elif user_input == "3":
        celsius = float(input("Enter celsius: "))
        result = celsius * 9 / 5 + 32
        calculate(result)
    elif user_input == "4":
        fahrenheit = float(input("Enter fahrenheit: "))
        result = (fahrenheit - 32) / 1.8
        calculate(result)
    else:
        print("You entered wrong number: ", user_input)

    if input("Enter 'exit' to exit: ") == "exit":
        break

print("Thank you for using converter")

numbers = [1, 2, 3, 4, 5, 6, 7]
function(numbers)
