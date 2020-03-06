import unittest
import jumpingOnClouds

class jumpingOnCloudsTest(unittest.TestCase):
    def test_hackerRankExample(self):
        inputArray = [0,0,0,0,1,0]

        expectedJumps = 3

        self.assertEqual(expectedJumps, jumpingOnClouds.jumpingOnClouds(inputArray))
    def test_hackerRankTestCase0(self):
        inputArray = [0,0,1,0,0,1,0]

        expectedJumps = 4

        self.assertEqual(expectedJumps, jumpingOnClouds.jumpingOnClouds(inputArray))
    def test_hackerRankTestCase1(self):
        inputArray = [0,0,0,1,0,0]

        expectedJumps = 3

        self.assertEqual(expectedJumps, jumpingOnClouds.jumpingOnClouds(inputArray))