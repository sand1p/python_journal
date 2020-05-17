# Loop in method

# Method that is declared outside the class can directly be invoked
# code in method need to be indented
# naming convention is to use snake_case for naming everything.
#  for class name its upper Snake_case


def print_multiple_times(times):
    # range function is exclusive range(1, 4) => will consider only 1,2,3.
    for i in range(1, times+1):
        print("Hello {}".format(i))


print_multiple_times(5)
