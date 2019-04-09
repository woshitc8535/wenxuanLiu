import unittest
from userstory25 import usstory25

fam4 = {'F23':
            {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],
             'MARR_rec': 99},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'MARR_dec': 228}}
ind9 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                'DEAT': '31 DEC 1970', 'BIRI_rec': 4, 'DEAT_rec': 22},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23',
                'DEAT': '22 FEB 1990', 'BIRI_rec': 35, 'DEAT_rec': 39},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}
# same name and birthday
fam3 = {'F23':
            {'fam': 'F23', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind8 = {'I01': {'id': 'I01', 'name': 'Joe /Brown/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                'DEAT': '31 DEC 2013'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}
#same name and different birthday
fam5 = {'F23':
            {'fam': 'F23', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind10 = {'I01': {'id': 'I01', 'name': 'Joe /Brown/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                'DEAT': '31 DEC 2013'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1982', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

class Us25(unittest.TestCase):
    def test_validation25_check(self):
        self.assertTrue(usstory25(fam4,ind9))
        self.assertFalse(usstory25(fam3,ind8))
        self.assertTrue(usstory25(fam5,ind10))


if __name__ == '__main__':
    unittest.main(verbosity=1)
