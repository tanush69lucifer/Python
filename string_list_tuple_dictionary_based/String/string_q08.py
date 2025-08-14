# first non repeated character
s=input("Enter a string: ")
found=False
for ch in s:
    if s.count(ch)==1:
        f=ch
        found=True
        break
if found:
    print("First non-repeated:", f)
else:
    print("No non-repeated characters found.")
