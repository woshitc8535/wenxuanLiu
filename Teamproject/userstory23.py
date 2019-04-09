#No more than one individual with the same name and birth date should appear in a GEDCOM file
def usstory23(indi):
    list=[]
    newlist=[]
    result=False
    for i in indi:
        if 'name' in indi[i] and 'BIRT' in indi[i]:
            name= indi[i]['name']
            birthday= indi[i]['BIRT']
            list.append(name)
            list.append(birthday)
            str=''
            name_birth=str.join(list)
            newlist.append(name_birth)
            list=[]

    if len(set(newlist))!=len(newlist):
        seen=set()
        duplicated=set()
        for x in newlist:
            if x not in seen:
                seen.add(x)
            else:
                duplicated.add(x)
        print('ERROR,There exist same name with same birthday',duplicated)
    else:
        result=True
    return  result














