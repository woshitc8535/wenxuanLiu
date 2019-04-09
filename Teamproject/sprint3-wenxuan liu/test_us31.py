import unittest
from userstory31 import us31
fam = {
    'F1': {'fam': 'F1', 'HUSB': 'I2', 'WIFE': 'I3', 'CHIL': {'I1'}},
    'F2': {'fam': 'F2', 'HUSB': 'I4', 'WIFE': 'I5', 'CHIL': {'I6', 'I8', 'I2'}},
    'F3': {'fam': 'F3', 'HUSB': 'I6', 'WIFE': 'I7', 'MARR': '14AUG1985'},
    'F4': {'fam': 'F4', 'HUSB': 'I13', 'WIFE': 'I7', 'MARR': '15SEP2005'},
    'F5': {'fam': 'F5', 'HUSB': 'I8', 'WIFE': 'I10', 'CHIL': {'I11'}, 'MARR': '7AUG2008'},
    'F6': {'fam': 'F6', 'HUSB': 'I8', 'WIFE': 'I9', 'CHIL': {'I12'}, 'MARR': '8JUL1994', 'DIV': '14NOV2002'}
}

indi = {
    'I1': {'id': 'I1', 'name': 'Sam/Smith/', 'sex': 'M', 'BIRT': '7OCT1965', 'FAMC': {'F1'}},
    'I2': {'id': 'I2', 'name': 'Sam/Smith/', 'sex': 'M', 'BIRT': '7OCT1965', 'FAMS': {'F1'}, 'FAMC': {'F2'}},
    'I3': {'id': 'I3', 'name': 'Mary/Smith/', 'sex': 'F', 'BIRT': '13JUL1966', 'FAMS': {'F1'}},
    'I4': {'id': 'I4', 'name': 'Jordan/Smith/', 'sex': 'M', 'BIRT': '28SEP1939', 'FAMS': {'F2'}},
    'I5': {'id': 'I5', 'name': 'Alice/Smith/', 'sex': 'F', 'BIRT': '15JUN1943', 'DEAT': '7SEP2009',
           'FAMS': {'F2'}},
    'I6': {'id': 'I6', 'name': 'Sam/Smith/', 'sex': 'M', 'BIRT': '7OCT1965', 'DEAT': '11APR2002', 'FAMS': {'F3'},
           'FAMC': {'F2'}},
    'I7': {'id': 'I7', 'name': 'Jane/Forrest/', 'sex': 'F', 'BIRT': '24JAN1963', 'FAMS': {'F3', 'F4'}},
    'I8': {'id': 'I8', 'name': 'Chris/Smith/', 'sex': 'M', 'BIRT': '19JUN1800', 'FAMS': {'F5', 'F6'},
           'FAMC': {'F2'}},
    'I9': {'id': 'I9', 'name': 'Julie/Swift/', 'sex': 'F', 'BIRT': '25MAR1972', 'FAMS': {'F6'}},
    'I10': {'id': 'I10', 'name': 'Fiona/Gibson/', 'sex': 'F', 'BIRT': '24MAY1974', 'FAMS': {'F5'}},
    'I11': {'id': 'I11', 'name': 'Curry/Smith/', 'sex': 'M', 'BIRT': '12OCT2010', 'FAMC': {'F5'}},
    'I12': {'id': 'I12', 'name': 'Brown/Smith/', 'sex': 'M', 'BIRT': '8SEP1997', 'FAMC': {'F6'}},
    'I13': {'id': 'I13', 'name': 'Paul/Pierce/', 'sex': 'M', 'BIRT': '24NOV1960', 'FAMS': {'F4'}}
}

class Us31(unittest.TestCase):
    def test_output_us31(self):
        self.assertIn('Julie/Swift/',us31(fam,indi))
        self.assertIn('Curry/Smith/',us31(fam,indi))
        self.assertIn('Brown/Smith/',us31(fam,indi))

if __name__ == '__main__':
    unittest.main(verbosity=2)

