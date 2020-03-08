import logging

''' asked by Karat on behalf of Indeed

We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period, and returns each time that they badged in during that period. (If there are multiple one-hour periods where this was true, just return the first one.)

badge_times = [
  ["Paul",     1355],
  ["Jennifer", 1910],
  ["John",      830],
  ["Paul",     1315],
  ["John",     1615],
  ["John",     1640],
  ["John",      835],
  ["Paul",     1405],
  ["John",      855],
  ["John",      930],
  ["John",      915],
  ["John",      730],
  ["Jennifer", 1335],
  ["Jennifer",  730],
  ["John",     1630],
  ["John",     2215],
  ["John",     2230],
  ["Paul",     1225],
    };


]

Expected output (in any order)
  John:  830  835  855  915  930
  Paul: 1315 1355 1405

n: length of the badge records array

'''

def frequentBadgers(arr):
    timeLog = {}
    personList = []
    
    for entry in arr:
        if entry[0] not in timeLog.keys():
            timeLog[entry[0]] = [entry[1]]
        else:
            timeLog[entry[0]].append(entry[1])
            
    
    for person in timeLog.keys():
        logging.debug(person)
        counter = 1
        s=0
        timeLog[person].sort()
        logging.debug(timeLog[person])
        for i in range(1, len(timeLog[person])):

            logging.debug(''.join([str(timeLog[person][s]),":",str(timeLog[person][i])]))
            if timeLog[person][i]-timeLog[person][s] < 100:
                counter = counter+1
                logging.debug("found")
                if counter == 3:
                    logging.debug("Breaking Loop")
                    break
            else:
                s=s+1
                if s != i and timeLog[person][i]-timeLog[person][s] < 100:
                    logging.debug("counter left alone")
                else:
                    counter = 1
                    logging.debug("counter reset")
        if counter >= 3:
            personList.append(person)
            
        logging.debug(personList)
    return {key:val for key, val in timeLog.items() if key in personList} 
    
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    badge_times = [
        ["Paul",     1355],
        ["Jennifer", 1910],
        ["John",      830],
        ["Paul",     1315],
        ["John",     1615],
        ["John",     1640],
        ["John",      835],
        ["Paul",     1405],
        ["John",      855],
        ["John",      930],
        ["John",      915],
        ["John",      730],
        ["Jennifer", 1335],
        ["Jennifer",  730],
        ["John",     1630],
        ["John",     2215],
        ["John",     2230],
        ["Paul",     1225],
    ]
    logging.debug(frequentBadgers(badge_times))