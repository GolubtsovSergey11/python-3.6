
def input_data(number=False):
    """Заполняем данные по зарплате"""
    solary = {}
    if not number:
        number = int(input('Как много сотрудников у вас работает? : '))
    for _ in range(number):
        key = input('Введите имя сотрудника : ').upper()
        value = float(input('Введите его зарплату : '))
        solary[key] = value
    return solary


def save_result(solary, file_name='solary.txt'):
    """Записываем данные в файл в необходимом формате"""
    with open(file_name, "w") as file:
        for key, value in solary.items():
            string = key + ' - ' + str(value) + '\n'
            file.write(string)
    return True


def load_result(file_name='solary.txt'):
    """Читаем файл и выводим результат в список"""
    with open(file_name) as file:
        file_info = file.readlines()
    return file_info


def filter_solary(strings):
    """Выводим результат с фильтрацией данных по зарплате"""
    for string in strings:
        date = string.split(' ')
        solary = float(date[2])
        solary -= solary*0.13
        if solary < 50000:
            date[2] = solary
            print(date[0], ' - ', date[2])



personal = input_data()
save_result(personal)
print('Данные занесены в файл. Чтобы вывести результат, нажмите ввод.')
input()
personal = load_result()
filter_solary(personal)