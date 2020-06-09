#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    l = {")":"(", "]":"[", "}":"{"}
    q = []
    for b in s:
        if b in "{[(":
            q.append(b)
        else:
            if not q: return "NO"

            c = q.pop()
            if c != l[b]:
                return "NO"
    
    return "YES" if q == [] and s else "NO"


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #t = int(input())
    # for t_itr in range(t):
    #     s = input()
    #     result = isBalanced(s)
    #     fptr.write(result + '\n')
    # fptr.close()
    print(isBalanced("{[()]}"))
    print(isBalanced("{[(])}"))
    print(isBalanced("{{[[(())]]}}"))
    print("----------------------------------")

    print(isBalanced("{{([])}}"))
    print(isBalanced("{{)[](}}"))
    print("----------------------------------")

    print(isBalanced("{(([])[])[]}"))
    print(isBalanced("{(([])[])[]]}"))
    print(isBalanced("{(([])[])[]}[]"))
    print("----------------------------------")

    print(isBalanced("}][}}(}][))]"))
    print(isBalanced("[](){()}"))
    print(isBalanced("()"))
    print(isBalanced("({}([][]))[]()"))
    print(isBalanced("{)[](}]}]}))}(())("))
    print(isBalanced("([[)"))
    print("----------------------------------")

    print(isBalanced(""))
    print("----------------------------------")