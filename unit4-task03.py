import string

sentence = input("Enter a sentence: ")
words = sentence.lower().translate(
    str.maketrans("", "", string.punctuation)
).split()

word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

for word, count in word_counts.items():
    print(f"{word}: {count}")