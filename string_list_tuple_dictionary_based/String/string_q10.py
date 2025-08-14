# character occurence removal
s=input("Enter a string: ")
r=input("Character to remove: ")
if r not in s:
    print(f"Character '{r}' not found.")
else:
    c=s.replace(r,"")
    print("After removal:", c)
