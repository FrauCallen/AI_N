import random
print("Завдання 1.")
text = "the ahirty - three thieves thought that they thrilled the throne throughout thursday"
alf = "zyxwvutsrqponmlkjihgfedcba"
# 1-z;2-y;3-x;4-w;5-v;6-u;7-t;8-s;9-r;10-q;11-p;12-o;13-n;14-m;15-l;16-k;17-j;18-i;19-h;20-g;21-f;22-e;23-d;24-c;25-b;26-a;


words = text.split()
for i in range(len(words)):
    first_letter = words[i][0].lower()
    if first_letter in alf:
        index = alf.index(first_letter) + 1
        words[i] = str(index) + words[i][1:]
new_string = ' '.join(words)
print(f"Відповідь:{new_string}")



print("\nЗавдання 2.")
# Задаємо розміри матриць
rows_X, cols_X = 4, 5
rows_Y, cols_Y = 5, 4
X = [[random.randint(-10, 10) for _ in range(cols_X)] for _ in range(rows_X)]
Y = [[random.randint(-10, 10) for _ in range(cols_Y)] for _ in range(rows_Y)]

# Виводимо матриці X та Y
print("Matrix X:")
for row in X:
    print(row)

print("\nMatrix Y:")
for row in Y:
    print(row)

# Знаходимо добуток матриць X та Y
Z = [[0 for _ in range(cols_Y)] for _ in range(rows_X)]
for i in range(rows_X):
    for j in range(cols_Y):
        for k in range(cols_X):
            Z[i][j] += X[i][k] * Y[k][j]

# Виводимо результат
print("\nMatrix Z:")
for row in Z:
    print(row)

