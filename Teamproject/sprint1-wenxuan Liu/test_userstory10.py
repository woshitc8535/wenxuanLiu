import unittest
from user10 import *
from datetime import datetime


indi1 = {'I1': {'id': 'I1', 'name': 'Sam/Smith/', 'sex': 'M', 'BIRT': '9JAN1980', 'family': 'F1'}}
indi2 = {'I2': {'id': 'I2', 'name': 'Mike/Smith/', 'sex': 'M', 'BIRT': '7OCT1965', 'family': 'F2'}}
indi3 = {'I3': {'id': 'I3', 'name': 'Mary/Smith/', 'sex': 'F', 'BIRT': '13JUL1966', 'family': 'F1'}}
indi4 = {'I4': {'id': 'I4', 'name': 'Jordan/Smith/', 'sex': 'M', 'BIRT': '28SEP1939', 'family': 'F2'}}
indi5 = {'I5': {'id': 'I5', 'name': 'Alice/Smith/', 'sex': 'F', 'BIRT': '15JUN1943', 'DEAT': '7SEP2009','family': 'F2'}}
indi6 = {'I6': {'id': 'I6', 'name': 'Will/Smith/', 'sex': 'M', 'BIRT': '7OCT1963', 'DEAT': '11APR2002','family': 'F2'}}

class US10_Function(unittest.TestCase):
    # test porject03.py

    def test_Validation_check10(self):
        self.assertTrue(marrAfter14(indi1))
        self.assertEqual(True,marrAfter14(indi2))
        self.assertNotEqual(False,marrAfter14(indi3))



if __name__ == '__main__':
    unittest.main(verbosity=1)

