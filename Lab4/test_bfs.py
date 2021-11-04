import unittest
from main import *


class TestGraph(unittest.TestCase): 
    
    def test_graph(self):
        graph = {
        '0': ['1', '2'],
        '1': ['3', '4'],
        '2': ['5', '6'],
        '3': ['7', '8'],
        '4': ['9', '10']
        }
        
        expected_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        list = bfs(graph, '0')

        self.assertEqual(expected_list, list)


if __name__ == '__main__':
    
    unittest.main()
    