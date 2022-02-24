import sys
import unittest

class Run_Unit_Tests(unittest.TestCase):

    def test_is_valid_word(self):
        from main import is_valid_word

        self.assertFalse(is_valid_word("aaabb"))
        self.assertFalse(is_valid_word("aabba"))
        self.assertFalse(is_valid_word("adaba"))
        self.assertTrue(is_valid_word("aabbc"))
        self.assertTrue(is_valid_word("abcba"))

    def test_is_lewd_word(self):
        from main import is_lewd_word

        self.assertFalse(is_lewd_word("aabed"))
        self.assertFalse(is_lewd_word("porng"))

        self.assertTrue(is_lewd_word("bussy"))
        self.assertTrue(is_lewd_word("cussy"))
        self.assertTrue(is_lewd_word("dicks"))
        self.assertTrue(is_lewd_word("prick"))
        self.assertTrue(is_lewd_word("grool"))
        self.assertTrue(is_lewd_word("twink"))
        self.assertTrue(is_lewd_word("bonch"))
        self.assertTrue(is_lewd_word("boobs"))
        self.assertTrue(is_lewd_word("quims"))
        self.assertTrue(is_lewd_word("booty"))
        self.assertTrue(is_lewd_word("frots"))
        self.assertTrue(is_lewd_word("skeet"))
        self.assertTrue(is_lewd_word("milfs"))
        self.assertTrue(is_lewd_word("daddy"))
        self.assertTrue(is_lewd_word("ponut"))
        self.assertTrue(is_lewd_word("cooch"))
        self.assertTrue(is_lewd_word("vulva"))
        self.assertTrue(is_lewd_word("balls"))
        self.assertTrue(is_lewd_word("shart"))

if __name__ == "__main__":
    unittest.main()
