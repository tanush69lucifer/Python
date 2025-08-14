# second largest element ina  list
lst=list(map(int, input("Enter a list of numbers separated by commas: ").split(",")))
lst.sort()
print("Second largest element:", lst[-2])
