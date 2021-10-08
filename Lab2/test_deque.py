import unittest
from main import Node, Deque 
from collections import deque

class DequeueTest(unittest.TestCase):
    def test_add_head(self):
        test_deque = Deque()
        test_deque.add_head(5)
        test_deque.add_head(10)
        test_deque.add_head(20)
        test_deque.add_head(-13)
        test_deque.add_head(7)

        test_deque_list = test_deque.deque_to_list()

        right_deque = deque()
        right_deque.appendleft(5)
        right_deque.appendleft(10)
        right_deque.appendleft(20)
        right_deque.appendleft(-13)
        right_deque.appendleft(7)

        right_deque_list = list(right_deque)

        self.assertEqual(test_deque_list, right_deque_list)

    def test_add_tail(self):
        test_deque = Deque()
        test_deque.add_tail(5)
        test_deque.add_tail(10)
        test_deque.add_tail(20)
        test_deque.add_tail(-13)
        test_deque.add_tail(7)

        test_deque_list = test_deque.deque_to_list()

        right_deque = deque()
        right_deque.append(5)
        right_deque.append(10)
        right_deque.append(20)
        right_deque.append(-13)
        right_deque.append(7)

        right_deque_list = list(right_deque)

        self.assertEqual(test_deque_list, right_deque_list)

    def test_delete_head(self):
        test_deque = Deque()
        test_deque.add_head(5)
        test_deque.add_head(10)
        test_deque.add_head(20)
        test_deque.delete_head()
        test_deque.delete_head()

        test_deque_list = test_deque.deque_to_list()

        right_deque = deque()
        right_deque.appendleft(5)
        right_deque.appendleft(10)
        right_deque.appendleft(20)
        right_deque.popleft()
        right_deque.popleft()

        right_deque_list = list(right_deque)

        self.assertEqual(test_deque_list, right_deque_list)
    
    def test_delete_tail(self):
        test_deque = Deque()
        test_deque.add_tail(5)
        test_deque.add_tail(10)
        test_deque.add_tail(20)
        test_deque.delete_tail()
        test_deque.delete_tail()

        test_deque_list = test_deque.deque_to_list()

        right_deque = deque()
        right_deque.append(5)
        right_deque.append(10)
        right_deque.append(20)
        right_deque.pop()
        right_deque.pop()

        right_deque_list = list(right_deque)

        self.assertEqual(test_deque_list, right_deque_list)
    
    def test_find_by_id(self):
        test_deque = Deque()
        test_deque.add_head(5)
        test_deque.add_head(10)
        test_deque.add_head(20)
        test_deque.add_tail(-13)
        test_deque.add_tail(7)
        test_data = test_deque.find_by_id(2)

        right_deque = deque()
        right_deque.appendleft(5)
        right_deque.appendleft(10)
        right_deque.appendleft(20)
        right_deque.append(-13)
        right_deque.append(7)
        right_data = right_deque[2]

        self.assertEqual(test_data, right_data)

