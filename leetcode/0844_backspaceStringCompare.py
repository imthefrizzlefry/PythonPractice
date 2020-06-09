def backspaceCompare(S: str, T: str) -> bool:
        return process(S) == process(T)
                
def process(s):
    temp = []
    for c in s:
        if c != '#':
            temp.append(c)
        elif len(temp) > 0:
            temp.pop()
    return ''.join(temp)

if __name__ == "__main__":
    print(backspaceCompare("ab#c", "ad#c"))
    print(backspaceCompare("ab##", "c#d#"))
    print(backspaceCompare("a##c", "#a#c"))
    print(backspaceCompare("a#c", "b"))