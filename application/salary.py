import datetime
from time import strftime


now_time = (datetime.datetime.now())
now_time_str = now_time.strftime("%d-%m-%Y   Время: %H:%M")


def calculate_salary():
    print(f'Текущая дата: {now_time_str}')
    print('Здесь работа функции calculate_salary()')



