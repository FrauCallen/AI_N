#Створити функцію для вирішення наступного завдання:
#Заданий масив X=(x1,x2,...,xn), в якому можуть бути однакові числа. Знайти максимальний і мінімальний елементи серед неповторюваних чисел.
print("Завдання 1")
def array_num(x):
    Y=[]
    for i in range(len(x)):
        num=0
        for j in range(len(x)):
            if x[i] == x[j]:
                num += 1
        if num == 1:
            Y = Y + [x[i]]
    max_element = max(Y)
    min_element = min(Y)
    return max_element,min_element
#Створити функцію сортування в порядку убування.
def sorting(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]< x[j]:
                x[i], x[j] = x[j], x[i]

    return x
#Створити анонімну функцію для обчислення функції:f = 5𝑥 ∗ 𝑦^3 + 7z
functions= lambda x,y,z:5*x*(y**3)+7*z

mas = [5, 2, 8, 5, 2, 9, 1, 4, 6, 9, 3, 7]
max, min=array_num(mas)
print(f"Максимальний елемент серед неповторюваних чисел: {max}")
print(f"Мінімальний елемент серед неповторюваних чисел: {min}")
a=sorting(mas)
print(f"Відсортований масив в порядку убування: {a}")

x,y,z=2,3,5
res=functions(x,y,z)
print(f"Результат виразу: {res}")

print("Завдання 2")
#Написати рекурсивну функцію: обчислення суми цифр натурального числа.
def sum(number): #456
    if number < 10: #456>10, 45>10
        return number #4
    else:
        return number % 10 + sum(number // 10) #456%10=45, sum(45);45%10=4, sum(4);)

# Приклад використання
num = int(input("Введіть число:"))
resu = sum(num) #4+5+6=15
print(f"Сума цифр числа {num} дорівнює {resu}")
#1234 1+2+3+4