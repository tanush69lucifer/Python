# merging two lists
lst1=input("Enter the first list (comma separated): ").split(",")
lst2=input("Enter the second list (comma separated): ").split(",")
def merge_lists(lst1, lst2):
    return lst1 + lst2
print("Merged list:", merge_lists(lst1, lst2))
