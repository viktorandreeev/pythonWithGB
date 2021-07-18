"""
Урок 1. Задание 1.
"""

duration = int(input('Введите число: '))

week = 604800
day = 86400
hour = 3600
minute = 60

while duration > week: #ограничиваем работу программы до 7 дней
    duration = int(input('Введите число меньше или равно 604800: '))

if duration < minute:
    duration_s = duration % minute
    print(f'{duration_s}сек')
elif duration < hour:
    duration_m = (duration % hour) // minute
    duration_s = duration % minute
    print(f'{duration_m}мин, {duration_s}сек')
elif duration < day:
    duration_h = (duration % day) // hour
    duration_m = (duration % hour) // minute
    duration_s = duration % minute
    print(f'{duration_h}ч, {duration_m}мин, {duration_s}сек')
else:
    duration_d = duration // day
    duration_h = (duration % day) // hour
    duration_m = (duration % hour) // minute
    duration_s = duration % minute
    print(f'{duration_d}дн, {duration_h}ч, {duration_m}мин, {duration_s}сек')

