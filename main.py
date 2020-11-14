
# # Numeric
#     int, float, complex

# # Text
#     string

# # Sequence
#     list, tuple, range, ...

# # Maping / Table
#     dict

# # Set
#     set, frozenset

# # Boolean
#     bool 

# # Other


# value = False

# print(type(value))

# TYPE CASTING
# int(), float(), complex()
# str()
# bool()

# value = bool("")
# print(value)

# # Basic Operators

# # - Arithmatic 
# #     + - * / % //
# # - Assignment
#       = += -= 
# # - Comparison
#       == > < >= <= != 
# # - Logical
#     #   and, or, not

# AND
    # True True -> True


# text = "10.45"
# output = str(int(float(text)))

# print(output)

# Function
    # - arguments (inputs)
    # - return data (output)


# False   await   else    import  pass
# None    break   except  in  raise
# True    class   finally is  return
# and continue    for lambda  try
# as  def from    nonlocal    while
# assert  del global  not with
# async   elif    if  or  yield


# a = 10
# b = 20
# sum = a + b


# P = 3.14 # Value of Pi

# """
# sdasd
# asd
# asd
# """


# val = 6


# if val%2 == 0:
#     if val%4 == 0:
#         val = val // 4
#     else:
#         val = val // 2
# else:
#     val = (val + 1) // 2

# if val%4 == 0:
#     val = val // 4
# elif val%2 == 0:
#     val = val // 2
# else:
#     val = (val + 1) // 2


# print(val)


# 75 A
# 65 B
# 50 C
# 35 S
#    Fail

# Score Student 1 : 60
# Score Student 2 : 70 
# Score Student 3 : 50

# Student 2
# Student 1
# Student 3

# List Data Type 

#          -5  -4  -3   -2       -1   
#           0   1   2   3         4  <- index
# numbers = [10, 20, 30, 12.123, "asdasd"]

# numbers.append(-20) 
# numbers.remove(10)
# del numbers[2]

# print( len(numbers) )

# print( numbers[1:4] )
# print( numbers )

# numbers = numbers[1:4]

# print(list("Hello"))

# numbers = []
# numbers = list()
# print(list())


# Tuples

# numbers = [10]
# # print( len(numbers) )
# # numbers.add("asdasd")
# numbers[0] = 20
# print(numbers[0])
# tuple()

# text = "Hello"
# print(text[1:3])
# text = text + " Python"


# Range
# range(end), 0 --- end - 1
# range(start, end),  start --- end - 1
# range(start, end, step), start start+step, start + 2xstep, .... end - 1
# numbers = range(2, 51, 2)
# print(list(numbers))

# range(4, 0, -1) 4, 3, 2, 1

# numbers = [1, 2, 3, 4]
# numbers.reverse()

# print(numbers)

# print( list(reversed(numbers)) )
# print(numbers)

# Membership Operators
#    in, not in

# Loops

# seq = [20, -10, 40]

# # For Loop
# for i in range(1, 20):
#     print(i)
#     if (i > 0):
#         print(i)

# print("Finish")

# scores = []

# for i in range(1, 6):
#     s = int(input("Student " + str(i) + " Score: "))
#     scores.append(s)

# print(scores)

# Exercise : Show the max value (5 inputs)