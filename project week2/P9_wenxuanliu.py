from string import punctuation
from collections import defaultdict
from operator import itemgetter


class P9:
    def get_result(self, path: str):
        dd1 = defaultdict(int)
        dd2 = defaultdict(int)
        count = 0
        total_num = 0
        trans_tab = str.maketrans({key: None for key in punctuation})
        try:
            file = open(path, encoding="utf-8")
        except FileNotFoundError:
            raise FileNotFoundError
        with file:
            for dirty_line in file:
                words = dirty_line.translate(trans_tab).lower().split()
                total_num += len(words)
                for word in words:
                    dd1[word] += 1
                    for char in [char for char in word if char.isalpha()]:
                        dd2[char] += 1
        print(f"Total words:{total_num} Total distinct words:{len(dd1.keys())}")
        for item in sorted(dd1.items(), key=itemgetter(1), reverse=True):
            if count > 26:
                break
            count += 1
            print(item[0], item[1])
        for item in sorted(dd2.items(), key=itemgetter(1), reverse=True):
            print(item[0], item[1])


def main():
    obj = P9()
    try:
        obj.get_result(input("please input file name"))
    except FileNotFoundError:
        print("file not found")
        main()


if __name__ == '__main__':
    main()
