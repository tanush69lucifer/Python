# sorting a list
lst=input("Enter numbers separated by commas: ").split(",")
lst=[int(x) for x in lst]
lst.sort()
print("Sorted list:", lst)
