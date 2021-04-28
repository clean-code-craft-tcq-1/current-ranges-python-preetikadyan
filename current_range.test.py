#Test_current_ranges

import unittest
import identify_range_and_count_implementation as ir

class CurrentRangeTest(unittest.TestCase):
    def passing_test_range_and_count(self):
        ir.identify_range_and_count([3, 3, 5, 4, 10, 11, 12])
        
    def failing_test_range_and_count(self):    
        ir.identify_range_and_count(['a'])

if __name__ == "__main__":
  unittest.main()
