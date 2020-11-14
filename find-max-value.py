
numbers = []

for i in range(1, 6):
    n = int(input("Enter number " + str(i) + ": "))
    numbers.append(n)

max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num

print(max_value)