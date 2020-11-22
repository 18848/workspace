# Utilities

def read_file(filename):
    fh = open(filename, mode="r")
    contents = fh.read()
    fh.close()
    return contents
