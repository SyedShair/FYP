# Description: This file contains manual testcases for fizzbuzz function

import unittest
import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz(self):  # fizzbuzz function with input value 15
        Input = 15  # input
        expectedOutput = "FizzBuzz"  # expectedOutput
        sut = fizzbuzz.fiz_buz_func(Input)  # software under test
        output = sut  # result
        self.assertEqual(expectedOutput, output)  # compare the actual and expectedOutput

    def test_fizz(self):  # fizzbuzz function with input value 3
        Input = 3  # input
        expectedOutput = "Fizz"  # expectedOutput
        sut = fizzbuzz.fiz_buz_func(Input)  # software under test
        output = sut  # result
        self.assertEqual(expectedOutput, output)  # compare the actual and expectedOutput

    def test_buzz(self):  # fizzbuzz function with input value 5
        Input = 5  # input
        expectedOutput = "Buzz"  # expectedOutput
        sut = fizzbuzz.fiz_buz_func(Input)  # software under test
        output = sut  # result
        self.assertEqual(expectedOutput, output)  # compare the actual and expectedOutput

    def test_number(self):  # fizzbuzz function with input value 1
        Input = 1  # input
        expectedOutput = 1  # expectedOutput
        sut = fizzbuzz.fiz_buz_func(Input)  # software under test
        output = sut  # result
        self.assertEqual(expectedOutput, output)  # compare the actual and expectedOutput


if __name__ == '__main__':
    unittest.main()
