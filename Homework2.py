# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

# num = input("Введите вещественное число: ")

# x = num.split(".")
# a = int(x[0])
# b = int(x[1])
# mult = 0
# while (a != 0):
#     mult = mult + (a % 10)
#     a = a // 10
# while (b != 0):
#     mult = mult + (b % 10)
#     b = b // 10
# print("Сумма цифр равна:", mult)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def factorial(n):
# 	result = 1
# 	i=1
# 	while i<=n:
# 		result*=i
# 		i+=1
# 	return result

# n = int(input('Enter a number: '))
# result = factorial(n)
# print(result)


# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# from msilib import sequence

# n = int(input('Введите число: ')) 

# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 5))


# 4.Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# 5.Реализуйте алгоритм перемешивания списка.

import time
test_list = [a for a in range(20)]
print('Начальный список : ' + str(test_list))
for i in range(len(test_list)):
    n=str(time.time())[-1]
    j=int(n)
    if j < len(test_list):
     test_list[i], test_list[j] = test_list[j], test_list[i]

print('Перемешанный список : ' + str(test_list))