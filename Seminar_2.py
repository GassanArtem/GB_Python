# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = int(input('PLease enter a number: '))
summa = 0
while number > 0:
    digit = number % 10
    summa += digit
    number //= 10
print(summa)




# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

number = int(input('PLease enter a number: '))
a = 1
for i in range(number):
    i = i + 1
    a = i * a
    print(a, end=" ")




# Задайте словарь из n чисел последовательности (1 + (1/n))^n и выведите на экран их сумму.

n = int(input())
lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')




# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
x = open('file.txt','r')
result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
print(result)
