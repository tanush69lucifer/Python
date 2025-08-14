# removing duplicate elements from tuple
t=tuple(input("Enter a list of items separated by commas: ").split(","))
t_no_duplicates=tuple(sorted(set(t), key=t.index))
print("Tuple without duplicates:", t_no_duplicates)
