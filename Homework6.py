# Задание 1

a = 'Мама сшила м0не штаны и7з бере9зовой кор45ы 893.'
res = ' '.join(list(filter(lambda word: all(map(lambda c: c.isalpha(), word)), a.split())))
print(res)

# 2- Найти сумму чисел списка стоящих на нечетной позиции

from functools import reduce


my_numbers = [2, 5, 6, 3, 2, 1, 9]

result = reduce(lambda x, y: x + y, my_numbers[::2])
print(result)

#  Задание 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

from functools import reduce
p1 = list(map(int, input('Введите координаты первой точки: ').split()))
p2 = list(map(int, input('Введите координаты второй точки: ').split()))
d = reduce(lambda a, b: (a + b)**(1/2),(map(lambda p: (p[1] - p[0])**2, zip(p1, p2))))
print(f'Расстояние = {round(d,2)}')

# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

list_string = ["qwe", "asd", "zxc", "qwe", "ertqwe"]# ищем: "qwe", ответ: 3
find_obj = "qwe"

list_string = list(enumerate(list_string))

new_list = list(filter(lambda x: x[1] == "qwe", list_string))
print(f"Ищем {find_obj}, ответ: {new_list[1][0]}")

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from functools import reduce
import math

my_nums = [1, 2, 3, 4, 5, 6, 7]

len_list = round(len(my_nums)/2)
first_list = my_nums[:len_list]
sec_list = my_nums[len_list:]

sec_list = sec_list[::-1]

if len(first_list) > len(sec_list):
    sec_list.append(first_list[len(first_list) - 1])

new_list = list(zip(first_list, sec_list))

new_list = list(map(lambda x, y: x * y, first_list, sec_list))
print(new_list)

# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

from functools import reduce

def Calc(inpt, el):
    print (inpt, el)
    return inpt * el * -3

N = int(input("Введите N: "))

m_list = [1] * N

f = lambda x, y: x * y * (-3)

for i in range(1,len(m_list)):
    m_list[i] = f(m_list[i], m_list[i-1])
print(m_list)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security