from __future__ import print_function
import argparse

def _argparse():
    parser = argparse.ArgumentParser(description="This is description")
    parser.add_argument('--host', action='store',
            dest='server',default="localhost", help='connect to host')
    parser.add_argument('-t', action='store_true',
            default=False, dest='boolean_switch', help='Set a switch to true')
    return parser.parse_args()

def main():
    parser = _argparse()
    print(parser)
    print('host =', parser.server)
    print('boolean_switch=', parser.boolean_switch)

if __name__ == '__main__':
    main()
