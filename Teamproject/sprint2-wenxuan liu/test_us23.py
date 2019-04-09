import unittest
from userstory23 import *
# same name same birthday
ind1 = {
    'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013',
            'DEAT_rec': 123, 'BIRI_rec': 11},
    'I07': {'id': 'I07', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'F', 'family': 'F23', 'DEAT': '31DEC2011',
            'DEAT_rec': 10, 'BIRI_rec': 13},
    'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013',
            'DEAT_rec': 32, 'BIRI_rec': 56}
    }
# same birthday different name
ind2 = {
    'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '23SEP1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013',
            'DEAT_rec': 123, 'BIRI_rec': 11},
    'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
            'DEAT': '31DEC2011', 'DEAT_rec': 10, 'BIRI_rec': 13},
    'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013',
            'DEAT_rec': 32, 'BIRI_rec': 56}
    }
# same name different birthday
ind3 = {
    'I01': {'id': 'I01', 'name': 'Dick /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013',
            'DEAT_rec': 123, 'BIRI_rec': 11},
    'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23',
            'DEAT': '31DEC2011', 'DEAT_rec': 10, 'BIRI_rec': 13},
    'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013',
            'DEAT_rec': 32, 'BIRI_rec': 56}
    }



# us23
class Us23(unittest.TestCase):
    # test userstory23
    def test_validation_check23(self):
        self.assertFalse(usstory23(ind1))
        self.assertTrue(usstory23(ind2))
        self.assertTrue(usstory23(ind3))


if __name__ == '__main__':
    unittest.main(verbosity=1)
