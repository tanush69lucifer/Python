def reverse_string(s):
    return s[::-1]

# Example
print(reverse_string("hello"))  # Output: "olleh"

def is_palindrome(s):
    return s == s[::-1]
# Examples
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')
def count_vowels(s):
    return(1 for char in s.lower() if char in 'aeiou')

# Examples
print(count_vowels("apple"))   # Output: 2
print(count_vowels("python"))  # Output: 1

def remove_spaces(s):
    return s.replace(" ", "")

# Example
print(remove_spaces("hello world"))  # Output: "helloworld"

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Examples
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("apple", "pale"))      # Output: False

def longest_word(s):
    return max(s.split(), key=len)

# Example
print(longest_word("The quick brown fox"))  # Output: "quick"

def url_encode(s):
    return s.replace(" ", "%20")

# Example
print(url_encode("hello world"))  # Output: "hello%20world"

def char_frequency(s):
    return {char: s.count(char) for char in set(s)}

# Example
print(char_frequency("apple"))  # Output: {'a': 1, 'p': 2, 'l': 1, 'e': 1}

def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# Example
print(first_non_repeating("swiss"))  # Output: "w"

def are_rotations(s1, s2):
    return len(s1) == len(s2) and s1 in (s2 + s2)

# Examples
print(are_rotations("abcde", "deabc"))  # Output: True
print(are_rotations("abcde", "abced"))   # Output: False

from itertools import permutations

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

# Example
print(all_permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

def most_frequent_word(s):
    words = s.split()
    return max(set(words), key=words.count)

# Example
print(most_frequent_word("apple banana apple orange banana apple"))  # Output: "apple"

def contains_only_digits(s):
    return s.isdigit()

# Examples
print(contains_only_digits("12345"))  # Output: True
print(contains_only_digits("123a5"))  # Output: False

def longest_unique_substring(s):
    char_map = {}
    left = max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Example
print(longest_unique_substring("abcabcbb"))  # Output: 3 ("abc")

def group_anagrams(words):
    anagrams = {}
    for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)
    return list(anagrams.values())

# Example
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def is_match(s, p):
    import re
    pattern = p.replace('*', '.*').replace('?', '.')
    return re.fullmatch(pattern, s) is not None

# Example
print(is_match("abc", "a*c"))  # Output: True

def longest_unique_substring(s):
    char_map = {}
    left = max_length = 0

    for right in range(len(s)):
        if s[right] in char_map:
            left = max(left, char_map[s[right]] + 1)
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Example
print(longest_unique_substring("abcabcbb"))  # Output: 3
