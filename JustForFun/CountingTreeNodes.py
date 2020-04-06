#!/bin/python

# given the root node of a tree, count the number of nodes

class Tree(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left=left
        self.right=right

    @staticmethod
    def node_count(root) -> int:
        # count = 0

        # if not root: return count

        # count += 1
        # count_queue = [root]

        # while count_queue:
        #     current = count_queue.pop(0)

        #     if current.left:
        #         count += 1
        #         count_queue.append(current.left)

        #     if current.right:
        #         count += 1
        #         count_queue.append(current.right)

        # return count
        return Tree.node_count(root.left) + Tree.node_count(root.right) + 1 if root else 0

def deepest(node):
    if node and not node.left and not node.right:
        return (node, 1) # Leaf and its depth

    if not node.left: # Then the deepest node is on the right subtree
        return increment_depth(deepest(node.right))
    elif not node.right: # Then the deepest node is on the left subtree
        return increment_depth(deepest(node.left))

    return increment_depth(
            max(deepest(node.left), deepest(node.right),
                    key=lambda x: x[1])) # Pick higher depth tuple and then increment its depth

def increment_depth(node_depth_tuple):
    node, depth = node_depth_tuple
    return (node, depth + 1)

if __name__ == '__main__':
    my_tree = Tree(1, Tree(2), Tree(3))
    print(Tree.node_count(my_tree))
    deepest_node = deepest(my_tree)
    print(deepest_node[0].value)
    print(deepest_node[1])
    print('-----------------')

    my_tree = Tree(1, Tree(2))
    print(Tree.node_count(my_tree))
    deepest_node = deepest(my_tree)
    print(deepest_node[0].value)
    print(deepest_node[1])
    print('-----------------')

    my_tree = Tree(1, right=Tree(2))
    print(Tree.node_count(my_tree))
    deepest_node = deepest(my_tree)
    print(deepest_node[0].value)
    print(deepest_node[1])
    print('-----------------')

    my_tree = Tree(1)
    print(Tree.node_count(my_tree))
    deepest_node = deepest(my_tree)
    print(deepest_node[0].value)
    print(deepest_node[1])
    print('-----------------')

    my_tree = None
    print(Tree.node_count(my_tree))
    # deepest_node solution requres a non-null solution
    # deepest_node = deepest(my_tree)
    # print(deepest_node[0].value)
    # print(deepest_node[1])
    # print('-----------------')

