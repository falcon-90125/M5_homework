"""Функция fizz_buzz"""

def fizz_buzz(*args):
    result = 0
    for i in range(args[0], args[1]+1):
        if i % 3 == 0 and i % 5 == 0:
            result += i
    return result

print('1000-20000:', fizz_buzz(1000, 20000))


"""Функция plural_form"""
vol = 17
noun1 = 'яблоко'
noun2 = 'яблока'
noun3 = 'яблок'

def plural_form(vol, noun1, noun2, noun3):
    i = int(str(vol)[-2:])

    if i > 9 and i < 21 or i%10 > 4 and i%10 < 10:
        noun = noun3
    else:
        if i%10 == 1:
            noun = noun1
        else:
            noun = noun2

    return noun
    
print(vol, plural_form(vol, noun1, noun2, noun3))

'''Декоратор html'''
def html(param1='', **kwargs):
    def decorator(decorated_function):
        def wrapper_over_decorated_function(*args):
            # resalt_kwargs = str(kwargs)
            if kwargs:
                resalt_kwargs = ''
                for k, v in kwargs.items():
                    resalt_kwargs += f' {k}="{v}"'
            else:
                resalt_kwargs = ''
            resalt = str('<'+ param1 + resalt_kwargs + '>'+ decorated_function(*args) + '</' + param1 + '>')
            return resalt
        return wrapper_over_decorated_function
    # html_code = wrapper + {args}#  + {kwargs}
    return decorator


@html('body')
@html('div', width=200, height=100)
@html('a', href='https://yandex.ru/')
def to_string(input_value):
    return str(input_value)


print(to_string('ссылка на яндекс'))