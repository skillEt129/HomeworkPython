#  Задание 2- Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# def is_prime(num):
#     if num < 2:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     limit = int(num**0.5) + 1
#     for divider in range(3, limit, 2):
#         if num % divider == 0:
#             return False
#     return True


# natural_n = int(input('Введите натуральное число N: '))
# prime_list = []

# for i in range(1, natural_n+1):
#     if natural_n % i == 0 and is_prime(i):
#         prime_list.append(i)

# print(f'Список простых делителей {natural_n}:\n', prime_list, sep='')

# Задание 1 Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = int(input('Введите точность: '))
# calc_pi = 0
# check = 0

# for n in range(int(10000)):
#     calc_pi += (1 / 16**n) * (4/(8*n + 1) - 2/(8*n + 4) - 1/(8*n + 5) - 1/(8*n + 6))
#     if abs(check - calc_pi) < 10**(-d):
#         break
#     check = calc_pi

# print('pi = ', round(calc_pi, d))




# - Задание 3 Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 

# import random as rnd


# def generate_lst(size: int) -> list:
#     rnd_lst = []
#     for _ in range(size):
#         nmb = round(-10 + 20 * rnd.random(), rnd.randint(0, 2))
#         if 0.3 > rnd.random():
#             nmb = int(nmb)
#         if 0.3 > rnd.random():
#             nmb = str(nmb)
#         rnd_lst.append(nmb)

#     return rnd_lst


# some_list = generate_lst(20)

# unique_list = []

# for item in some_list:
#     if some_list.count(item) == 1:
#         unique_list.append(item)

# print(f'Неповторяющиеся элементы ({len(unique_list)} шт.):', unique_list)
