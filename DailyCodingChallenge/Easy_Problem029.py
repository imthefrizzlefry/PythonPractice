'''This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

def encode(s):
    if len(s) < 2: return "1" + s if len(s) > 1 else ""
    res = ""
    b=0
    e=1
    while b < len(s):
        while e < len(s) and s[b] == s[e]:
            e += 1
        res += str(e-b)
        res += s[b]
        b = e
        e += 1
    return res


def decode(s):
    if len(s) < 2: return ""

    res=""
    n=0
    c=1
    while n < len(s)-1:
        res += s[c]*int(s[n])
        n += 2
        c += 2
    return res

original = "AAAABBBCCDAA"

encoded = encode(original)
print(encoded)

decoded = decode(encoded)

print(decoded)