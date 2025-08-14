# looping amnd printing key value pair
d = dict(input("Enter key-value pairs (key:value) separated by commas: ").split(","))
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")
