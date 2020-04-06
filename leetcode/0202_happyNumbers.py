def isHappy(n: int) -> bool:
    visited = set()
    while n != 1 and not n in visited:
        visited.add(n)
        n = sum(map(lambda x:int(x)**2, str(n)))
    return not n in visited

if __name__ == "__main__":
    print(isHappy(13))
    print(isHappy(19))
    print(isHappy(22))