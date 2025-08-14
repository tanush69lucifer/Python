# tuple element indexing
t=tuple(input("Enter a list of items separated by commas: ").split(","))
e=input("Enter the element to find index of: ")
if e in t:
    print(f"Index of '{e}':", t.index(e))
else:
    print(f"'{e}' not found.")
