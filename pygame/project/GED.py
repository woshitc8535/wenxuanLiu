# @author: XX, ZZ2
# @project holder: PL, ZZ1
"""
    Update: 2019-2-11 13:22:17
    Log:
        creating Individual.add_child()
        creating Individual.add_spouse()
"""

import os
import datetime
from CheckGED import get_fam, get_indi
from prettytable import PrettyTable


class Individual:
    """Repository where we store all information about each person"""

    pt_labels = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

    def __init__(self, id):
        """Initiate a new instance for a individual"""
        self._id = id
        self._name = ''
        self._gender = ''
        self._bday = ''
        self._age = ''
        self._alive = True
        self._dday = 'N/A'
        self._child = 'N/A'
        self._spouse = 'N/A'

    def add_name(self, name):
        """Add person's name to instance"""
        self._name = name

    def add_sex(self, sex):
        """Add gender information to instance"""
        self._gender = sex

    def get_age(self):
        """Calculate individual's age"""
        dt1 = datetime.datetime.strptime(self._bday, '%d %b %Y')
        if not self._alive:
            dt2 = datetime.datetime.strptime(self._dday, '%d %b %Y')
        else:
            dt2 = datetime.datetime.now()

        self._age = ((dt2 - dt1).days) // 365

    def add_bday(self, bday):
        """Add birthday to instace"""
        if bday != '':
            self._bday = bday

    def add_dday(self, dday):
        """Add death infotmation to istance is needed"""
        if dday != '':
            self._alive = False
            self._dday = dday

    def pt_row(self):
        """Return information needed for prettytable"""
        return self._id, self._name, self._gender, self._bday, self._age, self._alive, self._dday, self._child, self._spouse

    def add_child(self, fam_ID):
        if fam_ID != '':
            self._child = fam_ID

    def add_spouse(self, fam_ID):
        if fam_ID != '':
            self._spouse = fam_ID

    def __str__(self):
        """Convert info to string"""
        return f"Individule:{self._id}, name: {self._name}, gender:{self._gender}, bday: {self._bday}, alive: {self._alive}, dday: {self._dday}, age: {self._age}"


class Family():
    def __init__(self, fam_ID, married, divorced, hus, wife, child_id):
        self.fam_ID = fam_ID
        self.mar_date = married
        self.div_date = divorced
        self.hus_id = hus
        self.wife_id = wife
        self.child_id = child_id


