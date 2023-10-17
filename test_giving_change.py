import unittest
from algortihm_giving_change_Greedy import greedy_change

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greedy_change(2240),"""500 X 0
200 X 0
100 X 0
50 X 0
20 X 0
10 X 1""")
