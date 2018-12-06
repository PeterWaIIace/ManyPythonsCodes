import random


length = 8 
height = 8

def createMatrix(Nmatrix):
    for l in range(length):
        tmp = []
        for h in range(height):
            value = random.randint(0,8)
            tmp.append(value)
        Nmatrix.append(tmp)

def product(Amatrix,Bmatrix):
    C = []
    for l in range(length):
        tmp = []
        for h in range(height):
            value = 0
            for i in range(height):
                value += Amatrix[i][h] * Bmatrix[l][i]
                #print("wysokosc: {}, wartosci macierzy A l,Amatrix[i][h],Bmatrix[l][i],value)    
            tmp.append(value)
        C.append(tmp)
    return C

def main():
    A = []
    B = []

    createMatrix(A)
    createMatrix(B)
    print("A: ",A)
    print("B: ",B)
    print("C: ",product(A,B))



if __name__=='__main__':
    main()
