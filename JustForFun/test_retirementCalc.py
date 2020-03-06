import unittest
import retirementCalc 

class retirementCalcTests(unittest.TestCase):
    def test_calcProjectedRetirementAge_PersonRetiresOnTime(self):
        # arrange inputs
        age=18
        income=42553.2
        balance=0
        contributionRate=1
        growthRate=0

        # arrange expectations
        expectedAge = 65
        expectedBalance = 2000000.4
        expectedStatus = "You are on track to retire on time"
        expectedResult = [expectedAge, expectedBalance, expectedStatus]

        # arrange object instantiation
        retiree = retirementCalc.RetirementCalc(age, income,balance,contributionRate,growthRate)
        
        # act - run calculation
        actualResult = retiree.calcProjectedRetirementAge()

        #assert expectations are correct
        self.assertEqual(expectedResult, actualResult)
