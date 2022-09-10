# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.

number = input('Введите любое число: ')
sum = 0
for i in number:
    if i != '.':
        sum+= int(i)
print(f'Cумма цифр числа равна: {sum}')


# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

n = int(input('Введите число: '))
factorial = 1
list = []
for i in range(1, n+1):
    list.append(factorial * i)
    factorial *= i
print(f'Набор произведений чисел от 1 до {n} = {list}')


# Задайте список из n чисел последовательности 
# (1+1/n)**n и выведите на экран их сумму.

n = int(input('Введите число: '))
sum = 0
for i in range(1, n + 1):
    sum += (1 + 1 / i) ** 1
print(sum)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся 
# в файле file.txt в одной строке одно число.

from random import *

z = int(input('Введите число: '))
list_3 = [randint(-z, z) for _ in range(5, 10)]
print(list_3)
f = open ('taskPY.txt', 'w')
for i in range(randint(2, len(list_3))):
    f.write(str(randint(0, len(list_3) - 1)) + '\n')
f.close()

pr = 1
with open ('taskPY.txt', 'r') as f:
    for i in f.read().splitlines():
        pr = pr * list_3[int(i)]
print(pr)


# Реализуйте алгоритм перемешивания списка.

# from random import shuffle
# list_1 = [1, 2, 3, 4, 5, 6]
# print(f'Список до перемешивания: {list_1}')
# shuffle(list_1)
# print(f'Список после перемешивания: {list_1}')




