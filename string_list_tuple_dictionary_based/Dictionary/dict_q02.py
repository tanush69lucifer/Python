# getting value of a specific key
d = dict(input("Enter key-value pairs (key:value) separated by commas: ").split(","))
k = input("Enter the key to fetch its value: ")
if k in d:
    print(f"Value of '{k}':", d[k])
else:
    print(f"'{k}' not found in the dictionary.")
