import logging

# def most_common_character(S):
#     ''' returns the first occurance of the most common character'''
#     occurrences = [0] * 26

#     for i in range(len(S)):
#         occurrences[ord(S[i]) - ord('a')] += 1

#     best_char = 'a'
#     best_res = 0

#     for i in range(0, 26):
#         if occurrences[i] > best_res:
#             best_char = chr(ord('a') + i)
#             best_res = occurrences[i]

#     return best_char

def solution(S):
    # declare 6 integers to track state and metrics.  Because len() is O(1), the next couple lines are constant
    # these cound the number of 'a' and 'b' chracters found 
    a_count, b_count= 0, 0
    # these track the sliding window
    left, right = 0, 0
    # this variable is not really needed, but I thougth it was good for debugging and readability
    length = len(S)
    # tracking maximum window size
    max_window = 0

    if length < 3:
        return length
    
    # Iterate through the list O(n) time
    for lcv in range(0, length):
        # Handle each letter using a helper funciton
        if S[lcv] == 'a':
            a_count, b_count, left, right = letter_handler(lcv, a_count, b_count, left, right)
        else:
            b_count, a_count, left, right = letter_handler(lcv, b_count, a_count, left, right)

        cur_window = right - left
        
        # output current window to debug console
        logging.debug(S[left:right+1])
        # by tracking maximum window size here, I handle the case of shorter windows existing after the first
        max_window = cur_window if cur_window > max_window else max_window

    return max_window

def letter_handler(cur_position, cur_counter, other_counter, left, right):
    ''' Handles the state transition for a sliding window of semi-alternating substrings

        returns a tuple containing counts of state occurances and the new substring window
    '''
    # I have an letter, so increment the current counter and reset the other counter
    cur_counter += 1
    other_counter = 0

    # slide or expand substring window forward
    if cur_counter < 3:
        right += 1
    else:
        left = cur_position-2
        cur_counter -= 1

    return (cur_counter, other_counter, left, right)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(solution('baaabbabbb'))
    logging.debug(solution('abab'))
    logging.debug(solution('baaabbabbb'))