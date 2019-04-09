from datetime import datetime


def getAge(born):
    born = datetime.strptime(born,'%d%b%Y')
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#Get Age
def getAgeAt(born, given):
	born = datetime.strptime(born, '%d%b%Y')
	given = datetime.strptime(given, '%d%b%Y')
	return given.year - born.year - ((given.month, given.day) < (born.month, born.day))

#US10
def marrAfter14(fam, ind):
	result = True
	
	for f in fam:
		if("HUSB" in fam[f]): #check husb age
			husb = fam[f]["HUSB"]
			if(husb in ind and "BIRT" in ind[husb]):
				age = 0
				if("MARR" in fam[f]):
					age = getAgeAt(ind[husb]["BIRT"], fam[f]["MARR"])
				if(age <=14):
					print("ERROR: US10 - The individual "+husb+" was married before 14, this is invalid\n")
					result = False
		if("WIFE" in fam[f]): #check wife age
			wife = fam[f]["WIFE"]
			if(wife in ind and "BIRT" in ind[wife]):
				age = 0
				if("MARR" in fam[f]):
					age = getAge(ind[wife]["BIRT"])
				if(age <=14):
					print("ERROR: US10 - The individual "+wife+" was married before 14, this is invalid\n")
					result = False			
	return result