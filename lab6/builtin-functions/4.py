import time

def func(number, milliseconds):
    start = time.time() * 1000
    end = start + milliseconds

    while time.time() * 1000 < end:
        pass

    return number ** 0.5

number = int(input())
milliseconds = int(input())
result = func(number, milliseconds)
print("Square root of {} after {} milliseconds is {}".format(number, milliseconds, result))
