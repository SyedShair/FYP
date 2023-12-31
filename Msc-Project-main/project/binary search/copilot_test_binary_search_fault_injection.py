# Description: This file contains the test cases for the binary_search function in binary_search_Fault_Injection.py.
# The test cases are the same as the ones in copilot_test_binary_search.py.
# The difference is that this file is used to test the binary_search function in binary_search_Fault_Injection.py.


import unittest
import binary_search_Fault_Injection


class TestAlgorithm(unittest.TestCase):

    # Add four test cases to test the binary_search function.
    # test case 1: the target is in the array.
    # test case 2: the target is not in the array.
    # test case 3: the target is the first element in the array.
    # test case 4: the target is the last element in the array.

    def test_binary_search(self):
        # test case 1: the target is in the array.
        self.assertEqual(binary_search_Fault_Injection.binary_search_algo([1, 2, 3, 4, 5], 3), 2)

    def test_binary_search_2(self):
        # test case 2: the target is not in the array.
        self.assertEqual(binary_search_Fault_Injection.binary_search_algo([1, 2, 3, 4, 5], 6), -1)

    def test_binary_search_3(self):
        # test case 3: the target is the first element in the array.
        self.assertEqual(binary_search_Fault_Injection.binary_search_algo([1, 2, 3, 4, 5], 1), 0)

    def test_binary_search_4(self):
        # test case 4: the target is the last element in the array.
        self.assertEqual(binary_search_Fault_Injection.binary_search_algo([1, 2, 3, 4, 5], 5), 4)


if __name__ == '__main__':

    unittest.main()
