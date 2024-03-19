
a = 'a'
b = 'a'

# print(a / b)
# print(a // b)
# print(a ** b)
# print(a % b)


try:
    assert a == b, 'A not equal b'
    print(a / b)
except AssertionError:
    print('>>> AssertionError')
except ZeroDivisionError:
    print('>>> ZeroDivisionError')
except Exception as e:
    print('Something went wrong')
    print(e)

print("Another part of app")
