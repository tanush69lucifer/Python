# checking if string is valid number
s=input("Enter a string: ")
v=s.replace(".","",1).isdigit()
if not v:
    print("It's not a valid number.")
else:
    print("Valid number:", v)
