'''This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
'''
def can_reach_last(int_list):
    i = 0

    while i < len(int_list):
        if i == len(int_list)-1:
            return True
        
        cur = int_list[i]

        if cur == 0:
            return False

        i += cur

    return False

if __name__ == "__main__":
    list_of_inputs = [([2, 0, 1, 0],True),
        ([1, 1, 0, 1],False),
        ([0],True),
        ([99999],True),
        ([99999,0,1],False),
        ([],False)]

    for input in list_of_inputs:
        my_list = input[0]
        expected_result = input[1]

        actual_result = can_reach_last(my_list)

        assert actual_result == expected_result