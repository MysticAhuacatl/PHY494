# Problem 4.1

# this could be done more elegantly with a dictionary or directly with
# collections.Counter --- see
# https://docs.python.org/3/library/collections.html#counter-objects

def count_vowels(s):
    s = s.lower()
    counts = [0, 0, 0, 0, 0, 0]
    # smarter:
    #    vowels = "aeiouy"
    #    counts = len(vowels) * [0]
    for letter in s:
        if letter == "a":
            counts[0] += 1
        elif letter == "e":
            counts[1] += 1
        elif letter == "i":
            counts[2] += 1
        elif letter == "o":
            counts[3] += 1
        elif letter == "u":
            counts[4] += 1
        elif letter == "y":
            counts[5] += 1
    return counts



text = """'But I don't want to go among mad people,' Alice remarked.
'Oh, you can't help that,' said the Cat, 'we're all mad here. I'm mad. You're mad.'
'How do you know I'm mad?' said Alice.
'You must be,' said the Cat, 'or you wouldn't have come here.'"""

counts = count_vowels(text)
