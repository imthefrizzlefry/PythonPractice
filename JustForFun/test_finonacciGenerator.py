import unittest
import fibonacciGenerator

class fibonacciGeneratorTests(unittest.TestCase):
    def test_returns_First_NumberInSequence(self):
        expectedResult = 1        
        self.assertEqual(expectedResult, fibonacciGenerator.fibonacci_gen().__next__())

    def test_return_ThirtyFirst_NumberInSequence(self):
        inputIteration = 30
        expectedResult = 1346269
        fib = fibonacciGenerator.fibonacci_gen()
        for _ in range(inputIteration):
            fib.__next__()

        self.assertEqual(expectedResult, fib.__next__())
        
    def test_return_Third_NumberInSequence(self):
        inputIteration = 3
        expectedResult = 3
        fib = fibonacciGenerator.fibonacci_gen()
        for _ in range(inputIteration):
            next(fib)

        self.assertEqual(expectedResult, fib.__next__())

