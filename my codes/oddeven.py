# Even Odd without if else
# Input section
a = int(input("Enter the number: "))
# Logic section
x = "Number is even" * (a % 2 == 0) + "Number is odd" * (a % 2 != 0)
# Output
print(x)
