import unittest
import rotateArrayLeft

class RotatingArrayLeftTests(unittest.TestCase):
    def test_hackerRankTestCase0(self):
        inputArray = [1,2,3,4,5]
        numberOfRotations = 4

        expectedArray = [5,1,2,3,4]

        self.assertEqual(expectedArray, rotateArrayLeft.rotLeft(inputArray, numberOfRotations))
    def test_hackerRankTestCase1(self):
        inputArray = [41,73,89,7,10,1,59,58,84,77,77,97,58,1,86,58,26,10,86,51]
        numberOfRotations = 10

        expectedArray = [77,97,58,1,86,58,26,10,86,51,41,73,89,7,10,1,59,58,84,77]

        self.assertEqual(expectedArray, rotateArrayLeft.rotLeft(inputArray, numberOfRotations))
    def test_hackerRankTestCase2(self):
        inputArray = [33,47,70,37,8,53,13,93,71,72,51,100,60,87,97]
        numberOfRotations = 13

        expectedArray = [87,97,33,47,70,37,8,53,13,93,71,72,51,100,60]

        self.assertEqual(expectedArray, rotateArrayLeft.rotLeft(inputArray, numberOfRotations))