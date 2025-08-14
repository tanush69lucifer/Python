# string compression
s=input("Enter a string: ")
comp=""
count=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        count+=1
    else:
        comp+=s[i-1]+str(count)
        count=1
comp+=s[-1]+str(count)
if len(comp)==len(s):
    print("No compression possible.")
else:
    print("Compressed:", comp)
