from __future__ import print_function
import fileinput

for line in fileinput.input():
    print(line, end="")
