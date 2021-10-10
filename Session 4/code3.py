

# 1, 1, 2, 3, 5

def imp_fib(n):
    lst = [1, 1]
    if n < 3:
        return lst[n-1]
    for i in range(n-2):
        lst.append(lst[-1] + lst[-2])
    return lst[-1]

# 3
#   2    1

#          5
#      4      3
#    3   2  2   1
# 2   1


def fib(n):
    if n < 3:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(25))

# STACK
# 1
# 1, 2, 3
# 1, 2 -> 3
