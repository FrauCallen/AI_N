# Заданий  масив  X=(x1,x2,...,xn),  в  якому  можуть  бути однакові  числа.(<12)
# Знайти максимальний і мінімальний елементи серед неповторюваних чисел.


X = [2, 2, 3, 4, 45, 3, 10, 11, 45, 33, 45]
Y = []
size=12
if len(X) >= size:
    print(f"Кількість елементів у масиві X перевищує 12.")
else:
    for i in range(len(X)):
        buf = X[i]
        num = 0
        for j in range(len(X)):
            if X[i] == X[j]:
                num += 1
        if num == 1:
            Y = Y + [X[i]]
    max_element = max(Y)
    min_element = min(Y)
    print("Масив:", X)
    print("Масив без елементів з повтореннями:", Y)
    print("Максимальний елемент:", max_element)
    print("Мінімальний елемент:", min_element)
