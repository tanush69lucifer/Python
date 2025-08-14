# checking element existing in tuple
t=tuple(input("Enter a list of items separated by commas: ").split(","))
e=input("Enter the element to check: ")
if e in t:
    print(f"'{e}' is in the tuple.")
else:
    print(f"'{e}' is not in the tuple.")
