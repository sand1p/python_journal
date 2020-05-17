#  Restrict instantiation of a class to single object


class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        """ Virtual Private constructor. """
        if Singleton._instance is not None:
            raise Exception("This class is a Singleton!")
        else:
            Singleton._instance = self


if __name__ == "__main__":
    s = Singleton()
    print(s)
    try:
        s = Singleton()
    except Exception:
        print("can't reinitialize")

    print(s)
    s = Singleton.get_instance()
    print(s)
    s = Singleton.get_instance()
    print(s)
