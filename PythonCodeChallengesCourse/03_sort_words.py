

def sort_words(sentence):
    words = sentence.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return ' '.join(words)

if __name__ == "__main__":
    inputs = [
        ("string of words", "of string words"),
        ("banana ORANGE apple", "apple banana ORANGE")
    ]

    for pair in inputs:
        value = pair[0]
        expected_result = pair[1]

        actual_result = sort_words(value)

        print("{} => {}".format(value, actual_result))
        assert actual_result == expected_result