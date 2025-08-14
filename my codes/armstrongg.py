#An Armstrong number (also known as a narcissistic number or pluperfect number) is a number that
#is equal to the sum of its digits raised to the power of the number of digits.
#For example, 153 is an Armstrong number because 1^3+5^3+3^3=153
num = input("Enter a number: ")
num_int = int(num)  # Convert the input to an integer
num_length = len(num)  # Get the number of digits

# Calculate the sum of the digits raised to the power of the number of digits
sum_of_powers = sum(int(digit) ** num_length for digit in num)

# Check if the sum of the powers is equal to the original number
if sum_of_powers == num_int:
    print(f"{num_int} is an Armstrong number")
else:
    print(f"{num_int} is not an Armstrong number")

#second easy method
# Armstrong Number Checker

n = int(input('Enter a number: '))
num = n
sum = 0

while n > 0:
    d = n % 10
    sum = sum + d * d * d
    n = n // 10

if sum == num:
    print('It is an Armstrong number')
else:
    print('It is not an Armstrong number')




