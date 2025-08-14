# replacing substring
s=input("Enter a string: ")
o=input("Old substring: ")
n=input("New substring: ")
if o not in s:
    print(f"Substring '{o}' not found.")
else:
    m=s.replace(o,n)
    print("Updated:", m)
