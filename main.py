#Cifrado PLAYFAIR
#-----REGLAS-----
#1. La cadena a codificar debe estar en mayusculas y conjunta
#   Se deben eliminar signos de puntuacion
#   De ser posible eliminar acentos

#2. La clave a utilizar para cifrar debe omitir caracteres
#   repetidos, ejemplo: Calambre -> Calmbre y será cifrado
#   del arreglo.
import numpy #para ver si podemos iterar con matrices de caracteres
import sys

#Funcion para 'limpiar el mensaje'
def cleanMessage(dirtyMessage):
    upperMessage = dirtyMessage.upper() #Volviendo todo a mayusculas
    nonSpaceMessage = upperMessage.replace(" ", "") #Quitando espacios en blanco
    nonSpaceMessage = nonSpaceMessage.replace(".", "") #Quitando puntos
    nonSpaceMessage = nonSpaceMessage.replace(",", "") #Quitando comas
    nonSpaceMessage = nonSpaceMessage.replace("0", "") #Quitando numeros del 0-9
    nonSpaceMessage = nonSpaceMessage.replace("1", "")
    nonSpaceMessage = nonSpaceMessage.replace("2", "")
    nonSpaceMessage = nonSpaceMessage.replace("3", "")
    nonSpaceMessage = nonSpaceMessage.replace("4", "")
    nonSpaceMessage = nonSpaceMessage.replace("5", "")
    nonSpaceMessage = nonSpaceMessage.replace("6", "")
    nonSpaceMessage = nonSpaceMessage.replace("7", "")
    nonSpaceMessage = nonSpaceMessage.replace("8", "")
    nonSpaceMessage = nonSpaceMessage.replace("9", "")
    return nonSpaceMessage #Mensaje limpio

#Funcion para limpiar la clave de cifrado
def cleanCodificationCode(dirtyCode):
    print("Generando su clave, espere un momento...")
    upperCode = cleanMessage(dirtyCode) #Limpiamos la clave con la func cleanMessage
    upperCode = "".join(dict.fromkeys(upperCode)) #Limpiamos caracteres repetidos de la clave
    return upperCode #Clave limpia

#Funcion para generar la lista con todas las letras del abecedario, sin numeros
def abecedaryList(playFairKey):
    keyCodeList = list(playFairKey) #Separamos en elementos de una lista nuestra clave de encriptacion
    abcList = ['A','B','C','D','E','F','G','H',"I",'K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #Lista con el abecedario
    differencesList = [] #Lista vacia que tendra las diferencias entre los chars de KeyCodeList y abcList
    for character in abcList:
        if character not in keyCodeList: #Si el caracter está en abcList pero no en keyCodeList
            differencesList.append(character) #introduce el caracter en differencesList
    #Vamos a contemplar el caso de I/J
    #for i in range(len(keyCodeList)): #Recorremos toda la lista de la clave
    #    if keyCodeList[i] == "I" or keyCodeList == "J": #Si la clave tiene una I o una J
    #        differencesList.remove("IJ") #Entonces borramos de differencesList el elemento "IJ"
    finalCodeList = keyCodeList + differencesList #En una nueva lista juntamos las diferencias.
    if len(finalCodeList) != 25: #Interrumpe el flujo del programa si la longitud de la lista es distinta de 25
        print("ERROR! CARACTERES INSUFICIENTES, CONTACTE  A UN ADMINISTRADOR")
        sys.exit()
    codificationMatrix(finalCodeList) #Invocamos al metodo para generar la matriz
    return 0

#Funcion para generar y llenar la amtriz con el abecedario generado, con base en la clave dada por el usuario
def codificationMatrix(finalCodeList): 
    codeMatrix = numpy.empty((5,5), dtype=object) #Generamos la matriz de 5x5 con valores 0.
    abcPointer = 0 #Var que nos ayudará a llenar el arreglo de 5x5 con la lista 1D finalCodeList
    for i in range(5):
        for j in range(5):
            codeMatrix[i,j] = finalCodeList[j+abcPointer]
        abcPointer += 5 #Sumamos 5 despues de cada llenado de fila para recorrer el puntero inicial
    print(codeMatrix)

#Zona de pruebas, campo minado
print("----C I F R A D O    P L A Y F A I R----")
#Vamos a limpiar el mensaje a encriptar
uncodedMessage = input("Introduzca la cadena de texto a limpiar: ")
uncodedMessage = cleanMessage(uncodedMessage) #Obtenemos el mensaje limpio
print("Su mensaje limpio: ", uncodedMessage)
#Vamos a limpiar la clave con la cual encriptaremos el mensaje
playFairKey = input("Introduzca la clave para cifrar: ")
playFairKey = cleanCodificationCode(playFairKey)
print("Su clave: ", playFairKey)
abecedaryList(playFairKey)
