# -*- coding: utf-8 -*-
'''
Расставим все цифры в числе по убыванию — от наибольшей к наименьшей.
Например, 5707 преобразуем в 7750. Так мы получим новое число A.

Теперь сделаем наоборот: расставим все цифры в числе по возрастанию — от наименьшей к наибольшей.
Например, 5707 преобразуем в 0577 или просто 577. Так мы получим новое число B.

Вычитаем из числа A число B.
В нашем примере: 7750 - 577 = 7173.

Повторяем все шаги с полученным результатом вычитания.

'''

num = int(input('Введите 4х значное число!\n'))
print(num)

def ToLs(nm):
    '''Integer to list'''
    lst = [int(x) for x in str(nm)]
    return list(lst)

def ls_up(list):
    '''Sort Ascending'''
    list.sort()
    return int(''.join(map(str, list[::-1])))

def ls_dw(list):
    '''Sort in descending order'''
    list.sort()
    return int(''.join(map(str, list)))


while True:
    bkp = num
    ls1 = ToLs(num)
    num = ls_up(ls1) - ls_dw(ls1)
    print(num)
    if bkp == num:
        break