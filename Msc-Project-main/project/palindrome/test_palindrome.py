# Description: this file contain manual test cases for palindrome function
import unittest
import palindrome


class TestPalindrome(unittest.TestCase):

    def test_palindrome(self):  # test the word is palindrome
        Input = "racecar"  # input
        expectedOutput = True  # expected output
        sut = palindrome.is_palindrome(Input)  # software under test
        actualOutput = sut  # result

        self.assertEqual(expectedOutput, actualOutput)  # compare actual and expected results

    def test_palindrome_with_mixed_cases(self):  # test the word is palindrome with mixed cases
        Input = "Racecar"  # input
        expectedOutput = False  # expected output
        sut = palindrome.is_palindrome(Input)  # software under test
        actualOutput = sut  # result

        self.assertEqual(expectedOutput, actualOutput)

    def test_palindrome_with_punctuation(self):  # test the word is palindrome with punctuation
        Input = "Racecar!"  # input
        expectedOutput = False  # expected output
        sut = palindrome.is_palindrome(Input)  # software under test
        actualOutput = sut  # result

        self.assertEqual(expectedOutput, actualOutput)

    def test_palindrome_with_spaces(self):  # test the word is palindrome with spaces
        Input = "race car"  # input
        expectedOutput = False  # expected output
        sut = palindrome.is_palindrome(Input)  # software under test
        actualOutput = sut  # result

        self.assertEqual(expectedOutput, actualOutput)


if __name__ == '__main__':
    unittest.main()
