# iterate by 1


def print_square_of_numbers(n):
    for i in range(1, n+1):
        print(square(i))


def square(i):
    return i * i


# print_square_of_numbers(10)


# iterate by 2


def loop_by_step(times, step):
    for i in range(1, times+1, step):
        print("Index: {}, increment by: {} ".format(i, step))


loop_by_step(10, 2)

