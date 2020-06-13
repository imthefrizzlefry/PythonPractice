import re

def is_palendrome(word):
    forward = ''.join(re.findall(r'[a-z]+', word.lower()))
    backward = forward[::-1]
    return forward == backward


if __name__ == "__main__":
    inputs = [
        ("racecar",True),
        ("Wedding",False),
        ("hello world",False),
        ("Go hang a salami - I'm a lasagna hog.", True)
    ]

    for pair in inputs:
        value = pair[0]
        expected_result = pair[1]

        actual_result = is_palendrome(value)

        print("{} => {}".format(value, actual_result))
        assert actual_result == expected_result

