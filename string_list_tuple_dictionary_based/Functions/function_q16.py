# sum of digits of a number
n=int(input("Enter a number: "))
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
print("Sum of digits:", sum_of_digits(n))
