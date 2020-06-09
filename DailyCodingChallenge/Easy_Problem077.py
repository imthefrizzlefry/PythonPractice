''' This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
'''

def remove_overlapping_intervals(original):
    o_len = len(original)
    if o_len <= 1: return original

    original.sort(key=lambda x:x[0])
    ret_list = []
    i = 0

    while i < o_len:
        cur_tuple = original[i]
        if i+1 == o_len:
            ret_list.append(cur_tuple)
            i += 1
            continue
        next_tuple = original[i+1]

        if cur_tuple[1] < next_tuple[0]:
            ret_list.append(cur_tuple)
        else:
            new_tuple = (min(cur_tuple[0],next_tuple[0]),max(cur_tuple[1],next_tuple[1]))
            i+=1
            ret_list.append(new_tuple)

        i+=1

    return ret_list



if __name__ == "__main__":
    input_list = [(1, 3), (5, 8), (4, 10), (20, 25)]
    expected_list = [(1, 3), (4, 10), (20, 25)]

    result_list = remove_overlapping_intervals(input_list)
    print(result_list)
    assert  result_list == expected_list

    result_list = remove_overlapping_intervals([])
    assert  result_list == []

    result_list = remove_overlapping_intervals([(1,5)])
    assert  result_list == [(1,5)]

     