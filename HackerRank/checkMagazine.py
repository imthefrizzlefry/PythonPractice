from collections import Counter

def checkMagazine(magazine, note):
    return "Yes" if (Counter(note) - Counter(magazine)) == {} else "No"

def checkMagazine_tooSlow(magazine, note):
        
    for x in note:
        if x not in magazine:
            return "No"
        magazine.remove(x)

    return "Yes" if (Counter(note) - Counter(magazine)) == {} else "No"

# hacker rank made me print to screen... eeeewwwww
# I didn't bother writing unit tests for this one because HackerRank tested it for me...
def checkMagazine_PrintAnswer(magazine, note):
    
    print( "Yes" if (Counter(note) - Counter(magazine)) == {} else "No")