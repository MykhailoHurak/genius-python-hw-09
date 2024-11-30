## Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)

# Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс, 
# наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle). 
# Потім додайте новий клас, який розраховує площу будь-якої фігури, не модифікуючи існуючі класи. 
# Використовуйте принцип OCP для розширення функціональності.

from abc import ABC, abstractclassmethod

class Shape():
    def __init__(self) -> None:
        pass

class CalculateArea(ABC):

    @abstractclassmethod
    def calculate_area():
        pass

class Circle(Shape, CalculateArea):
    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Area of Circle (r={self.radius}) is {area}")

class Rectangle(Shape, CalculateArea):
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def calculate_area(self):
        area = self.a * self.b
        print(f"Area of Rectangle (a={self.a}, b={self.b}) is {area}")

circle_01 = Circle(5)
circle_01.calculate_area()

circle_02 = Circle(10)
circle_02.calculate_area()

rectangle_01 = Rectangle(5, 10)
rectangle_01.calculate_area()
