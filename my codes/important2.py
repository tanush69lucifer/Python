def rearrange_names(names):
    vowels = 'AEIOUaeiou'
    starts_with_vowel = [name for name in names if name[0] in vowels]
    starts_with_consonant = [name for name in names if name[0] not in vowels]
    return starts_with_vowel + starts_with_consonant

# Example
input_names = "Alice Bob Uma Charlie Eve".split()
print(" ".join(rearrange_names(input_names)))

def reverse_prices(prices):
    return " ".join(price[::-1] for price in prices.split())

# Example
input_prices = "123 456 789"
print(reverse_prices(input_prices))
 
def recover_message(secret):
    vowels = 'aeiou'
    return ''.join(vowels[(i % 5)] if char == '*' else char for i, char in enumerate(secret))

# Example
input_message = "Th* qu*ck br*wn f*x"
print(recover_message(input_message))

def fill_missing_letters(word, clue):
    for letter in clue:
        word = word.replace('_', letter, 1)
    return word

# Example
input_word = "Th__at"
clue = "erc"
print(fill_missing_letters(input_word, clue))

def unique_names(names):
    return list(set(names))

# Example
input_names = "John Mary John Alex Alex".split()
print(" ".join(unique_names(input_names)))

def capitalize_sentences(paragraph):
    sentences = paragraph.split('. ')
    return '. '.join(sentence.capitalize() for sentence in sentences)

# Example
input_paragraph = "hello. my name is john. i love programming."
print(capitalize_sentences(input_paragraph))

def sort_destinations(destinations):
    return sorted(destinations)

# Example
input_destinations = "Paris Tokyo London NewYork"
print(" ".join(sort_destinations(input_destinations.split())))

def decrypt_message(encrypted, shift):
    decrypted = []
    for char in encrypted:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            decrypted.append(decrypted_char)
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Example
input_encrypted = "jgnnq"
shift_value = 2
print(decrypt_message(input_encrypted, shift_value))

def validate_passwords(passwords):
    results = []
    for password in passwords.split():
        strong = (len(password) >= 8 and 
                  any(c.isupper() for c in password) and 
                  any(c.islower() for c in password) and 
                  any(c.isdigit() for c in password))
        results.append("strong" if strong else "weak")
    return " ".join(results)

# Example
input_passwords = "Password123 hello123 GoodMorning2021 badpass"
print(validate_passwords(input_passwords))

def reverse_names(names):
    return " ".join(name.split()[1] + " " + name.split()[0] for name in names)

# Example
input_names = "John Doe Alice Johnson"
print(reverse_names(input_names.split()))

def format_movie_titles(titles):
    return " ".join(title.title() for title in titles.split())

# Example
input_titles = "the lord of the rings harry potter"
print(format_movie_titles(input_titles))

def merge_shopping_lists(list1, list2):
    return " ".join(set(list1 + list2))

# Example
list1 = "apples bananas oranges"
list2 = "bananas grapes apples"
print(merge_shopping_lists(list1.split(), list2.split()))

