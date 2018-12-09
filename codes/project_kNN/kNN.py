import csv 
import random 
import time
import math
import operator

def euclideanDistance(data1, data2, length): #just a straight line, no need for so smart name
    distance = 0
    for x in range(length):
        distance += pow(data1[x]-data2[x],2) 
    return math.sqrt(distance)


def loadDataSet(filename, split, trainingSet=[],testSet = []):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataSet = list(lines)
        for y in range(len(dataSet)-1):
            for x in range(4):
                dataSet[y][x]=float(dataSet[y][x]) # str to float
            if random.random() < split:
                trainingSet.append(dataSet[y])
            else:
                testSet.append(dataSet[y])

def getNeighbors(instanceToCheck, referenceSet,k):
    distances = []
    length = len(instanceToCheck) - 1 # last field is str
    for x in range(len(referenceSet)):
        dist=euclideanDistance(instanceToCheck,referenceSet[x],length)
        distances.append((referenceSet[x],dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for y in range(k):
        neighbors.append(distances[y][0])
    return neighbors

def getResponse(neighbors):
    neighborsVotes = {}
    for y in range(len(neighbors)):
        vote = neighbors[y][-1]  # taking the name of flower
        if vote in neighborsVotes:
            neighborsVotes[vote] += 1
        else:
            neighborsVotes[vote] = 1
    sortedVotes =sorted(neighborsVotes.items(), key=operator.itemgetter(1), reverse=True) # reverse - we want the highest score
    return sortedVotes[0][0]
    
def getAccuracy(testSet,prediction):
    accurate = 0
    for y in range(len(testSet)):
        if testSet[y][-1] == prediction[y]:
            accurate += 1
    return float(accurate/len(testSet))*100.0


def main(split):

    if split <= 0 or split >= 1:
        raise ValueError("split value must be between 0 and 1")

    trainingSet=[]
    testSet=[]
    prediction = []
    k = 25
    loadDataSet('iris.data', split, trainingSet, testSet)
    print('Train: ',(len(trainingSet)))
    print('Test: ',(len(testSet)))

    for smth in testSet:
        neighbors = getNeighbors(smth,trainingSet,k)
        prediction.append(getResponse(neighbors))
        print(f"Prediction: {getResponse(neighbors)}, Real: {smth[-1]}")

    accuracy = getAccuracy(testSet,prediction)
    print(f"Accuracy: {accuracy }")

    return accuracy

if __name__ == "__main__":
    main(0.2)