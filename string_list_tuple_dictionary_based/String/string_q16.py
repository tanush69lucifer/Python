# removing duplicates from string
s=input("Enter a string: ")
u="".join(sorted(set(s),key=s.index))
if u==s:
    print("No duplicates to remove.")
else:
    print("Unique characters:", u)
