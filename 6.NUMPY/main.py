import numpy as np
while True:
    try:
        X = np.array(input("Введіть елементи вектора X через пробіл: ").split(), int)
        Y = np.array(input("Введіть елементи вектора Y через пробіл: ").split(), int)
        print("X =", X)
        print("Y =", Y)
        # Перевірка, чи співпадають унікальні значення векторів X та Y
        set_X = np.unique(X)
        set_Y = np.unique(Y)
        print("Унікальні значення X:", set_X)
        print("Унікальні значення Y:", set_Y)
        print("Чи співпадають мультимножину значення векторів X та Y:", np.array_equal(set_X, set_Y))
        continue
        #break
    except ValueError:
        print("Введено неправильний формат. Будь ласка, спробуйте ще раз.")
        continue

