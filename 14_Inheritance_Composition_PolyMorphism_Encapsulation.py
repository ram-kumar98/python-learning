# Agenda
-----------------
1. Quick Revision of IS-A and Inheritance
2. Types of Inheritance
3. HAS-A Relationship
4. Polymorphism
5. Encapsulation


class Vehicle:


    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start(self):
        self.is_running = True
        print(f"{self.brand} {self.model} engine started")
    
    def stop(self):
        self.is_running = False
        print(f"{self.brand} {self.model} engine stopped")
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
		

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)  # Call parent constructor
        self.doors = doors
    
    def honk(self):
        print(f"{self.brand} {self.model} says: Beep Beep!")
    
    # Override parent method (Method OverRiding)
    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors"
		

class Bike(Vehicle):
    def __init__(self, brand, model, year, engine_cc):
        super().__init__(brand, model, year)
        self.engine_cc = engine_cc
    
    def wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie! ")
    
    # Override parent method
    def display_info(self):
        return f"{super().display_info()} ({self.engine_cc}cc engine)"


my_car = Car("Toyota", "Camry", 2022, 4)
my_car.honk()
print(my_car.display_info())


-----------------------------------------


Composition = "HAS-A" relationship

One class contains another class as a part of it.
Composition = Using another class inside your class



A Car HAS-A Engine

Car is NOT an Engine 		❌ (so no inheritance)
Car USES an Engine 			✅ (composition)


class Engine:
    
    def start(self):
        print("Engine started")


class Car:
    
    def __init__(self):
        self.engine = Engine()   # Composition (Car HAS-A Engine)
    
    def drive(self):
        print("Car is driving")
        self.engine.start()      # Using Engine functionality


# Create object
car = Car()
car.drive()



Significance : Reusability


class Laptop:
    
    def code(self):
        print("Coding on laptop")


class Student:
    
    def __init__(self):
        self.laptop = Laptop()   # Composition
    
    def study(self):
        print("Student is studying")
        self.laptop.code()


s = Student()
s.study()





-----------------------------------------




Types of inheritance 
-------------------------

Single Heritance 

# Parent class
class Animal:
    
    def eat(self):
        print("Animal is eating")


# Child class

class Dog(Animal):
    
    def bark(self):
        print("Dog is barking")

d = Dog()
d.eat()   
d.bark()


Multi Level Inheritance

# Grandparent class
class Animal:
    
    def eat(self):
        print("Animal is eating")


# Parent class (inherits from Animal)
class Dog(Animal):
    
    def bark(self):
        print("Dog is barking")


# Child class (inherits from Dog)
class Puppy(Dog):
    
    def weep(self):
        print("Puppy is weeping")
		



p = Puppy()

# Access all methods
p.eat()   # from Animal
p.bark()  # from Dog
p.weep()  # from Puppy


---------------------------------------------------------------------------------

# Grandparent class
class Animal:
    
    def __init__(self, name):
        self.name = name
        print(f"Animal constructor called: {self.name}")
    
    def eat(self):
        print(f"{self.name} is eating")


# Parent class
class Dog(Animal):
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        print(f"Dog constructor called: {self.breed}")
    
    def bark(self):
        print(f"{self.name} ({self.breed}) is barking")


# Child class
class Puppy(Dog):
    
    def __init__(self, name, breed, age):
        super().__init__(name, breed)
        self.age = age
        print(f"Puppy constructor called: {self.age} months old")
    
    def weep(self):
        print(f"{self.name} is weeping")


# Create object
p = Puppy("Tommy", "Labrador", 3)

# Access all methods
p.eat()
p.bark()
p.weep()



Hierarchical Inheritance


# Parent class
class Animal:
    
    def __init__(self, name):
        self.name = name
        print(f"Animal constructor called: {self.name}")
    
    def eat(self):
        print(f"{self.name} is eating")


# Child class 1
class Dog(Animal):
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} ({self.breed}) is barking")


# Child class 2
class Cat(Animal):
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def meow(self):
        print(f"{self.name} ({self.color}) is meowing")


# Create objects
d = Dog("Rocky", "German Shepherd")
c = Cat("Kitty", "White")

# Access methods
d.eat()
d.bark()

c.eat()
c.meow()



					A 
				
		D(A) 				C(A)

--------------------------------------------------------


Multiple Inheritance


class Student:
    
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"Student Name: {self.name}")


class Sports:
    
    def __init__(self, sport):
        self.sport = sport
    
    def show(self):
        print(f"Sport: {self.sport}")


class Result(Student, Sports):
    
    def __init__(self, name, sport):
        Student.__init__(self, name)
        Sports.__init__(self, sport)
    
    def show(self):
        Student.show(self)
        Sports.show(self)

r = Result("Ram", "Cricket")
r.show()

# r = Result("Ram", "Cricket")

# Student.show(r)
# Sports.show(r)


-----------------




POLY MORPHISM
------------------

Poly - Multi (forms of functionality)
The same method name behaves differently depending on the object.

a = 5 
b = 10 

a + b 




x = 'Ram'
y = 'Kumar'

x + y 



Both the cases, we are adding the 2 variables 

but based on variable object type it automatically does the different functionality.


class CreditCard:
    
    def pay(self):
        print("Paid using Credit Card")


class UPI:
    
    def pay(self):
        print("Paid using UPI")


class Cash:
    
    def pay(self):
        print("Paid using Cash")


# Polymorphism in action
for payment in [CreditCard(), UPI(), Cash()]:
    payment.pay()
	


Credit Card → different behavior
UPI → different behavior
Cash → different behavior


But method name is same: pay()



class Bird:
    def fly(self):
        print("Bird can fly")


class Airplane:
    def fly(self):
        print("Airplane can fly")


def start_flying(obj):
    obj.fly()


start_flying(Bird())
start_flying(Airplane())



-------------------------------------------------------------------------

Encapsulation
=================

Encapsulation is one of the core OOP concepts.
It means bundling data (variables) and methods (functions) together inside a class and 
restricting direct access to some of the data.

class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private attribute (encapsulated)
    
    
    def get_balance(self):
        return self.__balance
    
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid amount")


account = BankAccount("Ram", 1000)
print(f"Balance: ${account.get_balance()}")  
account.deposit(500)    
account.withdraw(200)

-----------------------------------------------------------------------------------


