## Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)

# Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), 
# який включає методи для друку, сканування та копіювання. 

# Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner), 
# які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні. 
# Переконайтеся, що жоден з класів не має пустого методу.

from abc import ABC, abstractclassmethod

class ToPrint(ABC):
    @abstractclassmethod
    def to_print(self):
        pass

class ToScan(ABC):
    @abstractclassmethod
    def to_scan(self):
        pass

class ToCopy(ABC):
    @abstractclassmethod
    def to_copy(self):
        pass

class Printer(ToPrint):
    def to_print(self):
        print("Printer is printing the document...")

class Scaner(ToScan):
    def to_scan(self):
        print("Scaner is scaning the document...")

class MultifunctionalDevice(ToPrint, ToScan, ToCopy):
    def to_print(self):
        print("MultifunctionalDevice is printing the document...")

    def to_scan(self):
        print("MultifunctionalDevice is scaning the document...")

    def to_copy(self):
        print("MultifunctionalDevice is copying the document...")

printer_01 = Printer()
printer_01.to_print()

scaner_01 = Scaner()
scaner_01.to_scan()

multifunctional_device_01 = MultifunctionalDevice()
multifunctional_device_01.to_print()
multifunctional_device_01.to_scan()
multifunctional_device_01.to_copy()