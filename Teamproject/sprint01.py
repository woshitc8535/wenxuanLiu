from datetime import datetime

indi = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15JUL2015', 'sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23SEP1960', 'sex': 'F', 'family': 'F23', 'DEAT': '31DEC2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13FEB1999','sex': 'M', 'family': 'F23', 'DEAT': '31DEC2013'}
}
def birth_before_death(indi): #us03
    res = True

    for i in indi:
        if "BIRT" in indi[i] and "DEAT" in indi[i]:
            birthday = datetime.strptime(indi[i]["BIRT"],'%d%b%Y')
            deathday = datetime.strptime(indi[i]['DEAT'],'%d%b%Y')
    
            if birthday > deathday:
                warnin = 'ERROR death of individual %s comes before birth.' %i
                print(warnin)
                #file.write(warnin)
                res = False

    return res



class indi_date:
    def __init__(self,ID,Birthdate,Marrige_date,Death_date='NA',Divorce_date='NA'):
        self.id = ID
        self.bdate = Birthdate
        self.Marrige = Marrige_date
        self.death = Death_date 
        self.divorce = Divorce_date

    def __str__(self):
        pass

    def marrige_before_death(self):  #us05
        res = True
        if self.Marrige and self.death:
            if self.Marrige > self.death:
                waring = 'ERROR death of individual %s comes before birth.'%self.id
                print(waring)
                res = False

        else: 
            print('Missing individual data.')

        return res

        


#   I1 = indi_date('I01',indi['I01']['BIRT'],Death=indi['I01']['DEAT'])



if __name__ =='__main__':
    while True:
        Options = '1 for Marriage&Death, \
                   2 for Birthday&Death,\
                   3 for Marriage&Birthday,\
                   4 for Quit'
                   
        print(Options)
        user_selc= input('Please enter your selections>>>')
        user_INDI_ID = input('Please enter individual id>>>')
        if user_selc == '4': break
        selection = {
            '1':'Marriage&Death',
            '2':'Birthday&Death',
            '3':'Marriage&Birthday',

        }   

        if user_selc and user_INDI_ID:
            print(selection[user_selc])
            if selection[user_selc] == selection['1']:
                indi_date.__getattribute__(indi[user_INDI_ID],indi['MARR'],indi['DEAT'])
                
                


                






