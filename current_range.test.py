#Test_current_ranges

import unittest
import identify_range_and_count_implementation as ir

class CurrentRangeTest(unittest.TestCase):
    def passing_test_range_and_count(self):
        self.assertTrue(ir.identify_range_and_count([]) == 0)
        
   

if __name__ == "__main__":
  unittest.main()
