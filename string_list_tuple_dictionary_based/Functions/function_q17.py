# remove duplicates from a list
lst=input("Enter elements separated by commas: ").split(",")
def remove_duplicates(lst):
    return list(set(lst))
print("List without duplicates:", remove_duplicates(lst))
