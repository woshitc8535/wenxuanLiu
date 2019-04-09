# project week2 ssw555
# Wenxuan Liu
# C:\Users\woshi\PycharmProjects\untitled1\project week2\My-Family-23-Jan-2019-637.ged

def test_get():
    f = input('please input the file you want to test: ')
    with open(f, 'r') as file:
        for line in file.read().splitlines():
            print('<--' + line)
            line = line.split()
            level = line[0]
            if level == '0' and line[-1] in ['INDI', 'FAM']:
                tag = line[-1]
                line[0] = level + '|'
                line[1] = tag + '|Y|' + line[1]
                del line[-1]


            elif level == '1' and line[1] in ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE',
                                              'CHIL', 'DIV']:

                line[0] = level + '|'
                tag = line[1]
                line[1] = tag + '|Y|' + line[1]



            elif level == '2' and line[1] in ['DATE']:
                line[0] = level + '|'
                tag = line[1]
                line[1] = tag + '|Y|' + line[-1]
                del line[-1]
            elif level == '0' and line[1] in ['HEAD', 'TRLR', 'NOTE']:
                line[0] = level + '|'
                line[1] = line[1] + '|Y|'
            else:
                line[0] = level + '|'
                line[1] = line[1] + '|N|'
            print('-->' + ''.join(line))


if __name__ == '__main__':
    test_get()
