"""  Asked by Amazon

You are given a list of words:
['rock', 'star', 'rockstar', 'super', 'man', 'high', 'way', 'superman', 'superhighway', 'highway' 'rocks', 'tar']

Some of the words in the list may be formed by combining other words in the list together. For example,
rockstar, superman, and superhighway can be formed through the combination of other words.

Return a list of lists, like so:
[
    ['rock', 'star'],
    ['super', 'man'],
    ['super', 'high', 'way'],
    ['rocks', 'tar']
]
"""
ret_l = []

def complex_processor(c_w, w_l, built_word = None): # current_word, word_list
    if built_word is None:
        built_word = []
    #can we build c_w from words in w_l
    if c_w == "": 
        ret_l.append(built_word)
        return
    
    for i in range(len(w_l)):
        # find first word
        w = w_l[i]
        if c_w.startswith(w) and w != "":
            new_built_word = list(built_word)
            new_built_word.append(w)
            new_w_l = w_l[:i]+w_l[i+1:] if i != len(w_l)-1 else w_l[:i]

            complex_processor(c_w[len(w):], new_w_l, new_built_word)

def simple_from_complex(w_l): # w_l = word_list
    # input validation?
    
    
     
    for i in range(len(w_l)-1): # i = index
        # process
        c_w = w_l[i] # c_w = current_word
        if c_w == "":
            continue
        complex_processor(c_w, w_l[:i]+w_l[i+1:])
    
    return ret_l
    
    

            
        
        
simple_from_complex(['rock', 'star', 'rockstar', 'super', 'man', 'high', 'way', 'superman', 'superhighway', 'highway', 'rocks', 'tar', ""])

print(ret_l)