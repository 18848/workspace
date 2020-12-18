# Utilities

import re


def read_file(filename):
    fh = open(filename, mode="r")
    contents = fh.read()
    fh.close()
    return contents


class TAPData:

    def __init__(self):
        self.flag = 0
        self.status = ""
        self.offset = ""
        self.text = ""
        self.comment = ""
        self.test = [("", "", "", -1), ]
        self.subtest = [("", "", "", -1), ]

    def flag_increment(self):
        self.flag += 1

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
        # Capture Text
        if empty:
            self.text = string
        else:
            test_text = re.fullmatch(r"(-( [\w\d]*)*\n)", t.value)
            self.text = test_text.group(0).strip("\n")
        # Save Incidence
        # If test
        if self.flag == 0:
            # If first
            if self.test.__getitem__(-1)[-1] == -1:  # total_subtest == -1 $default
                self.test = [(self.status, self.offset, self.text, 0), ]  # Remove default values
            # If another
            elif self.test.__getitem__(-1)[-1] != -1 and self.offset != "1":  # total_subtest == -1
                self.test = self.test + [(self.status, self.offset, self.text, 0), ]  # Add test
        # If subtest
        elif self.flag > 0:
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
                    self.subtest = [(self.status, self.offset, self.text, self.flag), ]
                # If first in sequence
                else:
                    # Add to list
                    self.subtest = self.subtest + [(self.status, self.offset, self.text, self.flag), ]
            # If another
            elif self.offset != "1":
                # Increment amount of subtest
                self.test = self.test[:-1] + [(self.test.__getitem__(-1)[0],
                                               self.test.__getitem__(-1)[1],
                                               self.test.__getitem__(-1)[2],
                                               self.test.__getitem__(-1)[3] + 1), ]
                self.subtest = self.subtest + [(self.status, self.offset, self.text, self.flag), ]
            self.flag = 0
