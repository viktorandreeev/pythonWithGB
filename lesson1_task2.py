"""
Урок 1. Задание 2.
"""

for i in range(1, 1001, 2):
    sum = 0
    k = (i ** 3) + 17
    print(f'i = {i} i^3 = {k}')
    while k > 0:
        m = k % 10
        sum = sum + m
        k = k // 10
        no_surplus = sum % 7
        #print(f'сумма = {sum}')
    if no_surplus == 0:
        print(f'i = {i} | сумма = {sum}')