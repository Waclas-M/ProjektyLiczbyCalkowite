from Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie import Two_to_ten
import unittest

class Test(unittest.TestCase):
    def test_Two_to_ten(self):
        self.assertEqual(Two_to_ten(101011), 43,)
        self.assertEqual(Two_to_ten(101011111), 351,)
        self.assertEqual(Two_to_ten(10001000110010), 8754,)

