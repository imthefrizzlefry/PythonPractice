#Example Google Interview Question: A store that only sells pens is having the following sale:
# if you buy more than 5 pens at 10 rupees each, you will get a 10% discount on your order.
# 
# Write a program in Python to find the total bill when the user enters the number of pens with the keyboard.

def processPurchase(numPens, basePrice=10):
    
    if numPens > 5:
        actualPrice= basePrice*.9
     
    else:
        actualPrice = basePrice

    print('Your Bill for the pens is {0}'.format(numPens*actualPrice))

if __name__ == '__main__':
    processPurchase(int(input('How Many Pens would you like to purchase? ')))