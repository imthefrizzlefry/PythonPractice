import unittest
from firstMissingPositiveInt import firstMissingPositiveInt

class firstMissingPositiveIntTests(unittest.TestCase):
    def test_firstMissingPositiveInt_ExampleOne(self):
        a = [3,4,-1,1]
        expectedResult = 2
        
        actualResult = firstMissingPositiveInt(a)
        
        self.assertEqual(expectedResult, actualResult)
    
    def test_firstMissingPositiveInt_ExampleTwo(self):
        a = [1, 2, 0]
        expectedResult = 3
        
        actualResult = firstMissingPositiveInt(a)
        
        self.assertEqual(expectedResult, actualResult)

    def test_firstMissingPositiveInt_DuplicateValues(self):
        a=[1,1,1,1,2,4,0]
        expectedResult = 3

        actualResult = firstMissingPositiveInt(a)
    
        self.assertEqual(expectedResult, actualResult)