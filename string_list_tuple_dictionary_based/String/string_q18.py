# occurance of substrings
s=input("Enter a string: ")
sub=input("Enter substring: ")
c=s.count(sub)
if c==0:
    print(f"Substring '{sub}' not found.")
else:
    print("Occurrences:", c)
