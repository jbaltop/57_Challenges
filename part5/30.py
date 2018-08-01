def print_result(a, b):
    print("{} * {} = {}".format(a, b, a*b))

def make_list():
    a = 0
    while a <= 12:
        b = 0
        while b <= 12:
            print_result(a, b)
            b += 1
        a += 1

make_list()
