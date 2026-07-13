text = input("Enter a sentence: ")

words = text.split()

word_length = {}

for word in words:
    word_length[word] = len(word)

longest = max(word_length, key=word_length.get)

print("Longest word:", longest)
