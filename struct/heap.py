#!/usr/bin/env python3

""" """
import math


class Heap(object):
    """
    Max heap: A[Parent(i)] > A [i].
    Used in heap-sort max-heap and in priority queue: min-heap
    """

    def set_arr(self, arr):
        self.arr = arr
        self.heap_size = len(arr)

    def _parent(self, i):
        """
        :param i:
        :return:
        """
        return math.floor((i + 1) / 2) - 1

    def _left(self, i):
        """
        :param i:
        :return:
        """
        return (i + 1) * 2 - 1

    def _right(self, i):
        """
        :param i:
        :return:
        """
        return 2 * (i + 1)

    def _max_heapify(self, index):
        """
        Set self.arr to heapified state. From element with index.
        """
        # check left side
        left = self._left(index)
        if left < self.heap_size and self.arr[left] > self.arr[index]:
            largest = left
        else:
            largest = index
        # check right side
        right = self._right(index)
        if right < self.heap_size and self.arr[right] > self.arr[largest]:
            largest = right
        # check if we need to swap elements
        if index != largest:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[
                index]
            self._max_heapify(largest)


import unittest


class TestHeap(unittest.TestCase):
    def test_jumps(self):
        """ TestHeap: basic index operations. """
        heap = Heap()
        self.assertEqual(heap._parent(10), 4)
        self.assertEqual(heap._left(10), 21)
        self.assertEqual(heap._right(10), 22)

    def test_max_heapify(self):
        """ TestHeap: maintaining of basic heap feature by heapify. """
        heap = Heap()
        heap.set_arr([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        expected_arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        heap._max_heapify(1)  # heapify with element 4
        self.assertEqual(heap.arr, expected_arr)
