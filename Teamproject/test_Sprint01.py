import unittest
from us05us03 import check_birth_death as us03, marrige_before_death as us05
ind1 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013','DEAT_rec':123,'BIRI_rec':11},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23', 'DEAT': '31DEC2011','DEAT_rec':10,'BIRI_rec':13},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013','DEAT_rec':32,'BIRI_rec':56}
}

ind2={'I01': 
{'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013','MARR':'15MAR1980','DEAT_rec':67,'BIRI_rec':22,'MARR':28}
}

ind3 ={'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23','DEAT': '31DEC2013','DEAT_rec':32,'BIRI_rec':56},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12','BIRI_rec':23},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010','sex': 'M', 'family': 'F12','BIRI_rec':35},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997','sex': 'M', 'family': 'F23','BIRI_rec':56},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005','sex': 'F', 'family': 'F16','BIRI_rec':6},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003','sex': 'M', 'family': 'F16','BIRI_rec':99}
        }
ind4 ={'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23','BIRI_rec':11},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23','BIRI_rec':15},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23','BIRI_rec':18},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12','BIRI_rec':13},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F12','BIRI_rec':23},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23','BIRI_rec':25},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981','sex': 'F', 'family': 'F16','BIRI_rec':34},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16','BIRI_rec':142}}

ind5 ={'I01': 
{'id': 'I01', 'name': 'Joe /Smith/', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013','BIRI_rec':19,'DEAT_rec':90}
}

fam = {'F23': #one dead hus one alive wife 
	{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'MARR_rec':40},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','MARR_rec':22,}}
ind6 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013','DEAT_rec':200,'BIRI_rec':134},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23','BIRI_rec':141},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23','BIRI_rec':145},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23','BIRI_rec':53},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23','BIRI_rec':52},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23','BIRI_rec':50},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23','BIRI_rec':156}}

fam2 = {'F23': #both living and married spouses
	{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'MARR_rec':80},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','MARR_rec':179}}
ind7 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


fam3 = {'F23': #not married
	{'fam': 'F23', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind8 = {'I01': {'id': 'I01', 'name': 'Joe /Brown/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam4 = {'F23': #one dead hus death before marrige, one death wife after marrige
	{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30'],'MARR_rec':99},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','MARR_dec':228}}
ind9 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 1970','BIRI_rec':4,'DEAT_rec':22},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23','DEAT':'22 FEB 1990','BIRI_rec':35,'DEAT_rec':39},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


class Test_US03(unittest.TestCase):	
    def death_before_marrige(self):                           
        self.assertTrue(us05(ind6,fam))
        self.assertTrue(us05(ind7,fam2))
        self.assertFalse(us05(ind9,fam4))

    def test_birth_before_death(self):
        self.assertFalse(us03(ind1))
        self.assertTrue(us03(ind2))

    def no_death(self):
        self.assertTrue(us03(ind3))
        self.assertTrue(us03(ind4))

    def no_birth(self):
        self.assertTrue(us03(ind5))
	

		
if __name__ == '__main__':
    unittest.main()