#!/usr/bin/env python3

""" """
import math


class Heap(object):
    """
    Max heap: A[Parent(i)] > A [i].
    Used in heap-sort max-heap and in priority queue: min-heap
    """

    def __init__(self, arr):
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
        Set self.arr to heapified state. From element with index. Time: O(ln(n))
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

    def build_heap(self):
        """ Build heap in self.arr. Time: O(n). """

        for ind in reversed(range(math.floor(self.heap_size / 2))):
            self._max_heapify(ind)

    def sort(self):
        """ Sort heap in self.arr. Time: O(n*ln(n)). """
        self.build_heap()
        for ind in reversed(range(1, self.heap_size)):
            self.arr[0], self.arr[ind] = self.arr[ind], self.arr[0]
            self.heap_size -= 1
            self._max_heapify(0)


import unittest


class TestHeap(unittest.TestCase):
    def test_jumps(self):
        """ TestHeap: basic index operations. """
        heap = Heap([])
        self.assertEqual(heap._parent(10), 4)
        self.assertEqual(heap._left(10), 21)
        self.assertEqual(heap._right(10), 22)

    def test_max_heapify(self):
        """ TestHeap: maintaining of basic heap feature by heapify. """
        heap = Heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1])
        expected_arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        heap._max_heapify(1)  # heapify with element 4
        self.assertEqual(heap.arr, expected_arr)

    def test_create_heap(self):
        """ TestHeap: create max-heap from array. """
        heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        expected_arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        heap.build_heap()
        self.assertEqual(heap.arr, expected_arr)

    def test_heapsort(self):
        """ TestHeap: sort array by heapsort. """
        heap = Heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        expected_arr = [1, 2, 3, 4, 7, 8, 9, 10, 14, 16]
        heap.sort()
        self.assertEqual(heap.arr, expected_arr)
