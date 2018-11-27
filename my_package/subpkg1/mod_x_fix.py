if __name__ == '__main__':
    import sys
    sys.path.append('../../')
    import my_package
    print(my_package)
    from my_package.subpkg1.mod_y import spam as ham
else:
    from .mod_y import spam as ham

def main():
    ham()


if __name__ == '__main__':
    # This WILL work!
    main()