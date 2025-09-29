
#11..Write a program to print all prime numbers between 1 and 50.
              # Expected output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

for n in range(2, 51):
    is_prime = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, end=" ")
