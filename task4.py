# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num10 = int(input())
num2 = []
temp = 0
print(num10, '->', end= ' ')
while num10 > 0:
    num2.append(num10 % 2)
    num10 //= 2
num2.reverse()
for i in range(len(num2)):
    print(num2[i], end='')
