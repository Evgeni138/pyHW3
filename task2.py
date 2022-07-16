# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


from math import *
list1 = [1, 3, 23, 54, 1]
list2 = []
k = 0
j = len(list1) - 1
for i in range(int(len(list1) / 2)):
    list2.append(list1[k] * list1[j])
    k +=1
    j -=1
if len(list1) % 2 == 1:
    list2.append(list1[(ceil((len(list1)-1) / 2))] ** 2)
print(list2)