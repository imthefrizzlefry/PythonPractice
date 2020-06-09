import logging

''' This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''

def findSumOfK(s, k):
    ''' return boolean indicating whether any two numbers from the list s add up to k '''
    logging.debug(s)
    logging.debug(k)
    #create an empty set of compliments needed for reach K
    compList = set()

    #for each num a in s, see if k-a in in the compliment set
    for a in s:
        # if found, return true otherwise add the compliment
        comp = k-a   
        logging.debug(comp)

        if a in compList:
            logging.debug("Found Compliment")
            return True
        else:
            logging.debug("Adding Compliment To List")
            compList.add(comp)
            
    logging.debug("Compliment Not Found")
    return False

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    s = [10, 15, 3, 7]
    k = 17

    findSumOfK(s, k)

    