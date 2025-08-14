# vowel n consonent count
s = input("Enter a string: ")
v ="aeiou"
vc = sum(1 for c in s if c in v)
cc = sum(1 for c in s if c.isalpha() and c not in v)
if vc == 0 and cc == 0:
    print("No vowels or consonants.")
else:
    print(f"Vowels: {vc}, Consonants: {cc}")
