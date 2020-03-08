import unittest
from badgeViolations import invalidBadgeLog

class badgeViolationsTests(unittest.TestCase):
    def test_badgeViolations_Example_One(self):
        input = [
            ["Martha",   "exit"],
            ["Paul",     "enter"],
            ["Martha",   "enter"],
            ["Martha",   "exit"],
            ["Jennifer", "enter"],
            ["Paul",     "enter"],
            ["Curtis",   "exit"],
            ["Curtis",   "enter"],
            ["Paul",     "exit"],
            ["Martha",   "enter"],
            ["Martha",   "exit"],
            ["Jennifer", "exit"],
            ["Paul",     "enter"],
            ["Paul",     "enter"],
            ["Martha",   "exit"],
        ]

        expected = [["Curtis", "Paul"], ["Martha", "Curtis"]]

        actual = invalidBadgeLog(input)

        self.assertCountEqual(expected[0], actual[0], "The invalid Entry logs don't match")
        self.assertCountEqual(expected[1], actual[1], "The invalid Exit logs don't match")

    def test_badgeViolations_Example_Two(self):
        input = [
            ["Paul", "enter"],
            ["Paul", "enter"],
            ["Paul", "exit"],
        ]

        expected = [["Paul"], []]

        actual = invalidBadgeLog(input)

        self.assertEqual(expected, actual)
    
    def test_badgeViolations_Example_Three(self):
        input = [
            ["Paul", "enter"],
            ["Paul", "exit"],
            ["Paul", "exit"],
        ]

        expected = [[], ["Paul"]]

        actual = invalidBadgeLog(input)

        self.assertEqual(expected, actual)

    def test_badgeViolations_Example_Four(self):
        input = [
            ["Paul", "exit"],
            ["Paul", "enter"],
            ["Martha", "enter"],
            ["Martha", "exit"],
        ]

        expected = [["Paul"], ["Paul"]]

        actual = invalidBadgeLog(input)

        self.assertEqual(expected, actual)

    def test_badgeViolations_Example_Five(self):
        input = [
            ["Paul", "enter"],
            ["Paul", "exit"],
        ]

        expected = [[], []]

        actual = invalidBadgeLog(input)

        self.assertEqual(expected, actual)

