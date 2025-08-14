# rotating string
s=input("Enter a string: ")
n=int(input("Rotate by: "))
if n==0 or n==len(s):
    print("No rotation needed.")
else:
    r=s[-n:]+s[:-n]
    print("Rotated:", r)
