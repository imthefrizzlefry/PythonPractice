class node:
    def __init__(self, val=None, prev=None, next=None):
        self.val=val
        self.prev=prev
        self.next=next
        
class double_link_list:
    def __init__(self, val=None):
        self.link_list = node(val)
        self.head = self.link_list
        self.tail = self.link_list

    def add_node(self, val, tail=True):
        if self.head.val is None:
            self.head.val = val
            return
        if tail:
            temp = node(val=val, prev=self.tail)
            self.tail.next = temp
            self.tail = self.tail.next
        else:
            temp = node(val=val, next=self.head)
            self.head.prev = temp
            self.head = self.head.prev

    def clear_list(self):
        # I should use temp for garbage collection, but I don't care for this exercise...
        self.head = node()
        self.tail = self.head

    def list_to_linked_list(self, py_list):
        i = 0
        if self.head.val is not None:
            self.clear_list()

        while i < len(py_list):
            self.add_node(py_list[i])
            i += 1


def is_palendrome(link_list):
    '''
    pre-condition: we have a doubly linked list with one or more elements
    actions: comparing vales without making changes to the original list
    post-condition: returning true or false for is it a palendrome
    '''

    # make references to head and tail
    start = link_list.head
    end = link_list.tail

    # iterate from ends toward middle until head and tail are the same thing
    while start is not end:
        # compare the values for beginning and end
        if start.val != end.val:
            # return false if they are not equal
            return False

        #if there are an even number of nodes, break loop if the nodes are neighbors
        if start.next is end:
            break

        # move references toward the middle
        start = start.next
        end = end.prev

    # if we make it to the end, we have a palindrome
    return True

if __name__ == "__main__":

    my_link_list = double_link_list()

    my_link_list.list_to_linked_list([1,2,3,4,3,2,1])

    print(is_palendrome(my_link_list))

    my_link_list.list_to_linked_list([1,4,3,3,4,1])

    print(is_palendrome(my_link_list))

    my_link_list.list_to_linked_list([1,4])

    print(is_palendrome(my_link_list))
