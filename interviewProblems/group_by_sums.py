'''
value    neg     pos    total
   -6
   -2      8       0        8
   -1
   +1
   +0
   +1
   +5      1       7        8
   -1
   -1
   -1
   +5      3       5        8
   +1


[(8,0),(1,7)...]

([1, 3, -6], 5) -> [(1,4),(5,0)]

value    neg     pos    total
   -6      5       0        5   # -> -1
   -2      
   -1
   +1      4       1        5  # -> 0
   +0
   +1                    # 0, 1, 1, 0
   +5      0       5        5   # -> +1        # 0, 5, 5, 1
   -1
   -1
   -1
   +5      3       2        5   # -> +4
   +1      0       5        5
'''

def group_by_increment(my_list, target):
    neg, pos, total = 0, 0, 0
    ret_list = []

    for val in my_list:
        if val >= 0:
            if total + val < target:
                pos += val
                total += val
            else:
                remainder = val - (target - total)
                pos += target - total
                total = target
                ret_list.append((neg, pos, total))
                total = remainder
                pos = remainder
                neg = 0

        else:
            if total + -val <= target:
                neg += -val
                total += -val
            else:
                remainder = -val - (target - total)
                neg += target - total
                total = target
                ret_list.append((neg, pos, total))
                total = remainder
                pos = 0
                neg = remainder

    ret_list.append((neg, pos, total))

    return ret_list

if __name__ == "__main__":
    print(group_by_increment([-6,-2,-1,1,0,1,5,-1,-1,-1,5,1], 8))
    print("------------------------------")
    print(group_by_increment([1, 3, 6], 5))
    print("------------------------------")
    print(group_by_increment([-6,-2,-1,1,0,1,5,-1,-1,-1,5,1], 5))