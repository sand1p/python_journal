class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def update(self, obj):
        self.firstname = obj.firstname
        self.lastname = obj.lastname

    def print_object(self):
        print("firstname: {} , lastname: {}".format(self.firstname, self.lastname))


class Student(Person):
    pass


# use below syntax to run above class

student = Student("sandy", "gatkal")

student.printobject()

