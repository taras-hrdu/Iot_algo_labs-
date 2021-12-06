import unittest

from main import WChain


class LongestStrChainTest(unittest.TestCase):
    def test_wchain(self):
        data = WChain.read_file('wchain.in')
        first_attempt = WChain
        self.assertEqual(6, first_attempt.longestStrChain(data))


if __name__ == '__main__':
    unittest.main()