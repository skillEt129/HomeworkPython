#1 - Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#*Пример:*

 #[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# some_lst = [randint(0, 10) for _ in range(10)]
# result = 0

# for i in range(1, len(some_lst), 2):
#     result += some_lst[i]
# print(some_lst)
# print(result)

#2 - Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#*Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint

# some_lst = [randint(0, 10) for _ in range(11)]
# result = []
# for i in range((len(some_lst) + 1) // 2):
#     result.append(some_lst[i] * some_lst[len(some_lst) - 1 - i])

# print(some_lst)
# print(result)

# 3 - Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# -  [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# import random


# def generate_lst():     # генератор списка вещественных чисел
#     rnd_lst = []
#     for _ in range(10):
#         nmb = 10 * random.random()     # диапазон 0...9.(9)
#         if 0.3 > random.random():
#             nmb = int(nmb)
#         rnd_lst.append(round(nmb, random.randint(0, 4)))
#     return rnd_lst

# some_lst = generate_lst()
# print(some_lst)
# n_max = n_min = 0
# for item in some_lst:
#     if isinstance(item, float):
#         f_part = (str(item).split('.'))[1]
#         num = int(f_part)
#         num /= 10**len(str(f_part))
#         if n_max < num:
#             n_max = num
#         if n_min > num != 0 or n_min == 0:
#             n_min = num

# print(f'{n_max} - {n_min} = {n_max - n_min}')


# 4 - Напишите программу, которая будет преобразовывать десятичное число 
# в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# while True:
#     dec_num = int(input('Введите десятичное целое число (или -1 для выхода): '))
#     print(dec_num)
#     if dec_num == -1:
#         break
#     bin_num = '0' if dec_num == 0 else ''

#     while dec_num:
#         bin_num = str(dec_num % 2) + bin_num
#         dec_num //= 2

#     print(int(bin_num, 2), '->', bin_num)


# 5 - Задайте число. Составьте список чисел Фибоначчи,
#  в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib2(num):
    fib_posi = [0, 1]
    for i in range(2, num+1):
        fib_posi.append(fib_posi[i-1] + fib_posi[i-2])

    fib_nega = []
    for i in range(0, num+1):
        fib_nega.append((fib_posi[i] * (-1)**(i + 1)))

    return fib_nega[-1:1:-1] + fib_posi


print(fib2(8))