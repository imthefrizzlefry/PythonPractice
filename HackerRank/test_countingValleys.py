import unittest
import countingValleys

class countingValleysTests(unittest.TestCase):
    def test_exampleInput(self):
        inputSteps = 'UDDDUDUU'
        inputNumberSteps = 8

        expectedValleys = 1

        self.assertEqual(expectedValleys, countingValleys.countingValleys(inputNumberSteps,inputSteps))

    def test_HackerRankSampleTest2(self):
        inputSteps = 'DDUUDDUDUUUD'
        inputNumberSteps = 12

        expectedValleys = 2

        self.assertEqual(expectedValleys, countingValleys.countingValleys(inputNumberSteps,inputSteps))

    def test_myExampleTest(self):
        inputSteps = 'DDDDDUUDDUUDDUUDDUUUUU'
        inputNumberSteps = 12

        expectedValleys = 1

        self.assertEqual(expectedValleys, countingValleys.countingValleys(inputNumberSteps,inputSteps))
