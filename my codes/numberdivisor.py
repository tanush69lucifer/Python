# Count the number of divisor 
'''num = 29
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count == count +1
print(count)'''
num = int(input("Enter any positive integer: "))
# Using list comprehension and sum() to count divisors for any number
count = sum(1 for i in range(1, num + 1) if num % i == 0)
print(f'The number of divisors of {num} is {count}')
