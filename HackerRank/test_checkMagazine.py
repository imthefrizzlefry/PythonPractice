import unittest
import checkMagazine

class checkMagazineTests(unittest.TestCase):
    def test_HackerRankTestCase0(self):
        inputMagazine = "give me one grand today night".split()
        inputNote = "give one grand today".split()

        expectedOutput = "Yes"

        self.assertEqual(expectedOutput, checkMagazine.checkMagazine(inputMagazine, inputNote))
    def test_HackerRankTestCase1(self):
        inputMagazine = "two times three is not four".split()
        inputNote = "two times two is four".split() # two occurs only once

        expectedOutput = "No"

        self.assertEqual(expectedOutput, checkMagazine.checkMagazine(inputMagazine, inputNote))
    def test_HackerRankTestCase2(self):
        inputMagazine = "ive got a lovely bunch of coconuts".split()
        inputNote = "ive got some coconuts".split() # missing word "some"

        expectedOutput = "No"

        self.assertEqual(expectedOutput, checkMagazine.checkMagazine(inputMagazine, inputNote))
    def test_StringOccursTwiceInMagazineAndNote(self):
        inputMagazine = "I got a lovely bunch of coconuts I love".split()
        inputNote = "I need a coconut for I".split() # missing word "some"

        expectedOutput = "No"

        self.assertEqual(expectedOutput, checkMagazine.checkMagazine(inputMagazine, inputNote))