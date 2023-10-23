
from abc import ABC, abstractmethod

# Определяем абстрактный класс "Фигура"
class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Создаем класс "Квадрат", наследуясь от абстрактного класса "Фигура"
class Square(Figure):

    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

# Создаем класс "Треугольник", наследуясь от абстрактного класса "Фигура"
class Triangle(Figure):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        # Формула Герона для нахождения площади треугольника
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Пример использования классов
if __name__ == "__main__":
    square = Square(5)
    triangle = Triangle(3, 4, 5)

    print(f"Площадь квадрата: {square.area()}")
    print(f"Периметр квадрата: {square.perimeter()}")

    print(f"Площадь треугольника: {triangle.area()}")
    print(f"Периметр треугольника: {triangle.perimeter()}")
