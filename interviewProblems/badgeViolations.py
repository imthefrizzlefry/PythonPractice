import logging

''' asked by Karat on behalf of Indeed

We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room, write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room - they recorded an enter without a matching exit. (All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room - they recorded an exit without a matching enter. (The room is empty when the log begins.)

Each list should contain no duplicates, regardless of how many times a given employee matches the criteria for belonging to it.

badge_records_1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
]

Expected output: ["Curtis", "Paul"], ["Martha", "Curtis"]

Additional test cases:

badge_records_2 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], []

badge_records_3 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: [], ["Paul"]

badge_records_4 = [
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Martha", "enter"],
  ["Martha", "exit"],
]

Expected output: ["Paul"], ["Paul"]

badge_records_5 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

n: length of the badge records array

'''

def invalidBadgeLog(arr):
    invalidEntry = set()
    invalidExit = set()
    validEntry = set()
    
    for record in arr:
        if record[1] == 'enter' and record[0] in validEntry:
            # invalid enter
            invalidEntry.add(record[0])
        elif record[1] == 'enter' and record[0] not in validEntry:
            # valid entry  
            validEntry.add(record[0])
        elif record[1] == 'exit' and record[0] not in validEntry:
            # invalid exit
            invalidExit.add(record[0])
        elif record[1] == 'exit' and record[0] in validEntry:
            #valid exit
            validEntry.remove(record[0])
            
    for record in validEntry:
        invalidEntry.add(record)
        
    return [list(invalidEntry), list(invalidExit)]
         

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    badge_records_1 = [
        ["Martha",   "exit"],
        ["Paul",     "enter"],
        ["Martha",   "enter"],
        ["Martha",   "exit"],
        ["Jennifer", "enter"],
        ["Paul",     "enter"],
        ["Curtis",   "exit"],
        ["Curtis",   "enter"],
        ["Paul",     "exit"],
        ["Martha",   "enter"],
        ["Martha",   "exit"],
        ["Jennifer", "exit"],
        ["Paul",     "enter"],
        ["Paul",     "enter"],
        ["Martha",   "exit"],
    ]

    badge_records_2 = [
        ["Paul", "enter"],
        ["Paul", "enter"],
        ["Paul", "exit"],
    ]

    badge_records_3 = [
        ["Paul", "enter"],
        ["Paul", "exit"],
        ["Paul", "exit"],
    ]

    badge_records_4 = [
        ["Paul", "exit"],
        ["Paul", "enter"],
        ["Martha", "enter"],
        ["Martha", "exit"],
    ]

    badge_records_5 = [
        ["Paul", "enter"],
        ["Paul", "exit"],
    ]

    expected = ["Curtis", "Paul"], ["Martha", "Curtis"]
    logging.debug(invalidBadgeLog(badge_records_1))

    expected = ["Paul"], []
    logging.debug(invalidBadgeLog(badge_records_2))

    expected = [], ["Paul"]
    logging.debug(invalidBadgeLog(badge_records_3))

    expected = ["Paul"], ["Paul"]
    logging.debug(invalidBadgeLog(badge_records_4))

    expected = [], []
    logging.debug(invalidBadgeLog(badge_records_5))