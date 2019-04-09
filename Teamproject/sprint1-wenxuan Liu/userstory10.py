from datetime import datetime

#US10
def hus_wife_idget(fam):
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
    n = hus_wife_idget(fam)

    for i in fam.keys():
        for value1 in n:
            if value1 in fam[i].keys():
                bir = fam[i][value1]['BIRT']
                bir = datetime.strptime(bir, '%d%b%Y')
                famid = fam[i][value1]['family']
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











