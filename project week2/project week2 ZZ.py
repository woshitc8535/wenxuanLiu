"""
Created on Mon Feb 04 17:19:18 2019
@author: zheng zhou
"""


class Project2:
    f = input("please input the path of file:   ")
    with open(f, 'r') as file:
        for line in file.read().splitlines():
            process_line()

    def process_line():
        valid_tag = {'0': ('HEAD', 'NOTE', 'TRLR'),
                     '1': ('BIRT', 'CHIL', 'DEAT', 'DIV', 'FAMC', 'FAMS', 'HUSB', 'MARR', 'NAME'),
                     '2': ('DATE')}
        print(f"-->{line}")
        tokens = line.split()

        if len(tokens) == 3 and tokens[0] == '0' and tokens[2] in ('INDI', 'FAM'):
            level, arg, tag = tokens
            valid = "Y"
        elif len(tokens) >= 2:
            level, tag, args = tokens[0], tokens[1], " ".join(tokens[2:])
            valid = 'Y' if level in valid_tag and tag in valid_tag[level] else 'N'
        else:
            level, tag, valid, arg = tokens, 'NA', 'N', 'NA'
        print(f'--<{level}{tag}{valid}{arg}')
