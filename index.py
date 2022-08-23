"""Функция fizz_buzz"""
#возвращает сумму всех чисел от начала диапазона, до конца диапазона включительно, которые делятся без остатка и на 3 и на 5.
def fizz_buzz(*args):
    result = 0
    for i in range(args[0], args[1]+1): #принимает на вход начало диапазона (целое число) и конец диапазона (целое число). 
        if i % 3 == 0 and i % 5 == 0: 
            result += i
    return result

print('1000-20000:', fizz_buzz(1000, 20000))



"""Функция plural_form"""
#возвращает корректную форму существительного в зависимости от переданного числа.
vol = 17
noun1 = 'яблоко'
noun2 = 'яблока'
noun3 = 'яблок'

def plural_form(vol, noun1, noun2, noun3): #принимает на вход число и формы существительного
    i = int(str(vol)[-2:]) #получаем последние две цифры от числа любого размера, т.к. форма сущ-го зависит только от них

    if i > 9 and i < 21 or i%10 > 4 and i%10 < 10: #определяем диапазон от 5 до 20 для 3-ей формы
        noun = noun3
    else:  #остальные формы
        if i%10 == 1: #если цифра - единица, то 1я форма
            noun = noun1
        else: #оставшиеся цифры - 2я форма
            noun = noun2

    return noun
    
print(vol, plural_form(vol, noun1, noun2, noun3))



'''Декоратор html'''
#декоратор html принимает 1 позиционный аргумент и произвольное количество именованных аргументов.
#возвращает html-код
def html(param1='', **kwargs):
    def decorated_func(decorated_function): #декоратор функции to_string
        def wrapper_over_decorated_function(*args): #обёртка декоратора функции
            if kwargs: #есть получен именованный аргумент в декоратор
                resalt_kwargs = '' #собираем данные параментров
                for k, v in kwargs.items():
                    resalt_kwargs += f' {k}="{v}"'
            else: #если нет именованного аргумента, ни чего не передаём
                resalt_kwargs = ''
            #собираем в строку данные из входных параментров функции и декоратора
            resalt = str('<'+ param1 + resalt_kwargs + '>'+ decorated_function(*args) + '</' + param1 + '>')
            return resalt
        return wrapper_over_decorated_function
    return decorated_func

#позиционные и именованные аргументы декоратора
@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)
#вызов и вывод результата функции
print(to_string('ссылка на яндекс'))