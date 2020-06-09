import queue

def popularNFeatures(numFeatures, topFeatures, possibleFeatures, 
                     numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    # we want to count occurances for each word (possible feature), in the sentences (feature featureRequests)
    
    #priority queue to store top features, so it is always sorted
    # then we want to drop the smallest when count > topFeatures
    q = queue.PriorityQueue()
    
    for pf in possibleFeatures:
        pf_count = 0
        for fr in featureRequests:
            if fr.count(pf) > 0: # if the request has at least one mention of possibleFeature
                pf_count += 1 # increment count for that possible feature
        q.put((-pf_count, pf)) # put a tuple in the PriorityQueue
        
    return_list = []
    while topFeatures > 0:
        return_list.append(q.get()[1])
        topFeatures -= 1
        
    return return_list

import queue
from collections import Counter

def popularNFeatures(numFeatures, topFeatures, possibleFeatures, 
                     numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    # we want to count occurances for each word (possible feature), in the sentences (feature featureRequests)
    
    #priority queue to store top features, so it is always sorted
    # then we want to drop the smallest when count > topFeatures
    q = queue.PriorityQueue()
    
    # so it solves the base cases, but time complexity is too long with nested for loops
    # counter is the solution
    data_set = []
    for fr in featureRequests:
        # split into words, and and remove duplicates
        split_set = list(dict.fromkeys(fr.split()))
        data_set.extend(split_set)
        
   
    for word in Counter(data_set):
        if word[0] in possibleFeatures:
            q.put((-word[1], word[0])) # put a tuple in the PriorityQueue, negative to make

        
    return_list = []
    while topFeatures > 0:
        return_list.append(q.get()[1])
        topFeatures -= 1
        
    return return_list

print(popularNFeatures(5, 2, ['a', 'b', 'c', 'd', 'e'], 3, ["a f g h i j k l m n", "l o p b q r s t", "u v a x y z"]))

def reorderElements(logFileSize, logLines):
    # WRITE YOUR CODE HERE
    num_list = []
    word_list = []
    
    #iterate through lines and separate words from numbers
    for line in logLines:
        if line[-1].isdigit():
            num_list.append(line)
        else:
            word_list.append(line)
            
    # need to sort the word list by everything after the first space
    
    
    word_list.extend(num_list)
    
    return word_list
    
    # it may be better to sort within the for loop to try and get closer to O(n) time complexity
    # I think there is a sort method that allows a lambda as a second parameter
    

    import queue

def popularNFeatures(numFeatures, topFeatures, possibleFeatures, 
                     numFeatureRequests, featureRequests):
    # WRITE YOUR CODE HERE
    # we want to count occurances for each word (possible feature), in the sentences (feature featureRequests)
    
    #priority queue to store top features, so it is always sorted
    # then we want to drop the smallest when count > topFeatures
    q = queue.PriorityQueue()
    
    for pf in possibleFeatures:
        pf_count = 0
        for fr in featureRequests:
            if fr.count(pf) > 0: # if the request has at least one mention of possibleFeature
                pf_count += 1 # increment count for that possible feature
        q.put((-pf_count, pf)) # put a tuple in the PriorityQueue
        
    return_list = []
    while topFeatures > 0:
        return_list.append(q.get()[1])
        topFeatures -= 1
        
    return return_list
    
    
# running out of time, so moving on.  I should replace the nested for loops with:
# if I get time, I would break out each feature request into a list of unique words, 
# and extend all those lists into a single dataset

# then I will count the occurances of all the words using collections counter
# iterate through the counted words found in possible features and add them to the 
# PriorityQueue using the negative counts.

