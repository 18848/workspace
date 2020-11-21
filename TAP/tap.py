# TAP - Test Anything Protocol

import ply.lex as lex
import re
from utils import readFile
from html import Test

tokens = ('TOTAL', 'STATUS', 'OFFSET', 'TEXT', 'SUBTEST')

t_ignore = " \t"
t_TOTAL = r"1..[1-9][0-9]*\n"
t_STATUS = r"ok|not\sok"
t_OFFSET = r"[1-9][0-9]*"
t_TEXT = r"-(\s([\w\d]*))*\n"
indentation = r"\t+|(\s\s\s\s)+"
t_SUBTEST = indentation + r"^\#" + t_STATUS + t_OFFSET + t_TEXT


class TAPData:

    def __init__(self):
        self.total = 0
        self.offset = []
        self.test = [(), ]
        self.status = []
        self.comment = []
        self.subtests = [(), ]

    def show(self):
        for x in range(1, len(self.test)):
            print(f"test {self.test.__getitem__(x)[0]} : {self.test.__getitem__(x)[1]} {self.test.__getitem__(x)[2]}")
        for x in range(1, len(self.subtests)):
            print(f"subtest {self.subtests.__getitem__(x)[0]} :"
                  f" {self.subtests.__getitem__(x)[1]} "
                  f"{self.subtests.__getitem__(x)[2]}")

    def rec_STATUS(self, t):
        test_status = re.fullmatch(r"(ok|not ok)", t.value)
        self.status = self.status + [test_status.group(0), ]

    def rec_OFFSET(self, t):
        test_pos = re.fullmatch(r"([1-9][0-9]*)", t.value)
        self.offset = self.offset + [test_pos.group(0), ]

    def rec_TEXT(self, t):
        test_comment = re.fullmatch(r"-(\s([\w\d]*))*\n", t.value)
        self.comment = self.comment + [test_comment.group(0), ]
        self.test = self.test + [(self.status.__getitem__(-1),
                                  self.offset.__getitem__(-1),
                                  self.comment.__getitem__(-1))]

    def rec_SUBTEST(self, t):
        self.rec_STATUS(t)
        self.rec_OFFSET(t)
        subtest_comment = re.fullmatch(r"-(\s([\w\d]*))*\n", t.value)  # TO CLEAR !!!!WARNING!!!!
        self.comment = self.comment + [subtest_comment.group(0), ]
        self.subtests = self.subtests + [
            (self.status.__getitem__(-1),
             self.offset.__getitem__(-1),
             self.comment.__getitem__(-1))]

# states = (("testcase", "exclusive"), ("comment", "exclusive"))


def t_error(t):
    print(f"AN ERROR OCCURRED !!! '{t.value}'")
    exit(1)


lexer = lex.lex()
lexer.input(readFile("..\\output\\teste1.t"))

global data

for token in iter(lexer.token, None):
    if token.type == 'TOTAL':
        data = TAPData()
    elif token.type == 'STATUS':
        data.rec_STATUS(token)
    elif token.type == 'OFFSET':
        data.rec_OFFSET(token)
    elif token.type == 'TEXT':
        data.rec_TEXT(token)
    elif token.type == 'SUBTEST':
         data.rec_SUBTEST(token)

data.show()
Test.getPrint(data)
