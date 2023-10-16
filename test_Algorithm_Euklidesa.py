import unittest
import Algorithm_Euklidesa
import Algorithm_Ekulidesa_recursion

class Test(unittest.TestCase):
    def test_Eukalides(self):
        self.assertEqual(Algorithm_Ekulidesa_recursion.NWD(150,240),30)
        self.assertEqual(Algorithm_Ekulidesa_recursion.NWD(24,36),12)
        self.assertEqual(Algorithm_Euklidesa.Euklides(150,240),30)
        self.assertEqual(Algorithm_Euklidesa.Euklides(24,36),12)