class Repository():
    def __init__(self, filename, dir_path=os.getcwd()):
        self.People = dict()
        self.Familis = dict()
        self.working_path = dir_path
        self.filename = filename
        self.read_indi()
        self.read_detail()
        self.input_family()

    def read_indi(self):
        """Read through file, combine information for each person and create a istance of Individual"""
        dd = get_indi(self.working_path, self.filename)
        for i in dd.keys():
            self.People[i] = Individual(i)

    def read_detail(self):
        """Read all detail information for each person, and modify the instaces accordigly"""
        dd = get_indi(self.working_path, self.filename)
        for i in dd.keys():
            for j in range(len(dd[i])):
                if dd[i][j].startswith('1|NAME|'):
                    self.People[i].add_name(dd[i][j].split('|')[3])

                elif dd[i][j].startswith('1|SEX|'):
                    self.People[i].add_sex(dd[i][j].split('|')[3])

                elif dd[i][j].startswith('1|BIRT|'):
                    self.People[i].add_bday(dd[i][j + 1].split('|')[3])

                elif dd[i][j].startswith('1|DEAT|'):
                    self.People[i].add_dday(dd[i][j + 1].split('|')[3])
                elif dd[i][j].startswith('1|FAMS|'):
                    self.People[i].add_spouse(dd[i][j].split('|')[3])
                elif dd[i][j].startswith('1|FAMC|'):
                    self.People[i].add_child(dd[i][j].split('|')[3])
            self.People[i].get_age()

    def individual_pt(self):
        """Create prettytable for all instances of class Individual"""
        pt = PrettyTable(field_names=Individual.pt_labels)
        for i_id in sorted(self.People.keys()):
            pt.add_row(self.People[i_id].pt_row())

        print('\n', 'Inidividuals')
        print(pt, '\n')

    def input_family(self):
        path = self.working_path
        filename = self.filename
        fam_lst = list(get_fam(path, filename))
        # print("fam_lst: ", fam_lst)
        for fam_dic in fam_lst:
            # print(fam_dic)
            new_family = Family(fam_dic['fam_ID'], fam_dic['mar_date'], fam_dic['div_date'], fam_dic['hus'],
                                fam_dic['wife'], fam_dic['children'])
            self.Familis[fam_dic['fam_ID']] = new_family

    '''
    def getPeople(self, ID):
        for ind_ID, individual in self.People.items():
            # print(ind_ID, individual._id, ID)
            if ind_ID == ID:
                return individual


    def getPeople_id(self, name):
        for individual in self.People.values():
            if name == individual._name:
                return individual._id
    '''

    def get_people_name(self, ID):
        for individual in self.People.values():
            if ID == individual._id:
                return individual._name

    def output_family(self):
        field_name = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']
        table = PrettyTable(field_names=field_name)
        hus_name = 'NA'
        wife_name = 'NA'
        for family in self.Familis.values():
            if family.hus_id != 'NA':
                hus_name = self.get_people_name(family.hus_id)
            if family.wife_id != 'NA':
                wife_name = self.get_people_name(family.wife_id)
            table.add_row(
                [family.fam_ID, family.mar_date, family.div_date, family.hus_id, hus_name, family.wife_id, wife_name,
                 family.child_id])

        print(table.get_string(sortby='ID'))

    def US10_marriae_after_14(self, fam_id):
        """For a given fam_id, check the family marriage date and death date for each individual belongs to this family, return the result of checking"""
        result = ''

        if self.Familis[
            fam_id].mar_date != 'NA':  # check for marriage date, if there is not marriage date, change result
            mdt = datetime.datetime.strptime(self.Familis[fam_id].mar_date,
                                             '%Y-%m-%d')  # If there is marriage date, covert it to datetime object
            hus_id = self.Familis[fam_id].hus_id
            wife_id = self.Familis[fam_id].wife_id
            bdt = datetime.datetime.strptime(self.People[hus_id]._bday, '%d %b %Y')
            mage = mdt.year - bdt.year - ((mdt.month, mdt.day) < (bdt.month, bdt.day))
            print(mage)
            if mage < 14:
                print('ERROR')
            else:
                result = True
        return result

    # def US07_less_than_150(self, individual_ID):
    #     result = True
    #     bdt = datetime.datetime.strptime(self.People[individual_ID]._bday, '%d %b %Y')
    #     current = datetime.datetime.today()
    #     age = current.year - bdt.year - ((current.month, current.day) < (bdt.month, bdt.day))
    #
    #     if age > 150:
    #         print(self.People[individual_ID], "The age is more than 150")
    #         result = False
    #     return result
        # us_07
    def us07_age_less_150(self, individual_ID):
        # result = ''

        # bdt = datetime.datetime.strptime(self.People[individual_ID]._bday, '%d %b %y')
        for people in self.People.values():
            if people._id == individual_ID:
                if people._age > 150:
                    raise (ValueError("The age is more than 150"))
                else:
                    return True
        return False

 #us_15
    def US15_Fewer_15_Child(self):
      # For a given fam_id, check if the family has more than 15 children
        for family in self.Familis.values():
            if len(family.child_id) < 15:
                return True
            else:
                return False

def main():
    # path = input("Input path: ")
    # filename = input("Input filename: ")
    rep = Repository(filename='My-Family-27-Jan-2019-230.ged',
                     dir_path='C:\\Users\\woshi\\PycharmProjects\\untitled1\\Teamproject')
    # rep.individual_pt()
    # rep.output_family
    # for i in rep.Familis.keys():
    #     print(rep.US10_marriae_after_14(i))
    a=rep.US15_Fewer_15_Child()
    print(a)

if __name__ == "__main__":
    main()
