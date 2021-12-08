import unittest
from main import kmp, read_data


class TestKnuthMorrisPratt(unittest.TestCase):
    
    def test_kmp(self):
        kmp_data = read_data('kmp.in')
        self.assertEqual([0,7], kmp(*kmp_data))
