# #  Задание 2- Создайте программу для игры с конфетами человек против человека.

# # Условие задачи: На столе лежит 2021 конфета. 
# # Играют два игрока делая ход друг после друга. 
# # Первый ход определяется жеребьёвкой. За один ход можно забрать не более 
# # чем 28 конфет. Тот, кто берет последнюю конфету - проиграл.
# # a) Добавьте игру против бота
# # b) Подумайте как наделить бота ""интеллектом""

# from random import randint

# CANDIES_ON_TABLE = 2021
# # CANDIES_ON_TABLE = 121    # testing value
# AMT_MAX = 28
# names = tuple()
# mode = ''

# def game_play() -> None:
#     """basic logic"""
#     global names
#     candies = CANDIES_ON_TABLE
#     person = randint(0, 1)
#     flag = 1
#     while flag:
#         print(f'Конфет на столе: {candies}')
#         if mode == '1':
#             if person:
#                 num_take = human(person)
#                 if num_take > 28 or num_take < 0:
#                     num_take = AMT_MAX
#             else:
#                 num_take = ai_player(candies)
#         else:
#             num_take = human(person)
#             if num_take > 28 or num_take < 0:
#                 num_take = AMT_MAX

#         if candies <= 28:
#             print(f'{names[person]} забирает {candies} конфет.')
#         else:
#             print(f'{names[person]} берёт {num_take} конфет.')
#         candies -= num_take
#         if candies <= 0:
#             print(f'{names[person]} победил')
#             flag = 0
#         person = (person + 1) % 2


# def ai_player(candies: int) -> int:
#     """primitive AI"""
#     if candies < 28:
#         return candies
#     elif candies - 28 > 1 and candies < 28 * 2:
#         return candies - 27
#     else:
#         return 28


# def human(pers: int) -> int:
#     """human capture"""
#     global names
#     return int(input(f'Сколько конфет берёте (0 min, 28 max), {names[pers]}? '))


# def intro():
#     print(
#         '''
#         Играем в конфеты. 
#         Полиси: можно взять от 0 до 28 штук.
#         Если взять меньше 0 (интересный вариант...) или больше 28,
#         считается что взял 28. Поехали.    
#     '''
#         )

#     flag_0 = 1
#     global mode
#     global names
#     while flag_0:
#         mode = input('Играем с компьютером или на двоих? (1/2/exit): ')
#         if mode == 'exit':
#             print('Выход')
#             raise SystemExit
#         elif mode not in ('1', '2'):
#             print('Ошибка ввода.')
#         else:
#             flag_0 = 0

#     if mode == '1':
#         names = ('An artificial one', input('Введите имя: '))
#     else:
#         names = (input('Введите имя 1-го игрока: '), input('Введите имя 2-го игрока: '))

#     game_play()


# intro()




#  Задача 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]

# 4 Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('file_encode.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

with open('file_encode.txt', 'r') as data:
    string = data.readline()

def rle_encode(decoded_string):
    encoded_string = ''
    count = 1
    char = decoded_string[0]
    for i in range(1, len(decoded_string)):
        if decoded_string[i] == char:
            count += 1
        else:
            encoded_string = encoded_string + str(count) + char
            char = decoded_string[i]
            count = 1
            encoded_string = encoded_string + str(count) + char
    return encoded_string


def rle_decode(encoded_string):
    decoded_string = ''
    char_amount = ''
    for i in range(len(encoded_string)):
        if encoded_string[i].isdigit():
            char_amount += encoded_string[i]
        else:
            decoded_string += encoded_string[i] * int(char_amount)
        char_amount = ''
    print(decoded_string)

    return decoded_string


with open('file_encode.txt', 'r') as file:
    decoded_string = file.read()

with open('file_decode.txt', 'w') as file:
    encoded_string = rle_encode(decoded_string)
    file.write(encoded_string)

print('Decoded string: \t' + decoded_string)
print('Encoded string: \t' + rle_encode(decoded_string))
print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')
