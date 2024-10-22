n = int(input("Enter number of elements of fibonnacci: "))

def fib(n):
    a, b = 0, 1
    print(a, b, end = " ")
    for i in range(n-2)    :
        c = a + b
        print(c, end = " ")
        a, b = b, c


if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print(0)
elif n == 2:
    print("0 1")
else:
    fib(n)