# number is prime nor not
n=int(input("Enter a number: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(f"Is the number prime? {is_prime(n)}")
