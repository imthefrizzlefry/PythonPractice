'''This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class link_list:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def build_memory(my_list):
    mem = {}
    while my_list is not None:
        mem[my_list.val] = True
        my_list = my_list.next

    return mem

def find_in_memory(mem, my_list):
    while my_list is not None:
        if my_list.val in mem:
            return my_list.val

        my_list = my_list.next

    return -1

def find_intersection(a: link_list, b: link_list) -> int:
    memory = build_memory(a)

    return find_in_memory(memory, b)



#driver code
list_a = link_list(0)
cur_node = list_a
for i in range(1,3):
    cur_node.next = link_list(i)
    cur_node = cur_node.next

list_b = link_list(4)
cur_node = list_b
for i in range(5,8):
    cur_node.next = link_list(i)
    cur_node = cur_node.next

cur_node.next = link_list(2)

print(find_intersection(list_a, list_b))