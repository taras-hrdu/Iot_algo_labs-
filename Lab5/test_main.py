import unittest
from main import Graph


class TestMain(unittest.TestCase):

    def test_ford(self):
        graph = [
                [0, 20, 10, 0, 0, 10],
                [0, 0, 0, 30, 0, 0],
                [0, 0, 0, 0, 5, 0],
                [0, 0, 0, 0, 0, 20],
                [0, 0, 0, 0, 0, 10],
                [0, 0, 0, 0, 0, 0]
                ]
        g = Graph(graph, source=0, sink=5)

        expected = 35
        self.assertEqual(g.ford_fulkerson(), expected)
