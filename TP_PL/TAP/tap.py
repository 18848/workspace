# TAP - Test Anything Protocol

import sys
import ply.lex as lex
from utils import read_file
from utils import TAPData
from html import get_print

tokens = ('TOTAL', 'STATUS', 'OFFSET', 'TEXT', 'INDENT', 'COMMENT')

t_TOTAL = r"1..[1-9]\d*\n"
t_STATUS = r"ok|not\ ok"
t_OFFSET = r"\ ([1-9]\d*)(\ |\n)"
t_TEXT = r"-(\ [\w\d]*)*\n"
t_INDENT = r"\t|(\ \ \ \ )"
t_COMMENT = r"\#((.*))*\n"

filename = []
global fd

if len(sys.argv) != 2:
    print("Options:\n-Pass filename to analyze\n-Select from 0-7 for selected tests (0 -> selects all files)")
    exit(1)
elif sys.argv[1].isdigit():
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
    for file_count in range(1, len(sys.argv)):
        filename.insert((file_count - 1), str(sys.argv[file_count]))
    try:
        for file_count in range(0, len(filename)):
            fd = open(filename[file_count])
    except IOError as file_error:
        print(f"Impossible to open file:\n{file_error}")
        exit(1)
    finally:
        fd.close()


def t_error(t):
    print(f"AN ERROR OCCURRED !!! '{t.value}'")
    exit(1)


data = []

for file_count in range(0, len(filename)):
    lexer = lex.lex()
    lexer.input(read_file(filename[file_count]))
    print(filename[file_count])

    data.insert(file_count, TAPData())

    check1 = False
    check2 = False
    check3 = False

    for token in iter(lexer.token, None):
        if token.type == 'TOTAL':
            data[file_count].flag = 0
        if token.type == 'STATUS':
            if check1 and check2:
                data[file_count].rec_TEXT(token, True, "")
                check3 = True
            check1 = True
            data[file_count].rec_STATUS(token)
        if token.type == 'OFFSET':
            check2 = True
            data[file_count].rec_OFFSET(token)
        if token.type == 'COMMENT':
            if check1 and check2:
                if check3:
                    data[file_count].rec_TEXT(token, True, "")
                else:
                    data[file_count].rec_TEXT(token, True, "")
            else:
                data[file_count].flag = 0
            check1 = check2 = check3 = False
        if token.type == 'TEXT':
            if check1 and check2:
                data[file_count].rec_TEXT(token, False, "")
            check1 = check2 = False
        if token.type == 'INDENT':
            check1 = check2 = False
            data[file_count].flag_increment()
            pass

    data[file_count].show()
    print("\n")

get_print(data)
