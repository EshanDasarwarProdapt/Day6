# Input string
text = input("Enter a string: ").lower()

# Dictionary to store vowel counts
vowel_count = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

# Count vowels
for char in text:
    if char in vowel_count:
        vowel_count[char] += 1

print("Vowel counts:")
print(vowel_count)
