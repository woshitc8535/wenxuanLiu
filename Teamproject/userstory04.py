from datetime import datetime


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