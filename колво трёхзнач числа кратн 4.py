a = int(
    input()
)  # Напишите программу, которая в последовательности натуральных чисел определяет количество трёхзначных чисел, кратных 4. Программа получает на вход натуральные числа, количество введённых чисел неизвестно, последовательность чисел заканчивается числом 0 (0 — признак окончания ввода, не входит в последовательность).
# Количество чисел не превышает 1000. Введённые числа не превышают 30 000. Программа должна вывести одно число: количество трёхзначных чисел, кратных 4.
k = 0
while a != 0:
    if a % 4 == 0 and a > 100 and a < 1000 and a < 30000:
        k = k + 1
    a = int(input())
print(k)
# 19.03.22
