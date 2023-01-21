# 2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = list(map(int, input("Введите числа через пробел:\n").split()))

if len(my_list) % 2 != 0:
    new_my_list = len(my_list) // 2 + 1
    for i in range(new_my_list):
        mult_lst = my_list[i] * my_list[len(my_list) - i - 1]
        print(mult_lst)

else:
    new_my_list2 = len(my_list) // 2 
    for i in range(new_my_list2):
        mult_lst2 = my_list[i] * my_list[len(my_list) - i - 1]
        print(mult_lst2)
