import unittest
from Prime_Number import Prime

class Test(unittest.TestCase):

    def test_Prime(self):
        self.assertEqual(Prime(3),'liczba pierwsaza')
        self.assertEqual(Prime(5),'liczba pierwsaza')
        self.assertEqual(Prime(7),'liczba pierwsaza')
        self.assertEqual(Prime(8),'To nie liczba pierwsza')
        self.assertEqual(Prime(24),'To nie liczba pierwsza')

if __name__ == '__main__':
    unittest.main()
