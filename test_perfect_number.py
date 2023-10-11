import unittest
from perfect_number import perfect

class Test(unittest.TestCase):
    def test_perfect(self):
        self.assertEqual(perfect(28),'Liczba doskonala')
        self.assertEqual(perfect(6),'Liczba doskonala')
        self.assertEqual(perfect(496),'Liczba doskonala')
        self.assertEqual(perfect(8128),'Liczba doskonala')
        self.assertEqual(perfect(14),'Nie liczba doskonala')
        self.assertEqual(perfect(16),'Nie liczba doskonala')


if __name__ == '__main__':
    unittest.main()
