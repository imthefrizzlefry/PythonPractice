import unittest
import hourGlassSum

class hourGlassSumTests(unittest.TestCase):
    def test_hackerRankSampleTestCase0(self):
        inputArray = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]

        expectedMaxSum = 19

        self.assertEqual(expectedMaxSum, hourGlassSum.hourglassSum(inputArray))
    def test_hackerRankSampleTestCase1(self):
        inputArray = [[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,9,2,-4,-4,0],[0,0,0,-2,0,0],[0,0,-1,-2,-4,0]]

        expectedMaxSum = 13

        self.assertEqual(expectedMaxSum, hourGlassSum.hourglassSum(inputArray))
    def test_hackerRankSampleTestCase2(self):
        inputArray = [[-9,-9,-9,1,1,1],[0,-9,0,4,3,2],[-9,-9,-9,1,2,3],[0,0,8,6,6,0],[0,0,0,-2,0,0],[0,0,1,2,4,0]]

        expectedMaxSum = 28

        self.assertEqual(expectedMaxSum, hourGlassSum.hourglassSum(inputArray))
    def test_hackerRankSampleTestCase3(self):
        inputArray = [[-1,-1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]

        expectedMaxSum = -6

        self.assertEqual(expectedMaxSum, hourGlassSum.hourglassSum(inputArray))