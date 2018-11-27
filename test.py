"""
https://www.blog.pythonlibrary.org/2016/03/01/python-101-all-about-imports/

Open a terminal and cd to the folder that has my_package, but not into my_package. Run the Python interpreter in this folder. I’m using iPython below mainly because its auto-completion is so handy:

In [1]: import my_package
 
In [2]: my_package.subpackage1.module_x
Out[2]: <module 'my_package.subpackage1.module_x' from 'my_package/subpackage1/module_x.py'>
 
In [3]: my_package.subpackage1.module_x.main()
spam spam spam
"""

import my_package
print (my_package.subpkg1.mod_x) 
my_package.subpkg1.mod_x.main()

print("~~~~~~~~~~~~~FAILURE:~~~~~~~~~~~~~~~")
import os
os.chdir("my_package/subpkg1")
os.system("python3 mod_x.py")

print("~~~~~~~~~~~~~SUCCESS:~~~~~~~~~~~~~~~")
os.system("python3 mod_x_fix.py")

print("~~~~~~~~~~~~~INTERACTIVE:~~~~~~~~~~~~~~~")
from my_package.subpkg1.mod_x import *
main()
