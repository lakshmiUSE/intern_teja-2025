#  9.   Write a python program  to check whether a given number is prime or not.
         # Example:    n=7   —-------->Output: 7 is a prime number

n = 7
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

