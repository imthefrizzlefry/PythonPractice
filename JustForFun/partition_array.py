from collections import defaultdict

''' https://youtu.be/BFKbbE9Tpqs

'''
def partiton(array):
    dict = defaultdict(set)
    dict[0].add(0)

    for i, elem in enumerate(array):
        current = i+1
        for prev_diff in dict[current-1]:
            dict[current].add(prev_diff - elem)
            dict[current].add(prev_diff + elem)

    return 0 in dict[len(array)]





if __name__ == "__main__":
    print(partiton([3,1,2]))
    print(partiton([3,2,2]))


