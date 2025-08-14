# pallindrome 
s=input("Enter a string: ")
p=s==s[::-1]
if p:
    print("Palindrome?")
else:
    print("not a Palindrome")

