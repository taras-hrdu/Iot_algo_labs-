import unittest
from main import banan

class BananTest(unittest.TestCase):
    def test_banana_1(self):
        test_banan = banan([3, 6, 7, 11], 8)

        right_banan = 4

        self.assertEqual(test_banan, right_banan)

    def test_banana_2(self):
        test_banan = banan([30, 11, 23, 4, 20], 5)

        right_banan = 30

        self.assertEqual(test_banan, right_banan)
    
    def test_banana_3(self):
        test_banan = banan([30, 11, 23, 4, 20], 4)

        right_banan = -1

        self.assertEqual(test_banan, right_banan)
    
    def test_banana_4(self):
        test_banan = banan([0, 11, 23, 4, 20], 5)

        right_banan = -1

        self.assertEqual(test_banan, right_banan)
    
    def test_banana_5(self):
        test_banan = banan([-1, 11, 23, 4, 20], 5)

        right_banan = -1

        self.assertEqual(test_banan, right_banan)
    
    def test_banana_6(self):
        test_banan = banan([], 1)

        right_banan = -1

        self.assertEqual(test_banan, right_banan)