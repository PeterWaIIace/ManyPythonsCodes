#!/usr/bin/python3.6
import sys
import os
from PyPDF2 import PdfFileReader
from subprocess import call
import time
f = open(sys.argv[1], "ab")

z = ""
def recursive(lenrange,instr): 
    for i in range(33,126): #ASCII range (from space to end)
        z = str(chr(i))+str(instr)
        print(i)
        print("lenrange: ",lenrange," password: ",z)
        if(lenrange > 0):
            nlenrange = lenrange-1
            #print(z)
            recursive(nlenrange,z)
        else:
            password = str(z)
            #print(password)
            command = r'qpdf --password='+str(password)+" --decrypt "+str(f.name)+" pdfdecrypted.pdf"
        #print(str(command))      
            result=os.system(command)
            print(result)
        #with open(sys.argv[1], "wb") as out_file:
        #    output_pdf.write(out_file)
        #        print("[+] Password is: " + a)
        #        print("[...] Exiting..")
        #        sys.exit()

recursive(10,'')