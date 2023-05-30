def proc1():

    input('Введите пароль.')
    print('Пароль принят' if input() == input() else 'Пароль не принят')


def proc2():

    n = int(input('Введите номер вашего места в плацкартном вагоне: '))
    print()
    if n > 54:
        print('Некорректно введен номер места')
    elif n > 36:
        print('Ваше место - боковое.')
    elif n % 2:
        print('Ваше место в купе внизу.')
    else:
        print('Ваше место в купе наверху.')


def proc3():

    year = int(input('Введите номер года: '))
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print('Год високосный')
    else:
        print('Год не високосный')

def proc4():

    a = ('Красный', 'Синий', 'Желтый')
    c1 = input()
    c2 = input()
    if c1 in a and c2 in a:
        if (c1 in ('Красный', 'Синий')) and (c2 in ('Красный', 'Синий')):
            print('Фиолетовый')
        if (c1 in ('Желтый', 'Синий')) and (c2 in ('Желтый', 'Синий')):
            print('Зеленый')
        if (c1 in ('Красный', 'Желтый')) and (c2 in ('Красный', 'Желтый')):
            print('Оранжевый')
    else:
        print('Цвет введен неверно')

proc1()
proc2()
proc3()
proc4()