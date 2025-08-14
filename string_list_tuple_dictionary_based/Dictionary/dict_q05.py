# checking if key exist 
d = dict(input("Enter key-value pairs (key:value) separated by commas: ").split(","))
k = input("Enter the key to check: ")
if k in d:
    print(f"'{k}' exists in the dictionary.")
else:
    print(f"'{k}' does not exist in the dictionary.")
