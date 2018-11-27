import sys
if __name__ == '__main__':
    sys.path.append('../../')
from my_package.subpkg1.mod_y import spam as ham

def main():
    ham()


if __name__ == '__main__':
    # This WILL work!
    main()
