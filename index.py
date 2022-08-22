"""Функция fizz_buzz"""

def fizz_buzz(*args):
    result = 0
    for i in range(args[0], args[1]+1):
        if i % 3 == 0 and i % 5 == 0:
            result += i
    return result

print('1000-20000:', fizz_buzz(1000, 20000))


"""Функция plural_form"""
i = 3

def plural_form(i, **kwargs):
    noun1 = kwargs.get('noun1', '')
    noun2 = kwargs.get('noun2', '')
    noun3 = kwargs.get('noun3', '')
    i = int(str(i)[-2:])

    if i > 9 and i < 21 or i%10 > 4 and i%10 < 10:
        noun = noun2
    else:
        if i%10 == 1:
            noun = noun1
        else:
            noun = noun3

    return noun

print(str(i) + ' ' + plural_form(i, noun1='яблоко', noun2='яблок', noun3='яблока'))