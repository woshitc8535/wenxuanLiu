from datetime import datetime
from prettytable import PrettyTable as pt

from datetime import datetime
from prettytable import PrettyTable as pt

valid = {
    '0': (['INDI', 'FAM'], 'HEAD', 'TRLR', 'NOTE'),
    '1': ('NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV'),
    '2': ('DATE'),
}


def age_cal(birthday):
    birthdate = datetime.strptime(birthday, '%d%b%Y')
    current = datetime.today()
    return current.year - birthdate.year - ((current.month, current.day) < (birthdate.month, birthdate.day))


def parse_file(path, encode='utf-8'):
    with open(path, 'r', encoding=encode) as ged_file:
        isValid = 'Y OR N'
        IsIND = True
        indi = {}
        fam = {}
        currentDate = ''
        currentInd = ''
        currentFam = ''
        for line in ged_file:
            word_list = line.strip().split()
            arguments = ''.join(word_list[2:])
            tag = 'NA'
            level = 'NA'

            if len(word_list) == 1:
                level = word_list[0]
            elif len(word_list) > 1:
                level = word_list[0]
                tag = word_list[1]

            if len(word_list) == 3 and word_list[0] == '0' and word_list[2] in ('INDI', 'FAM'):
                isValid = 'Y'
                tag = word_list[2]

            elif len(word_list) > 1 and level in valid and tag in valid[level]:
                isValid = 'Y'

            if level == '0' and tag == 'INDI':
                currentInd = word_list[1]
                IsIND = True
                indi[currentInd] = {'id': word_list[1]}

            if IsIND:
                if level == '1' and tag == 'NAME':
                    indi[currentInd]['name'] = arguments
                if level == '1' and tag == 'BIRT' or tag == 'MARR' or tag == 'DEAT' or tag == 'DIV':
                    currentDate = tag
                if currentDate != '' and tag == 'DATE' and level == '2':
                    indi[currentInd][currentDate] = arguments

                if level == '1' and tag == 'SEX':
                    indi[currentInd]['sex'] = arguments
                if level == '1' and tag == 'FAMC' or tag == 'FAMS':
                    indi[currentInd]['family'] = arguments

            if level == '0' and tag == 'FAM':
                IsIND = False
                currentFam = word_list[1]
                fam[currentFam] = {'fam': currentFam}

            if IsIND == False:
                if level == '1' and word_list[1] == 'MARR' or word_list[1] == 'DIV':
                    currentDate = tag
                if level == '2' and tag == 'DATE':
                    fam[currentFam][currentDate] = arguments
                if level == '1' and tag in ('HUSB', 'WIFE'):
                    fam[currentFam][tag] = arguments
                if level == '1' and tag == 'CHIL':
                    if tag in fam[currentFam]:
                        fam[currentFam][tag].append(arguments)
                    else:
                        fam[currentFam][tag] = [arguments]

        indiTable = pt(["ID", "NAME", "Gender", "BDay", "Age", "Death", "Child", "Spouse"])
        indiTable.align['ID'] = '1'
        for key in sorted(indi):
            famID = indi[key]['family']
            if fam[famID]['HUSB'] == indi[key]['id'] or fam[famID]['WIFE'] == indi[key]['id']:
                spouse = famID
                chil = 'NA'
            else:
                spouse = 'NA'
                chil = famID
            if 'DEAT' in indi[key]:
                death = datetime.strptime(indi[key]['DEAT'], '%d%b%Y').date()
            else:
                death = 'NA'

            age = age_cal(indi[key]['BIRT'])
            indiTable.add_row([indi[key]['id'], indi[key]['name'], indi[key]['sex'],
                               datetime.strptime(indi[key]['BIRT'], '%d%b%Y').date(), age, death, chil, spouse])

        famTable = pt(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife name', 'Children'])
        for key in sorted(fam):
            if 'DIV' in fam[key]:
                div = datetime.strptime(fam[key]['DIV'], '%d%b%Y').date()

            else:
                div = "NA"

            if "HUSB" in fam[key]:
                hubID = fam[key]['HUSB']
                hubName = indi[hubID]['name']
            else:
                hubID = "NA"
                hubName = "NA"

            if "WIFE" in fam[key]:
                wifeID = fam[key]['WIFE']
                wifeName = indi[wifeID]['name']
            else:
                wifeID = "NA"
                wifeName = "NA"

            if 'CHIL' in fam[key]:
                chil = ','.join(fam[key]['CHIL'])
            else:
                chil = "NA"

            if 'MARR' in fam[key]:
                marr = datetime.strptime(fam[key]['MARR'], '%d%b%Y').date()
            else:
                marr = "NA"

            famTable.add_row([key, marr, div, hubID, hubName, wifeID, wifeName, chil])

        # print(indiTable)
        # print(famTable)

    return {'fam': fam, 'indi': indi}


# r = parse_file("D:\workspace\GED_file\My-Family-27-Jan-2019-230.ged")
# # r=parse_file('D:\workspace\sample_test.ged')
# print(r)

def Marrige_before_Divorce(fam):  # us04
    res = True
    for i in fam.keys():
        for n in fam[i]:

            if 'MARR' in fam[i][n].keys() and 'DIV' in fam[i][n].keys():
                marr = datetime.strptime(fam[i][n]['MARR'], '%d%b%Y').date()
                div = datetime.strptime(fam[i][n]['DIV'], '%d%b%Y').date()

                if marr > div:
                    warning = 'Error: '
                    print(warning + 'FAMILY: US04 ' + 'ID:' + fam[i][n]['fam'] + ' Divorced date ' + fam[i][n][
                        'DIV'] + ' before ' + 'Married ' + fam[i][n]['MARR'])
                    # file.write(warning)
                    res = False

    return res


def Marrige_date_get(fam):
    for i in fam.keys():
        for n in fam[i]:

            if 'MARR' in fam[i][n].keys():
                marr = datetime.strptime(fam[i][n]['MARR'], '%d%b%Y').date()
                yield marr
                # print(marr)


def Divorce_date_get(fam):
    for i in fam.keys():
        for n in fam[i]:

            if 'DIV' in fam[i][n].keys():
                div = datetime.strptime(fam[i][n]['DIV'], '%d%b%Y').date()
                return div
                # print(div)


# if __name__ == '__main__':
#     fam = parse_file('C:\\Users\\woshi\\PycharmProjects\\untitled1\\Teamproject\\My-Family-27-Jan-2019-230.ged')
#     Marrige_before_Divorce(fam)
#     Divorce_date_get(fam)
#     Marrige_date_get(fam)
#


def birthday_before_current(indi):
    res = True
    current_date = datetime.now().date()

    for i in indi.keys():
        for n in indi[i]:
            if "BIRT" in indi[i][n].keys():
                bir = datetime.strptime(indi[i][n]['BIRT'], '%d%b%Y').date()
                if bir > current_date:
                    print('Error')
                    res = False
    return True

#US10
def birthday_get(fam):
    list1 = []
    for i in fam.keys():
        for n in fam[i]:
            if 'MARR' in fam[i][n].keys():
                # print(fam[i][n])

                hus_get = fam[i][n]['HUSB']
                wife_get = fam[i][n]['WIFE']
                # marigedate= fam[i][n]['MARR']
                list1.append(hus_get)
                list1.append(wife_get)
    return list1





def marrige_after_14(fam):
    res = False
    list2=[]
    madtlist=[]
    n = birthday_get(fam)

    for i in fam.keys():
        for value1 in n:
            if value1 in fam[i].keys():
                bir = fam[i][value1]['BIRT']
                bir = datetime.strptime(bir, '%d%b%Y')
                famid = fam[i][value1]['FAMS']
                list2.append(famid)

    m=list2

    for i in fam.keys():
        for value2 in m:
            if value2 in fam[i].keys() and 'MARR' in fam[i][value2].keys():
                madt=fam[i][value2]['MARR']
                madt=datetime.strptime(madt,'%d%b%Y')

                mage=madt.year - bir.year - ((madt.month, madt.day) < (bir.month, bir.day))
                if mage < 14:
                    print('Error: ' + 'INDIVIDUAL: US10: ' +fam[i][value2]['fam']+'occur that someone marrige less than 14 years old')
                else:
                    res = True
        return res
















if __name__ == '__main__':
    fam = parse_file('C:\\Users\\woshi\\PycharmProjects\\untitled1\\Teamproject\\My-Family-27-Jan-2019-230.ged')
    # indi = parse_file('C:\\Users\\woshi\\PycharmProjects\\untitled1\\Teamproject\\My-Family-27-Jan-2019-230.ged')
    marrige_after_14(fam)