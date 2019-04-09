import unittest
from user04 import *
from datetime import datetime




class US04_Function(unittest.TestCase):
    # test porject03.py

    def test_Validation_check04(self):
        self.assertTrue(us04('8JUL1994','14NOV2001','Chris Smith','Julie Swift'))
        self.assertEqual(True,us04('8JUL1994','14NOV2001','Chris Smith','Julie Swift'))
        self.assertNotEqual(False,us04('8JUL1994','14NOV2001','Chris Smith','Julie Swift'))




if __name__ == '__main__':
    unittest.main(verbosity=1)
