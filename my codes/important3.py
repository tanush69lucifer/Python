def reverse_word(word):
    return word[::-1]

# Example
input_word = "mystery"
print(reverse_word(input_word))

def capitalize_names(names):
    return ' '.join(name.capitalize() for name in names.split())

# Example
input_names = "alice bob charlie"
print(capitalize_names(input_names))

def arrange_passengers(names):
    vowels = 'AEIOUaeiou'
    return ' '.join(name for name in names.split() if name[0] in vowels) + ' ' + ' '.join(name for name in names.split() if name[0] not in vowels)

# Example
input_names = "Alice Bob Eve Uma Charlie"
print(arrange_passengers(input_names))

def reverse_names(names):
    return ' '.join(names.split()[::-1])

# Example
input_names = "John Maria Ahmed"
print(reverse_names(input_names))

def encode_message(message):
    return ''.join(chr(ord(char) + 1) for char in message)

# Example
input_message = "hello"
print(encode_message(input_message))

def sort_prices(prices):
    return ' '.join(sorted(prices.split(), key=int))

# Example
input_prices = "500 100 2000 1500"
print(sort_prices(input_prices))

def count_words(paragraph):
    return len(paragraph.split())

# Example
input_paragraph = "This is a sample text for testing."
print(count_words(input_paragraph))

def sort_books(titles):
    return ' '.join(sorted(titles.split()))

# Example
input_titles = "The Hobbit Harry Potter War and Peace"
print(sort_books(input_titles))

def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

# Example
input_sentence = "I love programming"
print(reverse_sentence(input_sentence))
def shortest_word(sentence):
    return min(sentence.split(), key=len)

# Example
input_sentence = "I love playing games"
print(shortest_word(input_sentence))

