# index of element in list
lst=input("Enter elements separated by commas: ").split(",")
e=input("Enter the element to find the index of: ")
if e in lst:
    print(f"Index of '{e}':", lst.index(e))
else:
    print(f"'{e}' not found.")
