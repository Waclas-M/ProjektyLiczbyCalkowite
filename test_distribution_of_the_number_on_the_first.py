import unittest
from distribution_of_the_number_on_the_first import distribution
from My_own_distribution_number import a

class Test( unittest.TestCase):

    def test(self):
        self.assertEqual(a(24),[2,2,2,3])
        self.assertEqual(a(144),[2, 2, 2, 2, 3, 3])
        self.assertEqual(a(32),[2, 2, 2, 2, 2])
        self.assertEqual(a(15),[3, 5])
        self.assertEqual(distribution(24),[2,2,2,3])
        self.assertEqual(distribution(144),[2, 2, 2, 2, 3, 3])
        self.assertEqual(distribution(32),[2, 2, 2, 2, 2])
        self.assertEqual(distribution(15),[3, 5])


