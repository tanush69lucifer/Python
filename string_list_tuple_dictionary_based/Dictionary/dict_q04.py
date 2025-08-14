# removing a key value pair
d = dict(input("Enter key-value pairs (key:value) separated by commas: ").split(","))
k = input("Enter the key to remove: ")
if k in d:
    del d[k]
    print("Updated dictionary:", d)
else:
    print(f"'{k}' not found in the dictionary.")
