import sys
if __name__ == '__main__':
    sys.path.append('../')
from subpkg1.mod_y import spam as ham
from mod_a import *
from subpkg2.mod_z import zzz

def main():
    print ("z is the %dth letter in the alphabet" % zzz)
    ham()


if __name__ == '__main__':
    # This WILL work!
    main()
