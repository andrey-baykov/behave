# from common import function, summ
import common

# Calculator_Alex
# a = int(input("Add first Number: "))
# b = int(input("Add second Number: "))
# c = int(input("Add third Number: "))
#
# print((a+b)/c)
# print((a*b)/c)
# print((a-b)/c)
from typing import List


# Home Work - Python (if - else, For It, While True )

# # Converter#1 for Miles and Kilometers
# print("For Convert Kilometers to Miles enter - 1")
# print("For Convert Miles to Kilometers enter - 2")
# choose = input('Please add your choose:  ')
# distance = int(input('Enter Distance: '))
#
# if choose == "1":
#     print(distance * 1.6)
# elif choose == "2":
#     print(distance * 0.6)
# else:
#     print("Invalid Value")
#
#
# # Converter#2 for Miles and Kilometers - with While
# while True:
#     print("Option#1 For Convert Kilometers to Miles enter - 1")
#     print("Option#2 For Convert Miles to Kilometers enter - 2")
#     print("Option#3 For Exit enter - 3")
#     choose = input('Please add your choose: ')
#
#     if choose == "1":
#         distance = int(input('Please enter your Distance in Km: '))
#         print(distance * 1.6)
#     elif choose == "2":
#         distance = int(input('Please enter your Distance in Mi: '))
#         print(distance * 0.6)
#     elif choose == "3":
#         break
#     else:
#         print("Alert:Invalid Value!")
#
#
# # For i - in range:
# for i in range(0, 7):
#     if i == 0:
#         print("Home wok is not ready")
#     elif i == 1:
#         print("1st Task is ready")
#     elif i == 2:
#         print("2nd - Task is ready")
#     elif i == 3:
#         print("3rd - Task is ready")
#     elif i == 4:
#         print("4th - Task is ready")
#     elif i == 5:
#         print("5th - Task is ready")
#     else:
#         print("Invalid")


# def function(text):
#     for i in text:
#         if i == 0:
#             print("Home wok is not ready")
#         elif i == 1:
#             print("1st - Task is ready")
#         elif i == 2:
#             print("2nd - Task is ready")
#         elif i == 3:
#             print("3rd - Task is ready")
#         elif i == 4:
#             print("4th - Task is ready")
#         elif i == 5:
#             print("5th - Task is ready")
#         else:
#             print("Invalid")


# numbers = [1, 3, 3, 4, 5, 1, 2, 5]
# res = function(numbers)
# print(res)
# res = function([1, 2, 3, 4, 5, 6, 7])
# print(res)
# function([0, 1, 2])

print(common.summ(1, 8))
