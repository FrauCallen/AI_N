from lab4 import *


mas = [5, 2, 8, 5, 2, 9, 1, 4, 6, 9, 3, 7]
max_num, min_num = array_num(mas)
print(f"Максимальний елемент серед неповторюваних чисел: {max_num}")
print(f"Мінімальний елемент серед неповторюваних чисел: {min_num}")

a = sorting(mas)
print(f"Відсортований масив в порядку убування: {a}")

x, y, z = 2, 3, 5
res = functions(x, y, z)
print(f"Результат функції: {res}")

