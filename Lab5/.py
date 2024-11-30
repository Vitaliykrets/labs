class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())
print(cat.speak())


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

make_animal_speak(dog)  
make_animal_speak(cat)  


from abc import ABC, abstractmethod

class Shape(ABC):  
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
square = Square(4)

print(circle.area())  
print(square.area())  


class Animal:
    def speak(self):
        print("Animal speaks")

class Flyer:
    def fly(self):
        print("Flying in the sky")

class Bird(Animal, Flyer):  
    pass

bird = Bird()
bird.speak()  
bird.fly()    

#Агрегація
class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start(self):
        self.engine.start()
        print("The car is moving.")

engine = Engine()
car = Car(engine)

car.start()  




#Композиція
class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print(f"Engine with {self.power} HP started.")

class Car:
    def __init__(self, brand, model, engine_power):
        self.brand = brand
        self.model = model
        self.engine = Engine(engine_power)

    def start(self):
        print(f"{self.brand} {self.model} is starting the engine:")
        self.engine.start()
        print("The car is ready to drive.")

my_car = Car("Tesla", "Model S", 1020)
my_car.start()



class Person:
    @staticmethod
    def is_adult(age): 
        return age >= 18  

print(Person.is_adult(20))  


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_human(cls): 
        return cls("Max", 10)

human_person = Person.create_human()
print(human_person.name)  
print(human_person.age) 


class Circle:
    def __init__(self, radius):
        self._radius = radius  

    @property
    def radius(self): 
        return self._radius

    @radius.setter
    def radius(self, value):  
        if value <= 0:
            raise ValueError("The radius must be positive")
        self._radius = value

    @property
    def area(self):  
        return 3.14 * self._radius ** 2

circle = Circle(5)

print(circle.radius) 

print(circle.area) 

circle.radius = 10
print(circle.radius)  
print(circle.area)  


#множинне спадкування
class Flyable:
    def fly(self):
        return "I can fly!"

class Swimable:
    def swim(self):
        return "I can swim!"

class Duck(Flyable, Swimable):
    def quack(self):
        return "Quack-quack!"

duck = Duck()
print(duck.fly())    
print(duck.swim())   
print(duck.quack())  


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1 < person2)   
print(person1 > person2) 
print(person1 == person2) 
print(person1 != person2)  


def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()
