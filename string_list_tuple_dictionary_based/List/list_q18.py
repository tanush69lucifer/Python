# extending a list by adding another list
lst1=input("Enter the first list (comma separated): ").split(",")
lst2=input("Enter the second list (comma separated): ").split(",")
lst1.extend(lst2)
print("Extended list:", lst1)
