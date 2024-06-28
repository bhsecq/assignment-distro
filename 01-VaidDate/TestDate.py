import unittest

from main import *


class TestStats(unittest.TestCase):
   def test_all(self):
    tests = ["1", "01", "01/07/2003", "1/7/2013", "01/7/2023", "1/07/1999", "01 07 2003", "1/7/3", "01072003//", "01/07/2003/", "01//2003", "01/07/", "January 7th, 2003", "one/07/2003", "13/7/2000", "5/40/2000", "5/2/-1", "5/2/1"]
    expected = [False, False, True, True, True, True, False, False, False, False, False, False,  False, False, False, False, False, False]
    
    for i in range(len(tests)):
      self.assertEqual(is_valid_date(tests[i]), expected[i], msg=f"Failed test.\nInput:'{tests[i]}'\nExpected output: {expected[i]}\nActual output: {is_valid_date(tests[i])}")
      print(f"success with input {tests[i]}")
    
if __name__ == '__main__':
    unittest.main()


