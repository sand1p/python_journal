# classes have set of attributes that defines its state
# methods are used to modify the state

# all standard features of OOPs are supported by Python classes
# 1. Inheritance
# 2. override method
# 3. class data members are public and all member funtions are virtual ?
# 4. objects members cannot be accessed directly from the methods,
# 5. object argument is provided implicitly by the call
# 6. Scopes and namespaces: namespace is a mapping from names to objects, module object and module attribute.
#     - Name scopes are resolved dynamically at runtime.
#  7. attribute of the object is referenced with '.'.
#  8. Important modules
#     -  __ main__
#       -  builtins
#       -
#  9.


# Scope and namespace example


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("after Local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment", spam)


scope_test()
print("In global scope", spam)


