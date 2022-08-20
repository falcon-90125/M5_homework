"""Функция fizz_buzz"""

def fizz_buzz(*args):
    result = 0
    for i in range(args[0], args[1]+1):
        if i % 3 == 0 and i % 5 == 0:
            result += i
    return result

print('1000-20000:', fizz_buzz(1000, 20000))