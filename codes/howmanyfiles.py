#!/usr/bin/python3
#

import os

filelist=os.listdir(r'/dev/')

print("Ther is a {} files in dev/ directory".format(len(filelist)))