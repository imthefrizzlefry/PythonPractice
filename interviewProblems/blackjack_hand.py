''' asked by Avalara

implement a method for calculating a blackjack score

['ace', 'ace', 'ace', 'ace', '2', '2', '2', '2', '3', '3', '3'] => 21
['ace','ace'] => 12
5, 7, 10 => 0
ect...

write this method and test it

I forgot to include all my tests here, but I included:
1 test for each card alone as the hand
jack jack ace => 21
queen queen jack => 0

'''




# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def get_value_for_card(card):
    '''
    input: a string value representing a card name in this list:
        ['2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING','ACE']
    returns: a number between 1 and 11 inclusively

    Assumptions:
    - we do not need to guarantee case for face card names    
    '''
    # throw an exception if the card name is invalid
    assert card.upper() in ['2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING','ACE']

    if len(card) > 3:
        # return 10 for face cards
        return 10
    elif len(card) == 3:
        # return lower value for ace card
        return 1
    elif len(card) == 2:
        # ten is only number with 2 characters
        return 10
    else:
        assert int(card) > 1
        #calculate value based on string value
        return int(card)

def calculate_blackjack_hand(hand):
    '''
    input: a list of card names, where each card name is a string
    returns: a score of 1-21 for the card values, or zero if the score is greater than 21

    Assumptions:
    - the card names are correct
    - empty list is valid input, and is handled by the for loop
    '''
    # we need to track if we have one or more ace card
    have_ace = False

    # initialize our score at zero, then count as we iterate through the hand
    total_score = 0

    # iterate through each card in the hand
    # no iterations will occur if hand is an empty list
    for card in hand:
        # assess the value of the current card
        # if card is empty string, then there is no card so value is zero
        card_value = get_value_for_card(card) if card != '' else 0
        
        # the value of the card will only be 1 if it is an ace
        have_ace = True if card_value == 1 else have_ace
            
        #increment the total score of the hand for each card 
        total_score += card_value

        # assumption: 
        # if the number of cards were infinate, 
        # then I would want to check that total score is <= 21 here
        # because the maximum possible number of cards in a legitimate hand is 11
        # I will allow the performance hit (4-ace, 4-2, 3-3)

    # if we have an ace and using the upper score won't go over 21
    if have_ace and 21-total_score >= 10:
        # then add 10 to the score which includes 1 from an ace
        total_score += 10

    return total_score if total_score <= 21 else 0


#file is being run directly from command line
if __name__ == "__main__":
    for line in sys.stdin:
        # assume user will input comma separated list of elements with no quotes or brackets
        # assume user will type a semicolon then expected score

        # strip white space character from end ('\n')
        line = line.strip()

        # splitting the input line into:
        #       a comma separated list of cards
        #       an expected result
        cards, expected_score = line.split(';')
        
        #converting the expected result to an integer
        expected_score = int(expected_score)

        # greate a list from comma separated elements input from the user
        list_of_cards = cards.split(',')



    
        #test output to help visualize input and output
        print(list_of_cards, end=" => ")
        
        #calculate actual score
        actual_score = calculate_blackjack_hand(list_of_cards)
        
        print(actual_score)

        # I would normally complete this part with a testing framework using assertions
        # , but modifying this to work with hackerrank
        result = "pass" if actual_score == expected_score else "Fail: expected {}".format(expected_score)
        print(result)

        # this assertion would trigger hackerrank to fail and stop running the tests
        # Normally, it would be ideal to use a test framework to handle this assertion
        assert actual_score == expected_score





    # list_of_cards = ['ACE', 'ACE', 'JACK', 'QUEEN']
    # expected_score = 0
    # print(list_of_cards, end=" => ")
    # actual_score = calculate_blackjack_hand(list_of_cards)
    # print(actual_score)

    # result = "pass" if actual_score == expected_score else "Fail: expected {}".format(expected_score)
    # print(result)
    # for line in sys.stdin:
    # input = line.split(',')
    # print(input)
    # print(calculate_blackjack_hand(input))