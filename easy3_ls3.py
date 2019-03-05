#Задание 1 - функция получает имя, возраст и город и должна вывести строку
name = input('Введите свое имя: ')
age = int(input('Введите свой возраст: '))
city = input('Введите город в котором вы проживаете: ')

def names(name, age, city):
    print(f'{name.capitalize()}, {age} лет, живет в городе {city.title()}')

print(names(name, age, city))


# Задание 2 - написать функцию, возвращаемую максимальное значение среди
# 	# трех чисел

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

def max_value(a, b, c):
    return max(a, b, c)

print(max_value(a, b, c))

#  Задание 3 - написать функцию, принимающую любое количество аргументов и
# 	# возвращающую самую длинную строку

def max_len_string(*args):
    return max(args)
