# https://docs.python.org/3/tutorial/errors.html
# Multiple except statements for single try
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# B, D, D
# D D D
#  Derived class is matched to Parent class.
#  Parent class cannot match to Derived class.


# Last except clause may omit the Exception class name and can be kept as a wildcart for default case
import sys
try:
    f = open('resources/myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OSError: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an Integer.")
except:
    print("Unexpected error:", sys.exc_info()[1], sys.exc_info()[0])
    # raise

# try ... except statement has an optional else clause, which, when present, must follow all except clauses.
# it is useful for code that must be executed if the try clause does not raise an exception. For example

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readline()), 'lines')
        f.close()

# the use of the else clause is better that adding
# 'else' clause is required because the code that is not responsible for producing exception should not be there inside try


# exception's argument.
# The presence and type of the argument with the exception
# Variables are bound to exception instance, with arguments stored in instance.args
# exception defines __str__() so the arguments can be printed directly without having to reference .args,

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)
    x, y = inst.args
    print('x =', x)
    print('y =', y)

# __str__()  => default implementation.
# ClassName as instance will give the object in the instance variable
# exception can be raise with arguments


# Exception can be thrown from the method

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as instance:
    print("instance for raising exception from other method:", instance)

# 8.4 Raising Exceptions
# The raise statement allows the programmer to force specified exception to occur immediately in the try clause

# raise NameError("You have bad name")

# If you don't intend to catch the exception use raise in exception

try:
    raise NameError("Bad ")
except NameError as instance:
    print("Throwing it again ")
    raise


# 8.5 User-defined exception
# exceptions  are derived from the Exception class either directly or directly
class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    """Exceptions raised for the errors in the input.

        Attributes:
            expression -- input expression in which the error occurred
            message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# User defined Exceptions





