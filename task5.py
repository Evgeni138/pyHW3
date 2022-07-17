# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# F-n = (-1)**(n+1)*Fn, Fn = F(n+2)−F(n+1).

# n = int(input())
# list1 = []
# for i in range(1, -n - 1, -1):
#     if i == 1:
#         list1.append(1)
#     elif i == 0:
#         list1.append(0)
#     elif i == -1:
#         list1.append(1)
#     elif i == -2:
#         list1.append(-1)
#     else:
#         list1.append(list1[i - 1] - list1[i - 2])
# print(list1)


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)

n = int(input())
result = []
for i in range(0, n + 1):
    result.append((-1) ** (i + 1) * fib(i))
result.reverse()
for i in range(1, n + 1):
    result.append(fib(i))
print(result)