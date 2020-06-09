''' Asked by Google

The task is based on the games Scrabble and Quiddler. Each player gets a certain number of letters with different scores. The goal is to form words with as many of the letters as possible and with as few leftover letters. The player’s score is equal to the sum of scores for each letter in the words created minus the sum of scores for leftover letters.
Example:
Players hand:
Letter Score
A 1
C 4
D 2
T 1
O 1
G 2
J 8
We can create the following word combination:
CAT (6 points), DOG (5 points). But we didn’t use letter J (8 points).
The score is equal = 6 + 5 - 8 = 3 points.
The task is to write a program that will find the best combination (with the highest score) of words out of a given set of letters.

[“A”, “C”, ...]

point_lookup = {}
is_word(str_word) ⇒ -1(not a word), 0 (is a word), 2(possible words)

def scrabble_score(tiles, starting=””):
    result_set = {} # key = starting letter : value = list words
    for i, letter in enumerate(tiles):
        current_list = [].extend(tiles)
        starting += letter
        if is_word(starting) > 0:
            score += scrabble_score(tiles[:i].extend(tiles[i+1:]), starting)
        if == 0:
            #score keeping
        if a not in result_set:
            result_set[a] = []
    result_set[a].append(place_holder)

'''
import heapq
from collections import Counter
import logging

def add_word_to_word_list_trie(word, root):
    #Trie layout:
    # { char  : ( bool  ,   -int   ,  int  ,   dict  )}
    # {letter : (is_valid_word, next_word, points, children)}
    # Example:
    # Given "CAT"
    # Creates: {'C': (False, -2, 3, {'A': (False, -1, 4, {'T': (True, 0, 5, {})})})}
    # scrabble score chart
    cur = root
    score = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2, 
            "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3, 
            "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1, 
            "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4, "X": 8, "Z": 10}

    word_score = 0

    for i, letter in enumerate(word):
        word_score += score[letter]
        next_word = i+1-len(word)

        if letter not in cur:
            cur[letter] = (i+1 == len(word), next_word, word_score, {})
        else:
            cur_is_word = i+1 == len(word) if not cur[letter][0] else True
            cur_next = next_word if cur[letter][1] == 0 else max(next_word, cur[letter][1])
            cur_children = cur[letter][3]

            cur[letter] = (cur_is_word, cur_next, word_score, cur_children)

        cur = cur[letter][3]

def build_trie_for_word_list(word_list, filename="./interviewProblems/my_word_list.txt"):
    # Example:
    # Valid Words: ["CAT", "CATS", "DOG", "JOG", "ACT"]
    # word_list = {'A':(False, -2, 1, {'C':(False, -1, 4, {'T':(True, 0, 5, {})})}),
    #             'C':(False, -2, 3, {'A':(False, -1, 4, {'T':(True, -1, 5, {'S':(True, 0, 6, {})})})}),
    #             'D':(False, -2, 2, {'O':(False, -1, 3, {'G':(True, 0, 5, {})})}),
    #             'J':(False, -2, 8, {'O':(False, -1, 9, {'G':(True, 0, 11, {})})})
    #             }
    #my_dictionary = ["CAT", "CATS", "DOG", "JOG", "ACT"]

    with open(filename, 'r') as my_websters:
        for word in my_websters:
            add_word_to_word_list_trie(word.rstrip().upper(), word_list)

    #logging.debug(word_list)

def is_word(str_word):
    ''' returns: tuple
        a negative number if that number of letters can make a word
        zero if is not and can not be a word
        a positive number for the point value of the word created
    '''
    
    word_list = {}
    build_trie_for_word_list(word_list)
    
    cur = word_list
    is_valid_word = None
    next_word = 0
    points = 0
    for letter in str_word:
        if letter in cur:
            is_valid_word, next_word, points, cur = cur[letter]
            
        else:
            return (False, 0, 0) # not a word, cannot add letters to make a word

    return (is_valid_word, next_word, points) # is a word, might be able to add letters to create a different word, grants points

def create_word_list(letter_list, my_words=None, checked=None, cur=''):

    if my_words is None:
        my_words = []

    if checked is None:
        checked = set()

    for i in range(len(letter_list)):
        cur += letter_list[i]

        if cur not in checked:
            status = is_word(cur)

            
            if not status[0] and status[1] == 0:
                checked.add(cur)
            else:
                if status[0]:
                    heapq.heappush(my_words, (-status[2], cur))
                    checked.add(cur)

                if status[1] < 0: 
                    pre_list = letter_list[:i]            
                    post_list = letter_list[i+1:] if i+1 < len(letter_list) else []            
                    create_word_list(pre_list+post_list, my_words, checked, cur)
                
        cur = cur[:-1]

    return my_words

def unique_scores(word_list, letter_list):
    max_score = 0
    ret_list = {}
    # get count of each letter I have
    counted_letters = Counter(letter_list)
    ordered_words = []
    while len(word_list) > 0:
        ordered_words.append(heapq.heappop(word_list))

    for i, cur in enumerate(ordered_words):
        # check for overlapping words
        cur_score, cur_word = cur

        available_letters = dict(counted_letters)

        for letter in cur_word:
            available_letters[letter] -= 1
        temp_list =[cur_word]
        
        i_remaining = i+1

        while i_remaining < len(ordered_words):
            next_score, next_word = ordered_words[i_remaining]
            if can_make_word(next_word, available_letters):
                temp_list.append(next_word)
                cur_score += next_score
            i_remaining += 1
        
        if cur_score < max_score:
            ret_list = list(temp_list)
            max_score = cur_score

    return (-max_score, ret_list)

    #for cur in word_list

def can_make_word(word, available_letters):
    word_letter_count = Counter(word)

    # do we have available letters
    for key in word_letter_count.keys():
        if word_letter_count[key] > available_letters[key]: return False

    # we have all required available letters, so use the letters
    for key in word_letter_count.keys():
        available_letters[key] -= word_letter_count[key]

    return True

def find_the_best_scrabble_combination(my_letters):
    my_words = create_word_list(my_letters)
    logging.debug(my_words)
    best_score = unique_scores(my_words, my_letters)
    return best_score



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    my_letters = ["A", "C", "D", "T", "O", "G", "J", "S", "O", "G"]
    logging.debug(my_letters)
    logging.debug(find_the_best_scrabble_combination(my_letters))




#largest = heapq.heappop(my_words)
#print(largest)



# all_words = {}
# add_word_to_word_list_trie("CAT", all_words)
# add_word_to_word_list_trie("CATS", all_words)
# print(all_words)


# extra stuff I didn't need...

# def word_overlap(word1, word2):
#     shared_letters = {}

#     for letter in word1:
#         num_occurances = is_letter_in_word(word2, letter)
#         if num_occurances > 0:
#             shared_letters[letter] = num_occurances

#     return shared_letters

# def is_letter_in_word(word, letter):
#     count = 0
#     for c in word:
#         if c == letter:
#             count += 1
#     return count





# def create_word_trie(letter_list, word_trie={}, prev_word = ""):
#     for i in range(len(letter_list)):
#         cur_letter = letter_list[i]
#         cur_word = prev_word + cur_letter
        
#         word_trie[cur_letter] = {} if not is_word(cur_word) else {'*': True}

#         remainder = letter_list[:i]
#         if i < len(letter_list)-1 :
#             remainder += letter_list[i+1:] 
        
#         create_word_trie(remainder, word_trie[cur_letter], cur_word)

#     return word_trie


