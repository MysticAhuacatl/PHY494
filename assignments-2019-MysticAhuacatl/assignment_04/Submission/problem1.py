# Problem 4.

s = """'But I don't want to go among mad people,' Alice remarked.
'Oh, you can't help that,' said the Cat, 'we're all mad here. I'm
mad. You're mad.' 'How do you know I'm mad?' said Alice. 'You
must be,' said the Cat, 'or you wouldn't have come here.'"""

counts = [0,0,0,0,0,0]

def count_vowels(words):
    words = words.lower()
    for letter in words:
        if letter=='a':
            counts[0] += 1
        if letter=='e':
            counts[1] += 1
        if letter=='i':
            counts[2] += 1
        if letter=='o':
            counts[3] += 1
        if letter=='u':
            counts[4] += 1
        if letter=='y':
            counts[5] += 1

count_vowels(s)

print(counts)
