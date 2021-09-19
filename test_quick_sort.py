import unittest
from main import SortOrder, partition

array = [11, 10, -9, 13, 99, 88, -1]
sorted_array_asc = [1,2,3,4,5,6,7]
sorted_array_desc = [7,6,5,4,3,2,1]

class TestQuickSort(unittest.TestCase):
    def test_inputArray(self):
        partition(array, SortOrder.ASC)
        self.assertEqual(array, sorted(array))

    def test_SortAscArrayForAsc(self):
        partition(sorted_array_asc, SortOrder.ASC)
        self.assertEqual(sorted_array_asc, sorted(sorted_array_asc))
    
    def test_SortDescArrayForDesc(self):
        partition(sorted_array_desc, SortOrder.DESC)
        self.assertEqual(sorted_array_desc, sorted(sorted_array_asc, reverse = True))

    def test_SortDescArrayForAsc(self):
        partition(sorted_array_desc, SortOrder.ASC)
        self.assertEqual(sorted_array_desc, sorted_array_asc)
    
    def test_SortAscArrayForDesc(self):
        sorted_array_asc4 = [1,2,3,4,5,6,7,8]
        sorted_array_desc4 = [8,7,6,5,4,3,2,1]
        partition(sorted_array_asc4, SortOrder.DESC)
        self.assertEqual(sorted_array_asc4, sorted_array_desc4)