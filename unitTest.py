import unittest
from  calenderPrinter import calender_printer
import os

# define the unit tests
class my_unit_tests(unittest.TestCase):

        # tests if the days printed are correct
    def test_days(self):
        self.assertEqual(calender_printer(31, 3), ["S", "M" , "T", "W", "T", "F", "S"])

    # run the tests
if __name__ == "__main__":
    unittest.main()