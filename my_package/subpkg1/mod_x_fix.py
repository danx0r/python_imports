import sys
if __name__ == '__main__':
    sys.path.append('../../')
from my_package.subpkg1.mod_y import spam as ham
from my_package.mod_a import *

def main():
    ham()


if __name__ == '__main__':
    # This WILL work!
    main()
