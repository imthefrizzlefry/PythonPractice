'''
Binary tree 

serialize/deserialize 
    3  
  2   4   <==>  "3,2,;,;,4,;,;,"
'''

separator = ","
empty_node = "_"
class my_tree_node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

def serialize_tree(root):
    if root is None: return empty_node

    
    serialized_tree = str(root.val) + separator

    serialized_tree += serialize_tree(root.left) + separator
    serialized_tree += serialize_tree(root.right)

    return serialized_tree

def deserialize_tree(serialized_tree):
    
    node_list = serialized_tree.split(separator)

    return process_tree_nodes(node_list)

def process_tree_nodes(node_list):
    if node_list[0] == empty_node: 
        node_list.pop(0)
        return None

    val = int(node_list.pop(0))

    my_tree = my_tree_node(val)
    my_tree.left = process_tree_nodes(node_list)
    my_tree.right = process_tree_nodes(node_list)

    return my_tree

def print_tree(root, ending='\n'):
    if root is None: 
        print("None")
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)
    
def tree_example():
    my_tree = my_tree_node(4)
    my_tree.left = my_tree_node(2)
    my_tree.left.left = my_tree_node(1)
    my_tree.right = my_tree_node(6)

    my_tree_serialized = serialize_tree(my_tree)
    print(my_tree_serialized)

    new_tree = deserialize_tree(my_tree_serialized)

    print_tree(new_tree)

'''
Hangman solver
Given:
word_list
guess_letter(my_letter) ==> list of indexes for letter

Implement solve_puzzle(word_length)
'''
from collections import Counter
import heapq

hangman = "commercial"

def game_is_won(guess):
    return str(guess) == hangman

def guess_letter(my_letter):
    index_list = []
    for i, l in enumerate(hangman):
        if my_letter == l:
            index_list.append(i)

    return index_list

def get_possible_word_list(word_length, filename="./interviewProblems/my_word_list.txt"):
    filtered_word_list = []
    with open(filename, 'r') as my_websters:
        for word in my_websters:
            word = word.strip()
            if len(word) == word_length:
                filtered_word_list.append(word)

    return filtered_word_list
            
def count_letter_frequency(possible_words):
    cnt = Counter()
    letter_counts = []
    for words in possible_words:
        for letters in set(words):
            cnt[letters]+=1

    for letter in cnt.keys():
        heapq.heappush(letter_counts, (-cnt[letter], letter))

    return letter_counts

def update_solution(solution, current_letter, possible_indexes):
    for index in possible_indexes:
        solution[index] = current_letter
    return solution

def filter_possible_words(filter_letter, possible_indexes, possible_words):
    filtered_list = []
    for w in possible_words:
        possible = True
        if len(possible_indexes) > 0:
            for index in possible_indexes:
                if w[index] != filter_letter:
                    possible = False
                    break
        else:
            possible = filter_letter not in w

        if possible:
            filtered_list.append(w)

    return filtered_list


    return possible_words

def solve_puzzle(word_length):
    if word_length == 0: return ("", 0)
    num_guesses = 0
    guessed_letters = set()
    current_letter = None
    possible_words = get_possible_word_list(word_length)

    while len(possible_words) > 1:
        letter_counts = count_letter_frequency(possible_words)
        while current_letter is None or current_letter in guessed_letters: 
            current_letter = heapq.heappop(letter_counts)[1]

        num_guesses += 1
        guessed_letters.add(current_letter)
        possible_indexes = guess_letter(current_letter)

        possible_words = filter_possible_words(current_letter, possible_indexes, possible_words)
        

        
    return (possible_words[0], num_guesses)

def hangman_example():
    solution = solve_puzzle(len(hangman))

    print(solution)

'''
//Lets say we have a stream of integers like 3, 5, 6, 8, 1, 9, 34, 872, 4, 56, 76, 3, 38, 90, 87, 34 …..
// last 5 numbers in the stream at given point of time.
'''



class my_node:
    def __init__(self, val):
        self.val = val
        self.next = None


class my_queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.Nodes = None
        self.count = 0

    def push(self, val):

        if self.count < 1:
            self.head = my_node(val)
            self.tail = self.head
            self.count += 1
        elif self.count < 5:
            self.tail.next = my_node(val)
            self.tail = self.tail.next
            self.count += 1
        else:
            self.tail.next = my_node(val)
            self.tail = self.tail.next
            self.head = self.head.next
            
    def pop(self):
        if self.count == 0: return None
        temp = self.head.val
        self.head = self.head.next
        self.count -= 1
        return temp    
        
numberqueue = my_queue()

def insert_number(num):
    numberqueue.push(num)
        
def get_last_five():
    last_five = []
    num = numberqueue.pop()
    while num is not None:
        last_five.append(num)
        num = numberqueue.pop()
        
    return last_five

def queue_example():
    for i in range(10):
        insert_number(i)
    print(get_last_five())

if __name__ == "__main__":
    hangman_example()   
    