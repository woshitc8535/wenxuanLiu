"""
Created on Mon Feb 04 17:19:18 2019
@author: zheng zhou
"""


def test_tag(infile, outfile):

    f = open(infile, 'r')
    result = list()
    for line in f.readlines():
        line = line.strip()
        input = "--> " + line
        print(input)
        result.append(input)
        msg = line.split()
        level = msg[0]
        valid_tag1 = ['HEAD', 'TRLR', 'NOTE']
        valid_tag2 = ['INDI', 'FAM']
        valid_tag3 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
                      'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        valid_tag4 = ['DATE']
        if level == '0':
            if msg[1] in valid_tag1:
                tag = msg[1]
                flag = 'Y'
                argument = ' '.join(msg[2:])
                l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)
            elif msg[2] in valid_tag2:
                tag = msg[2]
                flag = 'Y'
                ID = msg[1]
                l = "<-- %s|%s|%s|%s" % (level, tag, flag, ID)
            else:
                tag = msg[1]
                flag = 'N'
                argument = ' '.join(msg[2:])
                l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        elif level == '1':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag3:
                flag = 'Y'
            else:
                flag = 'N'
            l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        elif level == '2':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag4:
                flag = 'Y'
            else:
                flag = 'N'
            l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        else:
            tag = msg[1]
            flag = 'N'
            argument = ' '.join(msg[2:])
            l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        print(l)
        result.append(l)

    output = open(outfile, 'w')
    for line in result:
        output.write(line)
        output.write('\n')

    f.close()
    output.close()


def main():
    f1 = 'proj02test.ged'
    f2 = 'PJ02-Output.txt'
    f3 = 'proj02test.ged'
    f4 = 'PJ02-Test-Output.txt'
    test_tag(f1, f2)
    print('-----------------------------------------------------')
    test_tag(f3, f4)


if __name__ == '__main__':
    main()




