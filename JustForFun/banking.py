

def calcSteppedInterestRate(balance, lowerRate=.0617, upperRate=.001, divider=500):
    '''Returns the annual interest on an account that charges different interest rates on balances above a divider'''
    if balance > divider:
        return (divider * lowerRate) + ((balance - divider) * upperRate)
    else:
        return balance * lowerRate

if __name__ == '__main__':
    annualDeposit = 100
    balance = 100
    print(balance)
    for age in range(2,18):
        interest = calcSteppedInterestRate(balance) 
        balance += interest
        print('the Effective Interest Rate will be {0:.3f}, and new balance is {1:.2f}'.format(interest/balance, balance))
        balance += annualDeposit
        print('new deposit of {0} bring account to {1:.2f}'.format(annualDeposit, balance))
