class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}"


class Student(Person):
    def __init__(self, name, age, group, gpa):
        super().__init__(name, age)
        self.group = group
        self.gpa = gpa
    
    def display_info(self):
        return (f"Имя: {self.name}, Возраст: {self.age}, "
                f"Группа: {self.group}, GPA: {self.gpa}")


class Teacher(Person):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience
    
    def display_info(self):
        return (f"Имя: {self.name}, Возраст: {self.age}, "
                f"Предмет: {self.subject}, Стаж: {self.experience} лет")


class AdminStaff(Person):
    def __init__(self, name, age, position, department):
        super().__init__(name, age)
        self.position = position
        self.department = department
    
    def display_info(self):
        return (f"Имя: {self.name}, Возраст: {self.age}, "
                f"Должность: {self.position}, Отдел: {self.department}")


if __name__ == "__main__":
    # Примеры объектов (для проверки полиморфизма)
    people = [
        Student("Алиса", 19, "IS-23", 3.7),
        Teacher("Пётр Иванов", 40, "Математика", 15),
        AdminStaff("Ирина Смирнова", 35, "HR-менеджер", "Отдел кадров")
    ]

    for p in people:
        print(p.display_info())