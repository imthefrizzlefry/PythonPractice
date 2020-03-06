# Asked by a Googler during a phone interview
#Find the odd one out: 
# Given a list of words paired with attributes, 
# find the word that should be excluded to maximize the number of common attributes among the remaining words. 
# Please begin with the first solution that comes to mind; we can discuss optimization later.


# Given:
word_dict = {}
word_dict['cow'] = set(['animal', 'mammal', 'white', 'big', 'slow', 'herbivore'])
word_dict['dog'] = set(['animal', 'mammal', 'brown', 'pet', 'carnivore'])
word_dict['spider'] = set(['animal', 'arthropod', 'spooky'])
word_dict['cat'] = set(['animal', 'mammal', 'white', 'pet', 'carnivore', 'cute'])

def commonCount (myDict):
    keys = list(myDict.keys())
    curPlace = 0
    tempList = []
    while curPlace < len(keys):
        if(curPlace > 0):
            #x.append(inst for inst in *keys[0:curPlace]
            #tempList.extend(x)
            print("not implemented") 
        print(*keys[curPlace+1:])
        #tempList.extend(*keys[curPlace+1:])
        commonList = myDict[keys[curPlace]].intersection(*[myDict[val] for val in keys if keys[curPlace] != val])
        yield (keys[curPlace], len(commonList)) 
        curPlace += 1

for i in commonCount(word_dict):
    print(i)