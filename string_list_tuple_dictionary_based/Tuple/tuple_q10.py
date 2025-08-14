# multiply elements of tuple
t=tuple(map(int, input("Enter a list of numbers separated by commas: ").split(",")))
result=1
for num in t:
    result*=num
print("Product of elements:", result)
