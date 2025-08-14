# most frequent character
s=input("Enter a string: ")
c={}
for ch in s:
    c[ch]=c.get(ch,0)+1
if not c:
    print("No characters found.")
else:
    f=max(c,key=c.get)
    print("Most frequent:", f)
