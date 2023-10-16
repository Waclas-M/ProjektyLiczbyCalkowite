import unittest
import Algorithm_Fibonacci
import Algorithm_fibonacci_recursion

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(Algorithm_Fibonacci.fibonacci(4),3)
        self.assertEqual(Algorithm_fibonacci_recursion.fibonacci_recursion(4),3)
