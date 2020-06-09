
# 
# Your previous C# content is preserved below:
# 
# using System;
# 
# // given a list of words:
# // ["steven", "steven", king", "king", "county", "hello", "world"]
# // i = 1
# // king - 2, steven - 2
# // i = 2
# // [king, steven]
# // i = 3
# // [king, steven, county]
# // func mostFreqWords(list words, int i ) => king
# 

# 
import collections

def most_freq_words(words, i):
    # setup
    memory = {}
    max_count = 0
    ret_list = []
    
    # preprocess
    for word in words:
        if word not in memory:
            memory[word] = 1
        else:
            memory[word] += 1
                
    # {steven: 2, king: 2}
    # lst.sort
    # sorted(memory,items(), key=lambda x:)
    
    
    for key in sorted(memory.items(), key=lambda x:x[1], reverse=True):
        if i > 0:    
            ret_list.append(key[0])
        i -= 1
            
    return ret_list


    import heapq
    counter = collections.Counter(words)
    max_heap = [(-freq, key) for key, freq in counter.items()]
    heapq.heapify(max_heap)
    return [heapq.heappop(_) for _ in range(i)]
    

word_list = ["steven", "steven", "king", "king", "county", "hello", "world"]
i = 3

print(most_freq_words(word_list, i))
