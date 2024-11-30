## Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)

# Створіть ієрархію класів для геометричних фігур, 
# де кожен підклас (наприклад, "Квадрат" і "Круг") може замінити базовий клас "Фігура" без порушення функціональності. 
# Переконайтеся, що ці підкласи можуть використовуватися замість базового класу у всіх контекстах без проблем.

from abc import ABC, abstractclassmethod

class Shape(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print(f"Circle's area is {area} (radius={self.radius})")

class Square(Shape):
    def __init__(self, a) -> None:
        super().__init__()
        self.a = a

    def calculate_area(self):
        area = self.a ** 2
        print(f"Square's area is {area} (a={self.a})")

circle_01 = Circle(10)
circle_01.calculate_area()

square_01 = Square(5)
square_01.calculate_area()