from __future__ import print_function
import os
import sys

def main():
    sys.argv.append("")
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        raise SystemExit(filename + ' does not exists')
    elif not os.access(filename, os.R_OK):
        raise SystemExit(filename + ' is not accessible')
    else:
        print(filename + ' is accessible')


if __name__ == '__main__':
    main()
