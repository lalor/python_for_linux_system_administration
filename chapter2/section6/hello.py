import os, sys

def main():
    print [item for item in os.listdir('.') if item.endswith('.py')];
    print sys.version


if __name__ == '__main__':
    main()
