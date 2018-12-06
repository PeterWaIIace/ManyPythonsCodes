#!/usr/bin/python3
#

import os

filelist=os.listdir(r'/dev/')

print("There is {} files in dev/ directory".format(len(filelist)))