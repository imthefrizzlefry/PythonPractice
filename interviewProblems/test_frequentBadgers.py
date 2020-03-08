import unittest
from frequentBadgers import frequentBadgers

class frequentBadgersTests(unittest.TestCase):
    def test_frequentBadgers_Example_One(self):
        input = [
            ["Paul",     1355],
            ["Jennifer", 1910],
            ["John",      830],
            ["Paul",     1315],
            ["John",     1615],
            ["John",     1640],
            ["John",      835],
            ["Paul",     1405],
            ["John",      855],
            ["John",      930],
            ["John",      915],
            ["John",      730],
            ["Jennifer", 1335],
            ["Jennifer",  730],
            ["John",     1630],
            ["John",     2215],
            ["John",     2230],
            ["Paul",     1225],
        ]
        
        expectedKeys = ['John', 'Paul']
        expectedEntries_John = [830, 835, 855, 915, 930]
        expectedEntries_Paul = [1315, 1355, 1405]

        actual = frequentBadgers(input)

        self.assertCountEqual(expectedKeys, actual.keys())
        #self.assertCountEqual(expectedEntries_John, actual['John'])
        #self.assertCountEqual(expectedEntries_Paul, actual['Paul'])