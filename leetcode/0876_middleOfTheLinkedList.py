import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode( head: ListNode) -> ListNode:
    
    desired_result = middle_recursive(head, 1)
    return desired_result[0]

def middle_recursive( node, position):
    desired_result = None
    
    if node.next is not None:
        desired_result = middle_recursive(node.next, position+1)
        
        if desired_result[1] == position:
            return (node, position)
        else:
            return desired_result
    else:
        return (node, math.ceil(position/2)) if position%2 == 1 else (node, position/2+1)


if __name__ == "__main__":
    my_list = ListNode(1)
    # my_list.next = ListNode(2)
    # my_list.next.next = ListNode(3)
    # my_list.next.next.next = ListNode(4)
    # my_list.next.next.next.next = ListNode(5)
    # my_list.next.next.next.next.next = ListNode(6)
    print(middleNode(head=my_list).val)