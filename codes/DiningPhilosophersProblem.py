#!/usr/bin/python

import threading
import time
import _thread

def jedzenie(nr, widelce):
    
   print("start")
   count = 0
   if ((nr+1)%5 > nr):            #Deadlock
      widelce[nr%5].acquire()
      time.sleep(5)
      widelce[(nr+1)%5].acquire()
   else:                              #Deadlock 
      widelce[(nr+1)%5].acquire()    #Deadlock 
      time.sleep(5)                  #Deadlock 
      widelce[nr%5].acquire()        #Deadlock 
   
   print("jem")

   if ((nr+1)%5 > nr):                #Deadlock
      widelce[(nr+1)%5].release()
      widelce[nr%5].release()
   else:                              #Deadlock
      widelce[nr%5].release()         #Deadlock
      widelce[(nr+1)%5].release()     #Deadlock
     
   print("end")

widelce = []
for i in range(0,5):
    widelce.append(threading.Lock())
#lock = threading.Lock()

try:
   _thread.start_new_thread( jedzenie, (0, widelce) )
   _thread.start_new_thread( jedzenie, (1, widelce) )
   _thread.start_new_thread( jedzenie, (2, widelce) )
   _thread.start_new_thread( jedzenie, (3, widelce) )
   _thread.start_new_thread( jedzenie, (4, widelce) )

except:
   print("Error: unable to start thread")

print("koniec")

while(1):
    pass