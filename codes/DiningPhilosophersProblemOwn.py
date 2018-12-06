import threading 
import time
import _thread 

number_of_forks_and_philosophers = 5

def Dining(who, cutlery): #nobody is going to eat anything because there is deadlock
    print("I am going to eat with two forks",who)
    cutlery[(who-1)%len(cutlery)].acquire()
    time.sleep(1)
    cutlery[who%len(cutlery)].acquire()

    print("Oh this dinner is so good",who)

    time.sleep(1)
    cutlery[(who-1)%len(cutlery)].release()
    time.sleep(1)
    cutlery[who%len(cutlery)].release()

    print("I finished my diner I can leave my forks on the table",who)

def DiningwithDifferentStrategy(who, cutlery):
    print("I am going to eat with two forks",who)
    if((who+1)%len(cutlery) < who):
        cutlery[(who+1)%len(cutlery)].acquire()
        time.sleep(1)
        cutlery[who%len(cutlery)].acquire()
    else:
        cutlery[who%len(cutlery)].acquire()
        time.sleep(1)
        cutlery[(who+1)%len(cutlery)].acquire()

    print("Oh this dinner is so good",who)

    time.sleep(1)

    if((who+1)%len(cutlery) < who):
        cutlery[(who+1)%len(cutlery)].release()
        time.sleep(1)
        cutlery[who%len(cutlery)].release()
    else:
        cutlery[who%len(cutlery)].release()
        time.sleep(1)
        cutlery[(who+1)%len(cutlery)].release()
        

    print("I finished my diner I can leave my forks on the table",who)
    

forks = []
for i in range(number_of_forks_and_philosophers):
    forks.append(threading.Lock())

try:
    for number in range(number_of_forks_and_philosophers):
        # _thread.start_new_thread(Dining,(number,forks))  #function with deadlock
        _thread.start_new_thread(DiningwithDifferentStrategy,(number,forks))

except:
    print("I tried and failed start new theard. I ask for forgivness")

while(1):
    pass
