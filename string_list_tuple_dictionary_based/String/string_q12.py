# checking anagram
s=input("Enter a string: ")
subs=[s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)]
if len(subs)==0:
    print("No substrings found.")
else:
    print("Substrings:", subs)
