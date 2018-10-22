#!/usr/bin/python3.6 

import os
import sys


def listfilestree(actualdir):
    fileslist = os.listdir(actualdir)
    #dir_path = os.path.dirname(os.path.realpath(__file__)
    for nfile in fileslist:
        print(nfile)
        nfile = actualdir+nfile
        if os.path.isdir(nfile):
            print("Directory: ",nfile)
            listfilestree(nfile)

def main():  
    path = sys.argv[1]
    listfilestree(path)

if __name__=='__main__':
    main()