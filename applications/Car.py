# TODO (s.gatkal) Initialize  Car class to get started


class Car:

    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0

    def say_state(self):
        print("I'm good {} kph!".format(self.speed))

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        if self.time != 0:
            return self.odometer / self.time
        else:
            pass


# main method is as follows, every execution starts from here.
# every program execution starts from here, if __name__ == '__main__'
# it's just a main method check in entire file, there can be multiple such check

if __name__ == '__main__':

    # object creation using python is direct assignment statement, no new keyword is used
    # while declaring the variable no need to provide  variable specifier such as 'val' and 'var' in Scala
    # Also there is no need to provide data type as wel.  variable_name = _value_
    my_car = Car()
    # Data in print statement has to be provided through parenthesis.
    print("I'm a car")
    # Loop constructs, to run infinite loop use  while True:
    # indentation is very important while writing  python programs
    while True:
        # input is used for reading line from the console
        action = input("What should I do? [A]ccelerate, [B]rake,"
                       "show [O]dometer, or show average [S]peed? ").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
