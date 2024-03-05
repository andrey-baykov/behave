# from time import sleep as sl
# import math
# import random
#
# for item in [1, 2, 3, 4, 5]:
#     sl(1)
#     print(item)
#
# x = math.sqrt(64)
# print(x)
#
# print(random.randint(1, 100))
# print(random.random())
def hello(name, age, sex="NA"):
    # age = input("Enter your " + name + " age: ")
    print("Hello,", name, "!", age, sex)


a = "Andrey"
hello(a, 17)
print("Hello,", a)

b = "Marina"
hello(b, 18, "F")
# print("Hello,", b)

c = "Alex"
hello(c, 19, "M")
# print("Hello,", c)

d = "Natalia"
hello(d, sex="F", age=20)
# print("Hello,", d)
