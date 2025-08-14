# length of longest word
s=input("Enter a sentence: ")
w=s.split()
if len(w)==0:
    print("No words found.")
else:
    l=max(w,key=len)
    print("Longest word length:", len(l))
