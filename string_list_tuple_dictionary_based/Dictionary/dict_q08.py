# merging two dictionaries
d1 = dict(input("Enter first dictionary (key:value) separated by commas: ").split(","))
d2 = dict(input("Enter second dictionary (key:value) separated by commas: ").split(","))
d1.update(d2)
print("Merged dictionary:", d1)
