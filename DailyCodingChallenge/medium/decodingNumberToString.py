import logging
import string
import math
'''This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def decoding_number_to_string(my_num):
    logging.debug(my_num)
    num2alphadict = dict(zip(range(1, 27), string.ascii_lowercase))
    lower_remainder = my_num % 10
    upper_remainder = my_num % 100
    result_list = []
    
    

    if lower_remainder > 0:
        # process 1 - 9
        result_list.append(num2alphadict[lower_remainder])    

    if upper_remainder > 9 and upper_remainder <= 26:
        # process 10 - 26        
        result_list.append(num2alphadict[upper_remainder])
    
    if my_num > 10:
        # shift and repeat
        result_list = result_list + decoding_number_to_string(int(my_num / 10))
    
    return result_list

def decode_cnt_no_zero(msg_list):
    if len(msg_list) <= 1:
        return 1

    if len(msg_list) >= 2:
        if 1 <= int(''.join(msg_list[0:2])) <= 26:
            return  (decode_cnt_no_zero(msg_list[1:]) +
                        decode_cnt_no_zero(msg_list[2:]))
        return decode_cnt_no_zero(msg_list[1:])


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    n = '26'

    #result = decoding_number_to_string(n)
    #logging.debug(result)

    result = decode_cnt_no_zero(n)
    logging.debug(result)

