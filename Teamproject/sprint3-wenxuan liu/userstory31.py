# list living single
def us31(fam, indi):
    marriedlist = []
    allpeoplelist = []
    singlelist = []
    namelist = []
    # print('person living and single')
    for i in fam:
        if 'DIV' not in fam[i] and 'WIFE' in fam[i] and 'HUSB' in fam[i]:
            marriedlist.append(fam[i]['HUSB'])
            marriedlist.append(fam[i]['WIFE'])
    # get married couple id

    for m in indi:
        if 'DEAT' not in indi[m]:
            allpeoplelist.append(indi[m]['id'])
            singlelist = [item for item in allpeoplelist if item not in marriedlist]
    for x in singlelist:
        print(f'US31:{indi[x]["name"]} is living and single.')
        namelist.append(indi[x]['name'])
    return namelist

