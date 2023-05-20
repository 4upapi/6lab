#Задание на л.р. №6
#Задание состоит из двух частей.
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов
# и целевую функцию для оптимизации решения.
#Вариант 30. Вводятся К цифр. Составьте все возможные целые числа из этих цифр. Каждая цифра используется только 1 раз.
import itertools
import math
print("Введите число K:",end='')
k = int(input())
col = 0
A = ''
poz = 0
mipoz = 9999
mich = 0
print("Часть 1")
print('============================')
for i in range(1,k+1):
    print("Введите "+str(i)+" цифру:",end='')
    ch = int(input())
    if len(str(ch)) == 1:
        A += str(ch)
    elif len(str(ch)) > 1:
        print("Введено число, введите цифру:",end='')
        ch = int(input())
        A += str(ch)
for j in range(1,k+1):
    f = itertools.permutations(A, j)
    for i in f:
        print('-'.join(i))
        col += 1
print("Всего комбинаций:",col)
print('============================')
print("Часть 2.1")
print('============================')
print('Вывести только чётные числа')
col = 0
for j in range(1,k+1):
    f = itertools.permutations(A, j)
    for i in f:
        if (int(''.join(i))) % 2 ==0:
            print(''.join(i))
            col += 1
print("Всего комбинаций при новом условии:",col)
print('============================')
print("Часть 2.2")
print('============================')
print('Найти первую позицию числа, факториал которого больше какого либо числа')
print('Введите какое нибудь число:',end='')
l = int(input())
for j in range(1,k+1):
    f = itertools.permutations(A, j)
    for i in f:
        poz += 1
        if math.factorial((int(''.join(i)))) > l:
            if poz < mipoz:
                mipoz = poz
                mich = ''.join(i)
print("Минимальная позиция:",mipoz)
print("Минимальное число:",mich)


