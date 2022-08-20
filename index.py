# """Функция fizz_buzz"""

# def fizz_buzz(*args):
#     result = 0
#     for i in range(args[0], args[1]+1):
#         if i % 3 == 0 and i % 5 == 0:
#             result += i
#     return result

# print('1000-20000:', fizz_buzz(1000, 20000))


"""Функция plural_form"""
i = 745
noun1 = 'яблоко'
noun2 = 'яблок'
noun3 = 'яблока'

def plural_form(i):
    i = str(i)
    i = int(i[-2:])

    if i > 4 and i < 21:
        noun = noun2
    else:
        i = str(i)
        i = int(i[-1])
        if i == 1:
            noun = noun1
        else:
            noun = noun3

    return noun

print(plural_form(i))