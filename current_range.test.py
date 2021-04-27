#Test_current_ranges

import unittest
import identify_range_and_count_implementation as ir

class CurrentRangeTest(unittest.TestCase):
    def test_range_and_count(self):
        ir.identify_range_and_count([3,5,3,10,15,16,17])
  

if __name__ == "__main__":
  unittest.main()
