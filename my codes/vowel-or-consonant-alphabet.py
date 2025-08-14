ch=input('enter alphabet :')
if ch in ['a','e','i','o','u','A','E','I','O','U'] :
    print('vowel')
else:
    print('consonant')
'''common source of error -
ch == ['a', 'e', 'i', 'o', 'u'] 
checks if ch is equal to the entire list ['a', 'e', 'i', 'o', 'u'],
 which will always be False since ch is a single character, not a list'''
#for words as strings and counting
word = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(c in vowels for c in word)
consonant_count = sum(c.isalpha() and c not in vowels for c in word)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
#better version 2
word = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = consonant_count = 0

for c in word:
    if c in vowels:
        vowel_count += 1
    elif c.isalpha():
        consonant_count += 1

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
