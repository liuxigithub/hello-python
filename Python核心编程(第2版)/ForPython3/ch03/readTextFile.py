#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get filename
fname = input('Enter file name: ')
print(fname)

# attempt to open file for reading
try:
    fobj = open(fname, 'r')
except  e:
    print("*** file open error:", e)
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine),
    fobj.close()
