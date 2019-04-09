from datetime import datetime

def check_birth_death(indi): #us03 
    res = True

    for i in indi:
        if "BIRT" in indi[i] and "DEAT" in indi[i]:
            birthday = datetime.strptime(indi[i]["BIRT"],'%d%b%Y')
            deathday = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
            #marri_date = datetime.strptime(indi[i]['MARR'],'%d%b%Y')
    
            if birthday > deathday:
                warnin = ('ERROR:US03,%d:%s death date %s happened beofore birthdate %s'%\
                         (indi[i]['DEAT_rec'],i,indi[i]['DEAT'],indi[i]['BIRT']))
                print(warnin)
                #file.write(warnin)
                res = False
        
    return res

#ind1 = {'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13FEB1998', 'sex': 'F', 'family': 'F23','DEAT': '31DEC2013','MARR':'15MAR2016'},}

#s= check_birth_death_marri(ind1)




def marrige_before_death(ind,fam):
    res = True
    for f in fam:
        hus_id = "0"
        wife_id = "0"
        if 'MARR' in fam[f] and 'HUSB' in fam[f] and 'WIFE' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']
            marr_date = datetime.strptime(fam[f]['MARR'],"%d%b%Y")
            marr_str = marr_date.strftime('%Y-%m-%d')
        if hus_id in ind:
            if 'DEAT' not in ind[hus_id]:
                print('%s is alive and married!\n'%hus_id)
            else:
                death_date = datetime.strptime(ind[hus_id]['DEAT'],"%d%b%Y")
                death_str = death_date.strftime('%Y-%m-%d')
                if marr_date > death_date:
                    print('ERROR:US05,%d:%s death date %s happened beofore marrige %s'%\
                         (fam[f]['MARR_rec'],hus_id,death_str,marr_str),)
                    res=False 
        if wife_id in ind:
            if 'DEAT' not in ind[wife_id]:
                print('%s is alive and married!\n'%wife_id)
            else:
                death_date = datetime.strptime(ind[wife_id]['DEAT'],"%d%b%Y")
                death_str = death_date.strftime('%Y-%m-%d')
                if marr_date > death_date :
                    print('ERROR:US05,%d:%s death date %s happened beofore marrige %s'%\
                         (fam[f]['MARR_rec'],wife_id,death_str,marr_str))
                    res=False
    return res