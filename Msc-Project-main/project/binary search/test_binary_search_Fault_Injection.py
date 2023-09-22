# Description: This file contains the test cases for the binary_search_Fault_Injection method


import unittest
import binary_search_Fault_Injection


class TestAlgorithm(unittest.TestCase):

    def test_binary_search(self):  # binary_search method for an item  found in the array
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # array
        target = 5  # target item
        expectedOutput = 4  # expected output
        sut = binary_search_Fault_Injection.binary_search_algo(array, target)  # software under test
        Output = sut  # actual output is equal to sut
        self.assertEqual(expectedOutput, Output)  # assert method

    def test_binary_search_itemNotFound(self):  # binary_search method for an item not in the array
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # array
        target = 11  # target item
        expectedOutput = -1  # expected output
        sut = binary_search_Fault_Injection.binary_search_algo(array, target)  # software under test
        Output = sut  # actual output is equal to sut
        self.assertEqual(expectedOutpu, Output)  # assert method

    def test_binary_search_negativeItem(self):  # binary_search method for a negative item
        array = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]  # array
        target = -5  # target item
        expectedOutput = 4  # expected output
        sut = binary_search_Fault_Injection.binary_search_algo(array, target)  # software under test
        Output = sut  # actual output is equal to sut
        self.assertEqual(expectedOutput, Output)  # assert method

    def test_binary_search_emptyArray(self):  # binary search method when string is empty
        array = []  # array
        target = 5  # target item
        expectedOutput = []  # expected output
        sut = binary_search_Fault_Injection.binary_search_algo(array, target)  # here is the software under test
        Output = sut  # actual output is equal to sut
        self.assertEqual(expectedOutput, Output)  # assert method


if __name__ == '__main__':
    unittest.main()
