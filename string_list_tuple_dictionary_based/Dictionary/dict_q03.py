# adding or updating a key value pair
d = dict(input("Enter key-value pairs (key:value) separated by commas: ").split(","))
k = input("Enter key to add/update: ")
v = input("Enter value for the key: ")
d[k] = v
print("Updated dictionary:", d)
