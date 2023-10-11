import Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie
import unittest

class Test(unittest.TestCase):
    def test_Two_to_ten(self):
        self.assertEqual(Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie.Two_to_ten(101011), 43,)
        self.assertEqual(Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie.Two_to_ten(101011111), 351,)
        self.assertEqual(Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie.Two_to_ten(10001000110010), 8754,)
    def test_Ten_to_two(self):
        self.assertEqual(Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie.Ten_to_two(43), '101011',)
        self.assertEqual(Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie.Ten_to_two(351), '101011111',)
        self.assertEqual(Zamiana_z_systemu_dziesietnego_na_dwojkowy_i_odwrotnie.Ten_to_two(8754), '10001000110010',)

if __name__ == '__main__':
    unittest.main()

