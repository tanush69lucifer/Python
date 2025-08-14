# splitting strings into words
s=input("Enter a string: ")
w=s.split()
if len(w)==0:
    print("No words found.")
else:
    print("Words:", w)
