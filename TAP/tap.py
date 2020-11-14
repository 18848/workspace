# TAP - Test Anything Protocol

import ply.lex as lex
import re
from utils import readFile

# tap_total = r"[0-9]+..[0-9]+\n"
# tap_status = r"ok\s|not\sok\s"
# tap_offset = r"[0-9]+"
# tap_text = r"(\s[A-Z][a-z]*)+\n"

tokens = ("TOTAL", "STATUS", "OFFSET", "TEXT")

states = (("testcase", "exclusive"), ("comment", "exclusive"))


# @lex.TOKEN(tap_total)
def t_TOTAL(t):
    r"1\.\.[0-9]+\n"
    t.lexer.begin("testcase")
    pass


# @lex.TOKEN(tap_status)
def t_testcase_STATUS(t):
    r"ok |not ok "
    t.lexer.begin("testcase")
    pass


# @lex.TOKEN(tap_offset)
def t_testcase_OFFSET(t):
    r"[0-9]+"
    t.lexer.begin("comment")
    pass


# @lex.TOKEN(tap_text)
def t_comment_TEXT(t):
    r"(.*)+\n"
    t.lexer.begin("testcase")
    pass


def t_error(t):
    print("AN ERROR OCCURRED !!!")
    exit(1)


def t_testcase_error(t):
    print("\tTESTCASE ERROR !!!")
    t_error(t)

def t_comment_error(t):
    print("\tCOMMENT ERROR !!!")
    t_error(t)


lexer = lex.lex()
print(lexer.current_state())
lexer.input(readFile("D:\\Uni\\Dev\\Workspace\\output\\teste1.t"))


total = 0
last_status = None
last_offset = 0

print("b4 for")

for token in iter(lexer.token, None):
    print("in for")
    print(token.value)
    if token.type == "TOTAL":
        total = re.fullmatch(r"1\.\.[0-9]+", token.value)
    elif token.type == "STATUS":
        last_status = token.value
    elif token.type == "OFFSET":
        last_offset = token.value
        # captures = re.fullmatch(r"([0-9]+):[0-9]+", token.value)
        # if int(captures.group(1)) >= 3:
        #     if last_interpreter in interpreter_counts:
        #         interpreter_counts[last_interpreter] += 1
        #     else:
        #         interpreter_counts[last_interpreter] = 1
    else:
        print(token)

print(total)
print(last_status)
print(last_offset)
print("\n read successful")
