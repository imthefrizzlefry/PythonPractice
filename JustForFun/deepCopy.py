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