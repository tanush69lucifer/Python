# checking if lisst is a sublist of another list

lst1=input("Enter the first list (comma separated): ").split(",")
lst2=input("Enter the second list (comma separated): ").split(",")
if all(i in lst1 for i in lst2):
    print("The second list is a sublist of the first list.")
else:
    print("The second list is not a sublist of the first list.")
