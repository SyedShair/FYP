import unittest
import fault_injection_palindrome


class TestPalindrome(unittest.TestCase):
    # generate four unittest methods to check that given string is a palindrome or not
    # 1. test_palindrome
    # 2. test_palindrome_with_mixed_case
    # 3. test_palindrome_with_punctuation
    # 4. test_palindrome_with_mixed_case_and_punctuation

    def test_palindrome(self):
        self.assertTrue(fault_injection_palindrome.is_palindrome("madam"))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(fault_injection_palindrome.is_palindrome("Madam"))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(fault_injection_palindrome.is_palindrome("madam!"))

    def test_palindrome_with_mixed_case_and_punctuation(self):
        self.assertTrue(fault_injection_palindrome.is_palindrome("Madam!"))


if __name__ == '__main__':
    unittest.main()
