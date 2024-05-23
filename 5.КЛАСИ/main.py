import math
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y


    # Переміщення точок
    def move_x(self, dx):
        self.__x += dx
    def move_y(self, dy):
        self.__y += dy

   # Обчислюємо відстань від точки до початку координат
    def origin(self):
        return round(math.sqrt(self.__x**2 + self.__y**2), 2)

    # Обчислюємо відстань між двома точками
    def distance(self, other_point):
        return round(math.sqrt((other_point.get_x()-self.__x)**2 + (other_point.get_y()-self.__y)**2), 2)

    # Обчислюємо відстань між двома точками
    def polar(self):
        r = math.sqrt(self.__x**2 + self.__y**2)  # Обчислюємо радіус (відстань до точки) в полярних координатах
        theta = math.atan2(self.__y, self.__x)  # Обчислюємо кут (аргумент) в полярних координатах
        return round(r, 2), round(theta, 2)

    # Перевірка на рівність точок
    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

#----------------------------------------------------------------------------------
def input_point():
    x = float(input("Введіть координату X: "))
    y = float(input("Введіть координату Y: "))
    return Point(x, y)

# Введення координат першої точки з консолі
print("Введіть координати першої точки:")
A = input_point()

# Введення координат другої точки з консолі
print("\nВведіть координати другої точки:")
B = input_point()

print("\nКоординати точки 1:", A.get_x(), ",", A.get_y())
print("Координати точки 2:", B.get_x(), ",", B.get_y())

A.move_x(2)
B.move_y(-3)

print("Після переміщення:")
print("Координати точки 1:", A.get_x(), ",", A.get_y())
print("Координати точки 2:", B.get_x(), ",", B.get_y())

print("Відстань від точки 1 до початку координат:", A.origin())
print("Відстань від точки 2 до початку координат:", B.origin())
print("Відстань між точками 1 і 2:", A.distance(B))

print("Точка 1 в полярних координатах:", A.polar())

if A == B:
    print("Точки 1 і 2 збігаються.")
else:
    print("Точки 1 і 2 різні.")
