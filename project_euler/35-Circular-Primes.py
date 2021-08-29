from math import sqrt


def is_prime(number):
    for i in range(2, int(sqrt(number))):
        if number % 2 == 0:
            return False
    return True


for i in range(2, 20):
    if (is_prime(i)):
        print(i)
