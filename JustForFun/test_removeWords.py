import unittest

from removeWords import removeWordFromSentence

class removeWordTests(unittest.TestCase):
# removeWordFromSentence("This is a test.", "test");
# will return "This is a"
    def test_removeWorkWithTrailingPunctuation(self):
        inputSentence = "This is a test."
        inputWord = "test"
        expectedResult = "This is a"

        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))

    # removeWordFromSentence("This test is good.", "test");
    # will return "This is good.""
    def test_removeWordFromMiddleOfSentenceIncludingOneSpace(self):
        inputSentence = "This test is good."
        inputWord = "test"
        expectedResult = "This is good."

        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))

    def test_RemovesNothingWhenTheWordToBeRemovedIsAnEmptyString(self):
        inputSentence = "This is a sample of a sentence."
        inputWord = ""
        expectedResult = "This is a sample of a sentence."

        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))

    def test_RemovesNothingWhenTheWordToBeRemovesIsNull(self):
        inputSentence = "This is a sample of a sentence."
        inputWord = None
        expectedResult = "This is a sample of a sentence."
        
        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))

    def test_RemovesTheLastWordInASentenceWhenThereIsNoPunctuation(self):
        inputSentence = "the test is to remove the last word"
        inputWord = "word"
        expectedResult = "the test is to remove the last"

        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))

    def test_RemovesWordBeforeCommaThatIsInTheMiddleOfTheSentence(self):
        inputSentence = "The sentence is more complex, than a simple idea."
        inputWord = "complex"
        expectedResult = "The sentence is more than a simple idea."

        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))

    def test_RemovesWordThatAppearsMultipleTimesInTheSameSentence(self):
        inputSentence = "The happy person was a happy poet."
        inputWord = "happy"
        expectedResult = "The person was a poet."

        self.assertEqual(expectedResult, removeWordFromSentence(inputSentence, inputWord))