# checking anagram
s1=input("Enter first string: ")
s2=input("Enter second string: ")
a=sorted(s1)==sorted(s2)
if a:
    print("It's an anagram!")
else:
    print("It's not an anagram.")
