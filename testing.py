

import numpy


abcList = ['A','B','C','D','E','F','G','H',"I",'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #Lista con el abecedario
#print (len(abcList))

#Metiendo abc list en codeMatrix

playFairMatrix = numpy.empty((5,5),dtype=object)
#print(playFairMatrix) #Pa ver la matriz de 5x5

#for i in range(5):
#    for j in range(5):
#        playFairMatrix[i,j] = abcList[:]


#for j in range(5):
#   playFairMatrix[0,j] = abcList[j]
#    playFairMatrix[1,j] = abcList[j+5]
#    playFairMatrix[2,j] = abcList[j+10]
#    playFairMatrix[3,j] = abcList[j+15]
#    playFairMatrix[4,j] = abcList[j+20]
aux = 0
for i in range(5):
    for j in range(5):
        playFairMatrix[i,j] = abcList[j+aux]
    aux += 5


print(playFairMatrix)
