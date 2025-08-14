# removing element from list
lst=input("Enter elements separated by commas: ").split(",")
e=input("Enter the element to remove: ")
if e in lst:
    lst.remove(e)
    print("Updated list:", lst)
else:
    print(f"'{e}' not found in the list.")
