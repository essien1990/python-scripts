class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(self.name + ' is walking')

    def speak(self):
        print('Hello, my name is ' + self.name +
              ' and i am ' + str(self.age) + ' years old')


john = Person('John', 27)
hilda = Person('Hilda', 30)

print(john.name + ' ' + str(john.age))
john.speak()
john.walk()
