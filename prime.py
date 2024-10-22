# print prime numbers from n to m

n = int(input("Enter the starting number: "))
m = int(input("Enter the last number: "))


def prime(num):
    if num < 2:
        print("all are prime before 2")
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(n, m + 1):
    if prime(i):
        print(i, end = " ")
        