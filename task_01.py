## Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)

# Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP. 
# В цьому класі повинні бути методи для створення користувача, оновлення даних користувача та видалення користувача. 
# Переконайтеся, що кожен метод відповідає за одну конкретну функцію.

# class User:
#     def __init__(self, name) -> None:
#         self.name = name

#     def get_user_name(self):
#         print(f"User's name is {self.name}")
#         print(self.__dict__)
#         print("-------")

#     def update_user_name(self, name):
#         self.name = name
#         print(f"User's NEW name is {name}")
#         print(self.__dict__)
#         print("-------")
    
# user_01 = User("Mike")
# user_01.get_user_name()
# user_01.update_user_name("Michael")

class Team:
    def __init__(self) -> None:
        self.team = []

    def get_team_data(self):
        print(self.team)

    def create_user(self, name):
        self.team.append(name)

    def remove_user(self, position):
        del self.team[position]

team = Team()
team.get_team_data()

team.create_user("Mike")
team.create_user("Michael")
team.create_user("Mykhailo")
team.get_team_data()

team.remove_user(0)
team.get_team_data()

