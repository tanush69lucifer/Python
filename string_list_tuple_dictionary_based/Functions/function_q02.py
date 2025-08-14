# even or odd
n=int(input("Enter a number: "))
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"
print(f"The number is {even_odd(n)}.")
