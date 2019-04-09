# the function of print next line


def parse_file(path, encode='utf-8'):
    with open(path, 'r') as ged_file:
        flag = True
        list = []
        for line in ged_file:
            # print(line)
            if flag == True:
                if line.startswith('<'):
                    list.append(line.strip())
                    flag = False
            else:
                list.append(line.strip())
                flag = True
        for line in ged_file:
            if line.endswith('>'):
                list.append(line.strip())


        print(list)


parse_file('C:\\Users\\woshi\\PycharmProjects\\untitled1\\Teamproject\\My-Family-27-Jan-2019-230.ged')
