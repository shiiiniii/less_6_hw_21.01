#1. Задайте список из нескольких чисел. Напишите 
# программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



my_list = input('Введите числа через пробел: ')
my_list = list(map(int, my_list.split()))
sum = 0
print(' Ищем нечётные индексы. ')
for i, item in enumerate(my_list):
    print(f' Индекс {i} число {item}')
    if i % 2 != 0:
        sum += item
print(f"Сумма элементов списка, стоящих на позиции с нечетным индексом равна: {sum}")



