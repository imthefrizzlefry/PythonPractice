# Asked by an ex-Googler during my Google Interview Prep
class Node:
	def __init__(self, value=0.0, children=[]):
		self.value = value
		self.children = children
		
	def deep_copy(self, history={}):
		
		if self in history:
			return history[self]
		else:
			newInstance = Node(self.value, [])
			history[self] = newInstance
			newInstance.children = [c.deep_copy(history) for c in self.children]
			return newInstance


if __name__ == '__main__':
	my_tree = Node(1, [Node(2), Node(3), Node(4)])

	print("{}{}".format("my_tree: ",id(my_tree)))
	print("{}{}".format("my_tree -> Child 1: ",id(my_tree.children[0])))
	print("{}{}".format("my_tree -> Child 2: ",id(my_tree.children[1])))
	print("{}{}".format("my_tree -> Child 3: ",id(my_tree.children[2])))

	new_tree = my_tree.deep_copy()

	print("{}{}".format("new_tree: ",id(new_tree)))
	print("{}{}".format("new_tree -> Child 1: ",id(new_tree.children[0])))
	print("{}{}".format("new_tree -> Child 2: ",id(new_tree.children[1])))
	print("{}{}".format("new_tree -> Child 3: ",id(new_tree.children[2])))

