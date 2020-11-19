# data.py

class TAPData:

    def __init__(self, total, status, offset, comment):
        self.total = total
        self.offset = offset
        self.status = list.__add__(status)
        self.comment = list.__add__(comment)

    def show(self, pos):
        print(f"test {pos}: {self.status[pos]} - {self.comment[pos]}")
