class ClassName:
    def display(self):
        print("Class definition")


classs = ClassName()

classs.display()

# class objects
# attribute references and instantiation instantiation
# obj.name attribute reference
#


class MyClass:
    """A Simple example class"""
    i = 12345

    def f(self):
        return "MyClass Hello, World!"


my_class = MyClass()

print(my_class.f())

print(MyClass().i)
print(MyClass().f)
print(MyClass.__doc__)


#  Some classes need to be in some initial state when instantiated , __init__ method is reserved for the same

class MySmartClass:
    def __init__(self):
        self.data = []

    def display(self):
        print("Hello, World!",self.data)


smartClass = MySmartClass()

smartClass.display()

# Passing arguments to the class def


class Complex:
    def __init__(self, real, imaginary):
        self.r = real
        self.i = imaginary


x = Complex(3.0, -4.5)
print(x.i)
print(x.r)

x.counter = 1
while x.counter < 10:
    x.counter = x.counter*2
print(x.counter)
del x.counter


# Method objects

xx = MyClass()
xf = xx.f()
print(xf)


class MethodObjects:
    def f(self):
        print("Hello, World!")


mObj = MethodObjects()
# of = mObj.f()


# while True:
#     print(xf)

MethodObjects.f(mObj)

#  Class and instance Variable
# Instance variables are for data Unique to each instance.
#  class variables are for attributes and methods shared by all instances of the class

class Dog:
    kind = 'canine'  #class variable shared by all the instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


a = Dog("Fido")
b = Dog("Pinto")

print(a.name, a.kind)
print(b.name, b.kind)
a.canine = "Pitbull"
print(a.name, a.kind)
print(b.name, b.kind)


class Cat:

    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Cat('Blacky')
e = Cat('Paddy')
d.add_trick("Meow")
e.add_trick("Pawing")
print(d.tricks)  # unexpectedly shared by all the dogs

#  Correct design of class should include instance variables instead


class Cow:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)


cow = Cow("Doongi")
cow2 = Cow("Zingri")

print(cow.tricks)
print(cow2.tricks)

cow.add_trick("Milking")
cow2.add_trick("fighting")

print(cow.tricks)
print(cow2.tricks)

# same attribute name occures in both an instance and in a class.


class Warehouse:
    purpose = 'storage'
    region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse
w2.region = 'east'
print(w2.purpose, w2.region)


# assigning function definition to a class variable


def f1(self, x, y):
    return min(x, y)


class C:
    f = f1

    def g(self):
        return 'Hello, World!'

    h = g


c = C()
print(c.f(3, 5))
print(c.g())
print(c.h())


class Bag:
    def __init__(self):
        self.data = []

    def add(self, data):
        self.data.append(data)

    def add_twice(self, data):
        self.data.append(data)
        self.data.append(data)

# Inheritance


class Person:
    name = 'sandip'
    address = 'Pune'

    def get(self):
        return "Name: {}, address: {}".format(self.name, self.address)


class Student(Person):
    pass


sandip = Student()
print(sandip.get())


# access modifiers, Private: Instance variables that that cannot be accessed except from inside
# an object don't exist in Python.
# private is just convention in Python and can be followed by placing _ before function or variable.
# name mangling {When subclass and parent class need to have same variable names}


class Mapping:
    def __init__(self, iterable):
        self.item_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)

    __update = update    # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.item_list.append(item)


# iterators


for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {"one": 1, "two": 2}:
    print(key)
for char in "sandip":
    print(char)
for line in open("Classes.py"):
    pass  # print(line, end='')
#
# iterator decoded
s = "abc"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
# next(it)


# reverse


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


rev = Reverse("spam")

for char in rev:
    print(char)

#  Generators
