def function(text):
    result = True
    for i in text:
        if i == 0:
            print("Home wok is not ready")
        elif i == 1:
            print("1st - Task is ready")
        elif i == 2:
            print("2nd - Task is ready")
        elif i == 3:
            print("3rd - Task is ready")
        elif i == 4:
            print("4th - Task is ready")
        elif i == 5:
            print("5th - Task is ready")
        else:
            print("Invalid")
            result = False

    return result


def summ(a, b):
    return a + b
