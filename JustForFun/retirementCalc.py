
class RetirementCalc:

    def __init__(self, age=18, income=0, balance=0, contributionRate=0, growthRate=0):
        self._age = age
        self._income = income
        self._balance = balance
        self._contributionRate = contributionRate
        self._growthRate = growthRate

    def calcRetirementContributionAmount(self, income = 0): 
        if income == 0:
            return self._income * self._contributionRate
        else:
            return income * self._contributionRate

    def calcGrowthAmount(self, balance=0):
        if balance == 0:
            return self._balance * self._growthRate
        else:
            return balance * self._growthRate

    def calcProjectedRetirementAge(self, goalAmount = 2000000, expectedGWI =.03):
        projectedIncome = self._income
        projectedAge = self._age
        retirementBalance = self._balance

        while(retirementBalance < goalAmount):      
            retirementBalance += self.calcGrowthAmount(retirementBalance)
            retirementBalance += self.calcRetirementContributionAmount(projectedIncome)
            projectedAge += 1

        if projectedAge < 65:
            retirementStatus = "You are on track for an early retirement"
        elif projectedAge == 65:
            retirementStatus = "You are on track to retire on time"
        elif projectedAge < 70:
            retirementStatus = "You are on track to retire a little late"
        elif projectedAge < 84:
            retirementStatus = "You are on track to retire very late"
        else:
            retirementStatus = "You are on track to die while working"

        return [projectedAge, round(retirementBalance, 2), retirementStatus]

    def calcContributionAmountByRetirementAge(self, age = 65):
        projectedAge = self.calcProjectedRetirementAge()[0]
        originalContributionRate = self._contributionRate

        # error on the side of early retirement
        while projectedAge < age:
            # decrease contribution
            self._contributionRate -= .01
            currentStat = self.calcProjectedRetirementAge()
            projectedAge = currentStat[0]
        
        while projectedAge > age:
            self._contributionRate += .01
            currentStat = self.calcProjectedRetirementAge()
            projectedAge = currentStat[0]

        return {
            "contributionAmount": self.calcRetirementContributionAmount(), 
            "contributionRate": self._contributionRate, 
            "retirementAge": currentStat[0],
            "retirementBalance": currentStat[1],
            "retirementStatus": currentStat[2]
        }
            # decrease contribution

def calcCompoundInterest(currentValue = 0, contributions = 0, numYears = 30, annualReturn = .06):
    if numYears > 1 :
        previousValue = calcCompoundInterest(currentValue, contributions, numYears-1, annualReturn)
    else:
        previousValue = currentValue

    return (previousValue + contributions) * (1 + annualReturn)

if __name__ == '__main__':
    # do by default
    #x = RetirementCalc(age=35, income= 200181.18, balance= 123435.12, contributionRate=0.1421, growthRate=0.06)
    #print(x.calcProjectedRetirementAge())

    #print(x.calcContributionAmountByRetirementAge())

    print('${0:,.2f}'.format(calcCompoundInterest(currentValue=120000, contributions=11000, numYears=30, annualReturn=0.06)))