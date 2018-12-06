import random
from multiprocessing import Pool
import multiprocessing as mp 
from multiprocessing import Process
from multiprocessing import Lock, Array
import numpy as np
from matplotlib import pyplot as plt
import time

howmuchdata = 8000000


def createDataSet():
    dataSet = []
    for k in range(howmuchdata):
        dataSet.append(int(random.random()*100))
    return dataSet.copy()

def createHist(dataSet,histogram,lockarg):
    histogram = [0] * (max(dataSet)+1)
    for datafromSet in dataSet:
        histogram [datafromSet] = histogram [datafromSet] + 1 
    return histogram

if __name__=="__main__":
    histogram = []
    
    dataSet = createDataSet()
    nothingimportant = 0
    start =time.time()
    histogram=createHist(dataSet,histogram,nothingimportant)
    finish = time.time()-start
    print(f"Calculation of histogram from {howmuchdata}, took: {finish}")

   
    
    dataSet2 = createDataSet()
    pool = Pool(processes=2) 
    lockarg = Lock()
    multiprocessingList = Array('i',range(max(dataSet2)))
    for data in range(max(dataSet2)):
        multiprocessingList[data] = 0
    start2 =time.time()
    p1 = Process(target=createHist,args=(dataSet2[0:int(len(dataSet2)/2)],multiprocessingList,lockarg))
    p2 = Process(target=createHist,args=(dataSet2[int(len(dataSet2)/2):len(dataSet2)],multiprocessingList,lockarg))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish2 = time.time()-start2
    print(f"Multiprocess calculation time: {finish2}")
    plt.bar(np.arange(len(histogram)),histogram)
    plt.show()


