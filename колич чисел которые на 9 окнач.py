kolvo = int(input())	# Напишите программу, которая в последовательности натуральных чисел определяет количество чисел, оканчивающихся на 9. Программа получает на вход количество чисел в последовательности, а затем сами числа. В последовательности всегда имеется число, оканчивающееся на 9.
						# Количество чисел не превышает 1000. Введённые числа по модулю не превышают 30 000.
						# Программа должна вывести одно число: количество чисел, оканчивающихся на 9
k = 0
for i in range (kolvo):
	num = int(input())
	if num % 10 == 9 and num <= 30000:
		k = k + 1
print(k)
# 19.03.22 уже легко