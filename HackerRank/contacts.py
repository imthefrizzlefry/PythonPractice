#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
def contacts(queries):
    #
    # Write your code here.
    #
    trie = {}
    for q in queries:
        s = q[1]
        book = trie

        if q[0] == "add":
            for c in s:
                if c in book:
                    book[c][0] += 1 
                    book = book[c][1]
                else:
                    book[c] = [1, {}]
                    book = book[c][1]
        else:
            l = len(s)
            r = -2

            for i in range(l):
                if s[i] in book:
                    r = i
                    book = book[s[i]][1] if r < l-1 else book
                else:
                    print("0")
                    break
            
            if r == l-1:
                print(book[s[r]][0])
            





        

if __name__ == '__main__':
    with open("./HackerRank/contact_input.txt", 'r') as testInput:
        num_queries = int(testInput.readline().rstrip())
        queries = []

        for _ in range(num_queries):
            queries.append(testInput.readline().rstrip().split())

        contacts(queries)
    
    #contacts(["add hack", "add hackerrank", "find hac", "find hak"])

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # queries_rows = int(input())

    # queries = []

    # for _ in range(queries_rows):
    #     queries.append(input().rstrip().split())

    # result = contacts(queries)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
