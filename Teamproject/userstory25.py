def usstory25(fam, indi):
    result = False
    for i in fam:
        if 'CHIL' in fam[i]:
            chid = fam[i]['CHIL']
            newlist = []
            list1 = []

            for x in chid:
                if 'name' and 'BIRT' in indi[x]:
                    name = indi[x]['name']
                    birth = indi[x]['BIRT']
                    list1.append(name)
                    list1.append(birth)
                    str = ''
                    name_birth = str.join(list1)
                    newlist.append(name_birth)
                    list1 = []
            if len(set(newlist)) != len(newlist):
                seen = set()
                duplicated = set()
                for x in newlist:
                    if x not in seen:
                        seen.add(x)
                    else:
                        duplicated.add(x)
                print('ERROR,There exist same name with same birthday in a famliy',fam[i]['fam'],duplicated)
            else:
                result = True
    return result
