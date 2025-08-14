# checking pallindrome
s=input("Enter a string: ")
def is_palindrome(s):
    return s == s[::-1]
print(f"Is palindrome? {is_palindrome(s)}")
