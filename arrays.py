# number_1 = 12
# number_2 = 3
# number_3 = 5
# number_4 = 7
# number_5 = 9

# list
# numbers_l = [12, 3, 3, 5, 7, 9]
# print(numbers_l)
# numbers.append(6)
# print(numbers)
# numbers.pop(0)
# print(numbers)

#  0  1  2  3  4
# -5 -4 -3 -2 -1

# print(len(numbers))
# print(numbers[len(numbers) - 1])

# print(numbers[-2])

# tuple
# numbers_t = (12, 3, 3, 5, 7, 9)
# print(numbers_t)

# set
# numbers_s = {12, 3, 3, 5, 7, 9}
# print(numbers_s)
#
# print(set(numbers_l))
# print(tuple(numbers_s))
# print(list(numbers_t))
#
# x = numbers_l[0] - numbers_t[1]
# print(x)

# dictionary
# key: value

# person = ["Andrey", 40, "M"]
#
# person_d = {
#     "name": "Andrey",
#     "age": 40,
#     "sex": "M"
# }
#
# print(person_d)
# print(person_d["name"])
# print(person_d["age"])
# print(person_d["sex"])
#
# person_d["name"] = "Alex"
# print(person_d["name"])

numbers_l = ["Andrey", 3, "Marina", 5, "Alex", 9, "Natalia"]
for item in numbers_l:
    print(item)

choice = ["1", "2", "3", "4"]

if "ello" in "Hello":
    print("Yes")
