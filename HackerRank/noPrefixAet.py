


def no_prefix_set(my_set):
    trie = {}
    problem = ""
    
    for s in my_set:
        c_trie = trie
        for c in s:
            if c not in c_trie:
                c_trie[c] = {}

            c_trie = c_trie[c]
            
            if '#' in c_trie:
                return "BAD SET\n{}".format(s)
    
        c_trie['#'] = True

        if len(c_trie) > 1:
            return "BAD SET\n{}".format(s)
        
    return "GOOD SET"
    

# n = int(input())
# my_set = []
# for _ in range(n):
#     my_set.append(input())

# no_prefix_set(my_set)

print(no_prefix_set(["aab","defgab","abcde","aabcde","cedaaa","bbbbbbbbbb","jabjjjad"]))
print(no_prefix_set(["a","a"]))