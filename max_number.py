#!/usr/bin/env
# Программа, выводящая число с максимальной суммой цифр.

# Рекурсивная функция для вычисления суммы цифр числа.
def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

# Словарь сумм цифр введённых чисел.
nums = {}
while True:
    num = int(input())
    if num == 0:
        break
    nums[digit_sum(num)] = num

# Вывод требуемого числа.
print(nums[max(nums.keys())])
