# removing duplicates from a list
lst=input("Enter elements separated by commas: ").split(",")
lst_no_duplicates=list(set(lst))
print("List without duplicates:", lst_no_duplicates)
