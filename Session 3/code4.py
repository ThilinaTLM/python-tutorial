

# RECURSION
# 0 1 2 3 4 5
# 1,1,2,3,5,8...


# Return nth fibonacci number
def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Return nth fibonacci number (improve performance with a dict)
fibonacci_store = {0: 1, 1: 1}
def fibonacci(n):
    if n in fibonacci_store:
        return fibonacci_store.get(n)
    fib_value = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_store[n] = fib_value
    return fib_value



"""
                                            fib(4)
                    fib(3)                                 fib(2)
           fib(2)               fib(1)              fib(1)        fib(0)
fib(1)               fib(0)

"""


print(fibonacci(35))