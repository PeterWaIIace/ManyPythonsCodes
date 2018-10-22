#!/usr/bin/python3.6

import sys
import re

fileslist = sys.argv[1:]
regex=re.compile(r'(\s+)why(\s+)|(\s)+[\w]*self(\s)+|(\s)+and(\s)+|(\s*)never(\s+)',re.I)
for nfile in fileslist:
    f = open(nfile,"r")
    for line in f:
        rline= regex.sub(' ',line)
        print(rline, end='')

