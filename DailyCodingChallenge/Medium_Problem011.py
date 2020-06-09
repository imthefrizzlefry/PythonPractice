'''This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''
class PrefixTrie(object):
    def __init__(self):
        self.nodes = {}

    def insert(self, word):
        node = self.nodes
        for l in word:
            if l not in node:
                node[l] = {}
            node = node[l]
        
        node['#'] = {}

    def search(self, word):
        node = self.nodes

        for l in word:
            if l not in node:
                return False

            node = node[l]

        if '#' in node:
            return True

        return False

    def starts_with(self, prefix):
        node = self.nodes
        for l in prefix:
            if l not in node:
                return []
            node = node[l]           

        return self.suggestions(node)

    def suggestions(self, node):
        res = []

        for l in node:
            v = [''] if l == '#' else [l + s for s in self.suggestions(node[l])]
            res.append(*v)

        return res
            

            

def autocomplete(q, p):
    dictionary = PrefixTrie()

    for w in p:
        dictionary.insert(w)
    
    return [q + s for s in dictionary.starts_with(q)]


if __name__ == '__main__':
    print(autocomplete('de', ['dog', 'deer', 'deal']))

    print(autocomplete('el', ['dog', 'deer', 'deal']))
