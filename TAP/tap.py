# TAP - Test Anything Protocol

import sys
import ply.lex as lex
import re
from utils import read_file
from html import get_print

tokens = ('TOTAL', 'STATUS', 'OFFSET', 'TEXT', 'INDENT', 'COMMENT')

t_TOTAL = r"1..[1-9]\d*\n"
t_STATUS = r"ok|not\ ok"
t_OFFSET = r"\ ([1-9]\d*)(\ |\n)"
t_TEXT = r"-(\ (\w*))*\n"
t_INDENT = r"\t|(\ \ \ \ )"
t_COMMENT = r"\#((.*))*\n"

flag = 0
filename = []
global fd


if len(sys.argv) != 2:
    print("Options:\n-Pass filename to analyze\n-Select from 0-7 for selected tests (0 -> selects all files)")
    exit(1)
else:
    if int(sys.argv[1]) == 0:
        filename.insert(0, "..\\output\\teste1.t")
        filename.insert(1, "..\\output\\teste2.t")
        filename.insert(2, "..\\output\\teste3.t")
        filename.insert(3, "..\\output\\teste4.t")
        filename.insert(4, "..\\output\\teste5.t")
        filename.insert(5, "..\\output\\teste6.t")
        filename.insert(6, "..\\output\\teste7.t")
    elif int(sys.argv[1]) == 1:
        filename.insert(0, "..\\output\\teste1.t")
    elif int(sys.argv[1]) == 2:
        filename.insert(1, "..\\output\\teste2.t")
    elif int(sys.argv[1]) == 3:
        filename.insert(2, "..\\output\\teste3.t")
    elif int(sys.argv[1]) == 4:
        filename.insert(3, "..\\output\\teste4.t")
    elif int(sys.argv[1]) == 5:
        filename.insert(4, "..\\output\\teste5.t")
    elif int(sys.argv[1]) == 6:
        filename.insert(5, "..\\output\\teste6.t")
    elif int(sys.argv[1]) == 7:
        filename.insert(6, "..\\output\\teste7.t")
    else:
        try:
            for file_count in range(0, len(filename)):
                filename[file_count] = str()  # (sys.argv[1])
                fd = open(filename)
        except IOError as file_error:
            print(f"Impossible to open file:\n{file_error}")
            exit(1)
        finally:
            fd.close()


class TAPData:

    def __init__(self):
        self.status = ""
        self.offset = ""
        self.text = ""
        self.comment = ""
        self.test = [("", "", "", -1), ]
        self.subtest = [("", "", "", -1), ]

    def show(self):
        count = 0
        for x in range(0, len(self.test)):
            print(f"test {self.test.__getitem__(x)[0]} : "
                  f"{self.test.__getitem__(x)[1]} "
                  f"{self.test.__getitem__(x)[2]}\n"
                  f"  subtest : {self.test.__getitem__(x)[3]}")
            if self.test.__getitem__(x)[-1] > 0:
                for y in range(0, self.test.__getitem__(x)[-1]):
                    print((self.subtest.__getitem__(count)[-1] * "\t") +
                          f"subtest {self.subtest.__getitem__(count)[0]} : "
                          f"{self.subtest.__getitem__(count)[1]} "
                          f"{self.subtest.__getitem__(count)[2]}"),
                    count += 1

    def rec_STATUS(self, t):
        test_status = re.fullmatch(r"ok|not ok", t.value)
        self.status = test_status.group(0)

    def rec_OFFSET(self, t):
        test_pos = re.fullmatch(r" ([1-9]\d*)[ \n]", t.value)
        self.offset = test_pos.group(0).strip("\n")

    def rec_TEXT(self, t, empty, string):
        global flag
        # Capture Text
        if empty:
            self.text = string
        else:
            test_text = re.fullmatch(r"(-( (\w*))*\n)", t.value)
            self.text = test_text.group(0).strip("\n")
        # Save Incidence
        # If test
        if flag == 0:
            # If first
            if self.test.__getitem__(-1)[-1] == -1:  # total_subtest == -1 $default
                self.test = [(self.status, self.offset, self.text, 0), ]  # Remove default values
            # If another
            elif flag == 0 and self.test.__getitem__(-1)[-1] != -1 and self.offset != "1":  # total_subtest == -1
                self.test = self.test + [(self.status, self.offset, self.text, 0), ]  # Add test
        # If subtest
        elif flag > 0:
            # If first
            if self.offset == " 1\n" or self.offset == " 1 ":
                # Change last test amount of subtest
                self.test = self.test[:-1] + [(self.test.__getitem__(-1)[0],
                                              self.test.__getitem__(-1)[1],
                                              self.test.__getitem__(-1)[2],
                                              self.test.__getitem__(-1)[-1] + 1), ]
                # If first ever
                if self.subtest.__getitem__(0)[0] == "":
                    # Remove default values
                    self.subtest = [(self.status, self.offset, self.text, flag), ]
                # If first in sequence
                else:
                    # Add to list
                    self.subtest = self.subtest + [(self.status, self.offset, self.text, flag), ]
            # If another
            elif self.offset != "1":
                # Increment amount of subtest
                self.test = self.test[:-1] + [(self.test.__getitem__(-1)[0],
                                               self.test.__getitem__(-1)[1],
                                               self.test.__getitem__(-1)[2],
                                               self.test.__getitem__(-1)[3] + 1), ]
                self.subtest = self.subtest + [(self.status, self.offset, self.text, flag), ]
            flag = 0


def t_error(t):
    print(f"AN ERROR OCCURRED !!! '{t.value}'")
    exit(1)


for file_count in range(0, len(filename)):
    lexer = lex.lex()
    lexer.input(read_file(filename[file_count]))
    print(filename[file_count])

    data = TAPData()

    check1 = False
    check2 = False
    check3 = False

    for token in iter(lexer.token, None):
        if token.type == 'TOTAL':
            flag = 0
        if token.type == 'STATUS':
            if check1 and check2:
                data.rec_TEXT(token, True, "")
                check3 = True
            check1 = True
            data.rec_STATUS(token)
        if token.type == 'OFFSET':
            check2 = True
            data.rec_OFFSET(token)
        if token.type == 'COMMENT':
            if check1 and check2:
                if check3:
                    data.rec_TEXT(token, True, "")
                else:
                    data.rec_TEXT(token, True, "")
            else:
                flag = 0
            check1 = check2 = check3 = False
        if token.type == 'TEXT':
            if check1 and check2:
                data.rec_TEXT(token, False, "")
            check1 = check2 = False
        if token.type == 'INDENT':
            check1 = check2 = False
            flag += 1
            pass

    data.show()
    print("\n")

get_print(data)
