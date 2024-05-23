class Product:
    def __init__(self, name, color, shape, taste):
        self.__name = name
        self.__color = color
        self.__shape = shape
        self.__taste = taste
    def get_name(self):
        return self.__name
    def get_color(self):
        return self.__color
    def get_shape(self):
        return self.__shape
    def get_taste(self):
        return self.__taste


    def validation(self, prompt):
        value = input(prompt)
        while not all(word.isalpha() for word in value.split()):
            print("Невірно введені данні")
            value = input(prompt)
        return value


# Класи-нащадки
class Fruit(Product):
    def __init__(self, name, color, shape, taste):
        super().__init__(name, color, shape, taste)
    def what_is_it(self):
        return "фрукт"
    def add(self):
        self._Product__name=self.validation("Введіть назву фрукта:\t")
        self._Product__color = self.validation("Введіть колір фрукта:\t")
        self._Product__shape = self.validation("Введіть форму фрукта:\t")
        self._Product__taste = self.validation("Введіть смак фрукта:\t")


class Vegetable(Product):
    def __init__(self, name, color, shape, taste):
        super().__init__(name, color, shape, taste)
    def what_is_it(self):
        return "овоч"
    def add(self):
        self._Product__name = self.validation("Введіть назву овоча:\t")
        self._Product__color = self.validation("Введіть колір овоча:\t")
        self._Product__shape = self.validation("Введіть форму овоча:\t")
        self._Product__taste = self.validation("Введіть смак овоча:\t")


class Berry(Product):
    def __init__(self, name, color, shape, taste):
        super().__init__(name, color, shape, taste)
    def what_is_it(self):
        return "ягода"
    def add(self):
        self._Product__name = self.validation("Введіть назву ягоди:\t")
        self._Product__color = self.validation("Введіть колір ягоди:\t")
        self._Product__shape = self.validation("Введіть форму ягоди:\t")
        self._Product__taste = self.validation("Введіть смак ягоди:\t")

class Tomato(Vegetable):
    def __init__(self, name=None, color=None, shape=None, taste=None,acidity=None):
        super().__init__(name, color, shape, taste)
        self.__acidity = acidity

    def add(self):
        super().add()
        self.__acidity = input("Введіть кислотність помідора:\t")

    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()},продукт - {self.what_is_it()}, кислотність - {self.__acidity}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()},продукт - {self.what_is_it()}, кислотність - {self.__acidity}"


class Raspberry(Berry):
    def __init__(self, name=None, color=None, shape=None, taste=None, seeds=None):
        super().__init__(name, color, shape, taste)
        self.__seeds = seeds

    def add(self):
        super().add()
        self.__seeds = input("Введіть наявність насіння в малини:\t")

    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, продукт - {self.what_is_it()},наявність насіння - {self.__seeds}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, продукт - {self.what_is_it()},наявність насіння - {self.__seeds}"


class Strawberry(Berry):
    def __init__(self, name=None, color=None, shape=None, taste=None, size=None):
        super().__init__(name, color, shape, taste)
        self.__size = size

    def add(self):
        super().add()
        self.__size = input("Введіть розмір полуниці:\t")

    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, продукт - {self.what_is_it()},розмір - {self.__size}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()},продукт - {self.what_is_it()},розмір - {self.__size}"


class Banana(Fruit):
    def __init__(self, name=None, color=None, shape=None, taste=None, curvature=None):
        super().__init__(name, color, shape, taste)
        self.__curvature = curvature
    def add(self):
        super().add()
        self.__curvature = input("Введіть кривизну банана:\t")
    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, кривизна - {self.__curvature},продукт - {self.what_is_it()}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, кривизна - {self.__curvature},продукт - {self.what_is_it()}"



class Potato(Vegetable):
    def __init__(self, name=None, color=None, shape=None, taste=None, starchiness=None):
        super().__init__(name, color, shape, taste)
        self.__starchiness = starchiness

    def add(self):
        super().add()
        self.__starchiness = input("Введіть крохмалевість картоплі:\t")


    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, крохмалевість - {self.__starchiness},продукт - {self.what_is_it()}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, крохмалевість - {self.__starchiness},продукт - {self.what_is_it()}"


class Grape(Fruit):
    def __init__(self, name=None, color=None, shape=None, taste=None, seedlessness=None):
        super().__init__(name, color, shape, taste)
        self.__seedlessness = seedlessness

    def add(self):
        super().add()
        self.__seedlessness = input("Введіть наявність насіння в винограді (так/ні):\t")

    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, безнасінність - {self.__seedlessness},продукт - {self.what_is_it()}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, безнасінність - {self.__seedlessness},продукт - {self.what_is_it()}"


class Apple(Fruit):
    def __init__(self, name=None, color=None, shape=None, taste=None, crunchiness=None):
        super().__init__(name, color, shape, taste)
        self.__crunchiness = crunchiness

    def add(self):
        super().add()
        self.__crunchiness = input("Введіть хрусткість яблука:\t")

    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, хрусткість - {self.__crunchiness},продукт - {self.what_is_it()}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, хрусткість - {self.__crunchiness},продукт - {self.what_is_it()}"


class Kiwi(Fruit):
    def __init__(self, name=None, color=None, shape=None, taste=None, fuzziness=None):
        super().__init__(name, color, shape, taste)
        self.__fuzziness = fuzziness
    def add(self):
        super().add()
        self.__fuzziness = input("Введіть пухнастість ківі (так\ні):\t")
    def info(self):
        return print(
            f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()},пухнастість - {self.__fuzziness},продукт - {self.what_is_it()}")

    def __str__(self):
        return f"{self.get_name()}: колір - {self.get_color()}, форма - {self.get_shape()}, смак - {self.get_taste()}, пухнастість - {self.__fuzziness},продукт - {self.what_is_it()}"


# Main
apple = Apple("Яблуко", "червоний", "кругле", "солодкий","Yes")
strawberry = Strawberry("Полуниця", "червоний", "кусковидна", "солодка", "4 см")

print(strawberry)

f=Banana()
f.add()
f.info()
