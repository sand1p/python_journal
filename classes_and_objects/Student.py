# Class declaration
"""
    Class is declared in Python as follows,
    provide 2 blank lines at the top,
    class name is provided as follows
    class Class_Name:

"""
# Class definition
"""
Class definition includes __init__(self) method
fields in the class are provided there, 
and are initialize using initial values. 

"""
# Constructors
"""
    
"""
# Destructors
# Important keywords
# How to compare 2 classes
# How to sort collection of objects of same class
# How to display class elements
# is there a concept of object in Python.


# TODO Declare class Student with name and roll number as attributes
# indentation: Class definition starts with 2 blank lines at top


class Student:
    def __init__(self, name="",roll_number = 0):
        self.name = name
        self.roll_number = roll_number

    def display(self):
        print("Name: {}, roll Number: {}".format(self.name, self.roll_number))


# main definition check also needs 2 blank lines at the top


if __name__ == '__main__':
    student = Student("Sandip", 456)
    student.display()

