num = int(input("Enter: "))

isPrime = True

for i in range(2, num):
    if num % i == 0:
        isPrime = False

if isPrime:
    print("Number is prime")
else:
    print("Number is not prime")