N = int(input("Enter the value of N: "))

a = 0
b = 1

while a < N:
    print(a, end=" ")
    a, b = b, a + b