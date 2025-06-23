import itertools
words = ['SEND', 'MORE', 'MONEY']
unique_letters = set(''.join(words))
if len(unique_letters) > 10:
    print("Too many unique letters for digits 0-9.")
else:
    for perm in itertools.permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, perm))
        if any(letter_to_digit[word[0]] == 0 for word in words):
            continue
        word_values = {word: sum(letter_to_digit[letter] * (10 ** i) for i, letter in enumerate(reversed(word))) for word in words}
        if sum(word_values[word] for word in words[:-1]) == word_values[words[-1]]:
            print(f"Solution found:")
            for word, value in word_values.items():
                print(f"{word}: {value}")
            print(f"Mapping: {letter_to_digit}")