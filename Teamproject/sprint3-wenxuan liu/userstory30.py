# list living married
def us30(fam, indi):
    print('US30:person living and married')
    marriedlist = []
    namelist = []
    for i in fam:
        if 'DIV' not in fam[i] and 'WIFE' in fam[i] and 'HUSB' in fam[i]:
            marriedlist.append(fam[i]['HUSB'])
            marriedlist.append(fam[i]['WIFE'])
    # get married couple id
    for m in marriedlist:
        if 'DEAT' not in indi[m]:
            print(f'US30{indi[m]["name"]} is living and married.')
            namelist.append(indi[m]['name'])
    return namelist


