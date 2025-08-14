# element existing in a list
lst=input("Enter elements separated by commas: ").split(",")
e=input("Enter the element to check: ")
if e in lst:
    print(f"'{e}' is in the list.")
else:
    print(f"'{e}' is not in the list.")
