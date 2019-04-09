from datetime import datetime
import os
from datetime import timedelta
from sprint01_yuzhen import Homework04_Zhonghua_Bao as hz

def userStory01(result):
    """implement user story 01, dates (birth, marriage, divorce, death) should not be after the current date,
       verify the date checked validity, return none if date is invalid, and then compare with current date,
       if it is not later than current date, return true, else return false
    """
    indi,fam = result['indi'],result['fam']   # get the summary of the test ged

    for key in indi.keys():
        if 'BIRT' in indi[key]:   # if indi has birthday, compare with the current date
            if hz.dateVerify(indi[key]['BIRT']) == False:
                birthday = datetime.strptime(indi[key]['BIRT'],'%d%b%Y')
                birth_str = birthday.strftime('%Y-%m-%d')
                print("ERROR: INDIVIDUAL: US01:",indi[key]['BIRT_rec'],":",indi[key]['id'],": Birthday",birth_str,"occurs in the future")
        
        if 'DEAT' in indi[key]:   # if indi has death date, compare with the current date
            if hz.dateVerify(indi[key]['DEAT']) == False:
                death = datetime.strptime(indi[key]['DEAT'],'%d%b%Y')
                death_str = death.strftime('%Y-%m-%d')
                print("ERROR: INDIVIDUAL: US01:",indi[key]['DEAT_rec'],":",indi[key]['id'],": Death",death_str,"occurs in the future")
    
    for key in fam.keys():
        if 'MARR' in fam[key]:   # if fam has marriage date, compare with the current date
            if hz.dateVerify(fam[key]['MARR']) == False:
                marr = datetime.strptime(fam[key]['MARR'],'%d%b%Y')
                marr_str = marr.strftime('%Y-%m-%d')
                print("ERROR: FAMILY: US01:",fam[key]['MARR_rec'],":",fam[key]['fam'],": Marriage",marr_str,"occurs in the future")
        
        if 'DIV' in fam[key]:   # if fam has divorce date, compare with the current date
            if hz.dateVerify(fam[key]['DIV']) == False:
                div = datetime.strptime(fam[key]['DIV'],'%d%b%Y')
                div_str = div.strftime('%Y-%m-%d')
                print("ERROR: FAMILY: US01:",fam[key]['DIV_rec'],":",fam[key]['fam'],": Divorce",div_str,"occurs in the future")


def userStory08(result):
    """implementing user story 08, the child birthday should not be earlier the parent's marriage date, and not be later than 9 months after the parent's divorce date if applicable
       only apply to those clear date, not to any 'NA'
       get this two date from the summary of ged, if wrong, print error statement
    """
    indi,fam = result['indi'],result['fam']

    for key in fam.keys():
        if 'CHIL' in fam[key]:   # only applicable to family has child, or it will raise keyerror
            for item in fam[key]['CHIL']:   # get the kid iterately    
                if 'BIRT' not in indi[item]:
                    continue
                else:
                    if 'MARR' not in fam[key]:
                        continue
                    else:
                        if hz.dateCompare(indi[item]['BIRT'],fam[key]['MARR']) == False:   # child birthday earlier than parent's marriage date
                            birth = datetime.strptime(indi[item]['BIRT'],'%d%b%Y')
                            birth_str = birth.strftime('%Y-%m-%d')
                            marr = datetime.strptime(fam[key]['MARR'],'%d%b%Y')
                            marr_str = marr.strftime('%Y-%m-%d')
                            print("ANOMALY:FAMILY: US08:",fam[key]['MARR_rec'],":",key,": Child",indi[item]['id'],"born",birth_str,"before marriage on",marr_str)
                    
                    if 'DIV' not in fam[key]:
                        continue
                    else:
                        div = datetime.strptime(fam[key]['DIV'],'%d%b%Y')
                        expire = div + timedelta(days=272)   # add 9 months to divorce date
                        expire_day = expire.strftime('%d%b%Y').upper()
                        
                        if expire_day.startswith('0'):   # string use 01 for 1, for later comparison without error, skip 0
                            expire_day = expire_day[1:]
                                               
                        if hz.dateCompare(indi[item]['BIRT'],expire_day) == True:
                            birth = datetime.strptime(indi[item]['BIRT'],'%d%b%Y')
                            birth_str = birth.strftime('%Y-%m-%d')
                            div_str = div.strftime('%Y-%m-%d')
                            print("ANOMALY:FAMILY: US08:",fam[key]['DIV_rec'],":",key,": Child",indi[item]['id'],"born",birth_str,"after divorce on",div_str)