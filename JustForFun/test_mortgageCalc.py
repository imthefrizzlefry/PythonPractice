import unittest
import datetime
import mortgageCalc

class mortgageCalcTests(unittest.TestCase):
    def test_calculatesMyMortgageCorrectly(self):
        inputPrincipal = 522000
        inputinterest = 0.03875
        inputPayments = 360
        expectedResult = 2454.64

        self.assertEqual(expectedResult, float('{0:.2f}'.format(mortgageCalc.CalcMonthlyPayment(inputPrincipal, inputinterest, inputPayments))))

    def test_calculatesEnerbankCorrectly(self):
        inputPrincipal = 15106
        inputinterest = 0.0699
        inputPayments = 84
        expectedResult = 227.92

        self.assertEqual(expectedResult, float('{0:.2f}'.format(mortgageCalc.CalcMonthlyPayment(inputPrincipal, inputinterest, inputPayments))))

    def test_calculatesHondaLoanCorrectly(self):
        inputPrincipal = 32063.65
        inputinterest = 0.0190
        inputPayments = 60
        expectedResult = 560.60

        self.assertEqual(expectedResult, float('{0:.2f}'.format(mortgageCalc.CalcMonthlyPayment(inputPrincipal, inputinterest, inputPayments))))

        def test_InterestRateIsZero(self):
            inputPrincipal = 10000.0
            inputinterest = 0.0
            inputPayments = 15
            expectedResult = 666.67

            self.assertEqual(expectedResult, float('{0:.2f}'.format(mortgageCalc.CalcMonthlyPayment(inputPrincipal, inputinterest, inputPayments))))

    def test_calcPaymentsCompleteSameYear(self):
        inputOriginationDate = datetime.date(2018, 5, 10)
        inputEndDate = datetime.date(2018, 6, 10)
        expectedNumberOfPayments = 1

        self.assertEqual(expectedNumberOfPayments, mortgageCalc.completedPayments(inputOriginationDate,inputEndDate))

    def test_calcPaymentsCompleteNextYear(self):
        inputOriginationDate = datetime.date(2018, 5, 10)
        inputEndDate = datetime.date(2019, 6, 10)
        expectedNumberOfPayments = 13

        self.assertEqual(expectedNumberOfPayments, mortgageCalc.completedPayments(inputOriginationDate,inputEndDate))

    def test_maturityDateIsCalculatedCorrectly(self):
        inputOriginationDate = datetime.date(2018, 5, 10)
        inputNumberOfPayments = 5
        expectedMaturityDate = datetime.date(2018, 10, 10)

        self.assertEqual(expectedMaturityDate, mortgageCalc.LoanMaturity(inputNumberOfPayments, inputOriginationDate))

    def test_maturityDateHandlesYearRollover(self):
        inputOriginationDate = datetime.date(2018, 10, 10)
        inputNumberOfPayments = 5
        expectedMaturityDate = datetime.date(2019, 3, 10)

        self.assertEqual(expectedMaturityDate, mortgageCalc.LoanMaturity(inputNumberOfPayments, inputOriginationDate))

    def test_maturityDateWorksForMultiYearLoans(self):
        inputOriginationDate = datetime.date(2018, 5, 10)
        inputNumberOfPayments = 60
        expectedMaturityDate = datetime.date(2023, 5, 10)

        self.assertEqual(expectedMaturityDate, mortgageCalc.LoanMaturity(inputNumberOfPayments, inputOriginationDate))

    def test_calculateRemainingBalanceSinglePayment(self):
        inputPrincipal = 100
        inputInterest = .12
        inputPaymentAmount = 10
        inputNumberOfPayments = 1
        expectedRemainingPrincipal = 91

        self.assertEqual(expectedRemainingPrincipal, mortgageCalc.CalcRemainingPrincipal(inputPrincipal, inputInterest, inputPaymentAmount, inputNumberOfPayments))
        
    def test_calculateRemainingBalanceSinglePaymentZeroInterest(self):
        inputPrincipal = 100
        inputInterest = 0.0
        inputPaymentAmount = 10
        inputNumberOfPayments = 1
        expectedRemainingPrincipal = 90

        self.assertEqual(expectedRemainingPrincipal, mortgageCalc.CalcRemainingPrincipal(inputPrincipal, inputInterest, inputPaymentAmount, inputNumberOfPayments))