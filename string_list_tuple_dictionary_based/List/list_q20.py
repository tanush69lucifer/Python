# common elements between two lists
lst1=input("Enter the first list (comma separated): ").split(",")
lst2=input("Enter the second list (comma separated): ").split(",")
common_elements=list(set(lst1) & set(lst2))
print("Common elements:", common_elements)
