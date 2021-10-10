
def custom_filter(func, numbers):
    result = []
    for n in numbers:
        if func(n):
            result.append(n)
    return result

# return true if number is divisible by 4
def is_divided_by_4(number):
    if number % 4 == 0:
        return True
    else:
        return False


# return squre of the number
def squre(number):
    return number*number

numbers1 = range(10, 21) # [10, 11, 12, ... 20]
numbers2 = filter(is_divided_by_4, numbers1) 
numbers3 = map(squre, numbers2)    

print(list(numbers1))
print(list(numbers2))
print(numbers3)


