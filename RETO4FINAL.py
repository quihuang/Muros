import os

def muros(fila,columna,ancho,alto):

    coordenadas = []
    cont = 0
    validatorItems = len(fila) 

    if validatorItems == len(columnas) and validatorItems  == len(anchos) and validatorItems  == len(largos) :

        while cont < len(fila):

            rows = fila[cont]
            columns = columna[cont]
            widths = ancho[cont]
            long = alto[cont]

            for i in range(0,long):
                for j in range(0, widths):
                    coordenadas.append(f"{rows+i}:{columns+j}")
            cont = cont + 1

        return coordenadas
    else:
        return coordenadas

messageErrorArrayList = "\nTodos las listas deben tener la misma cantidad de elementos"
messageExit = "\nSaliendo del programa..."
messageDataInvalid = "\nLa opción ingresada no es validad"
messageNumberInvalid = "\nLa opción debe ser un numero"

# filas = [0,3,5,6]
# columnas = [1,3,11,12]
# anchos = [2,9,1,4]
# largos = [5,2,2,1]

filas = []
columnas = []
anchos = []
largos = []

option = ""

while option != "2":

        print("\n==================================================")
        print("   WORLD CRAFT ASCII PARTE 2 CREACION DE MUNDOS   ")
        print("==================================================")
        print("1. Crear Mundo")
        print("2. Salir")

        option = input("Ingrese una opción : ")

        if option == "1":

            countMuros = 0
            cantidadMuros = int(input("\nIngrese la cantidad de muros a crear : "))

            while countMuros < cantidadMuros :
                os.system("clear")
                print("\n==================================================")
                print("\nMuro #",countMuros)

                filas.append(int(input("\nIngrese el numero de fila : ")))
                columnas.append(int(input("Ingrese el numero de columna : ")))
                anchos.append(int(input("Ingrese el ancho : ")))
                largos.append(int(input("Ingrese el alto : ")))  
                print("\n==================================================")
                countMuros = countMuros + 1

            world = muros(filas,columnas,anchos,largos)

            if len(world) > 0 :
                os.system("clear")
                print(f"\nLas posiciones de los muros son : \n\n{world}")
            else:
                os.system("clear")
                print(messageErrorArrayList)
        elif option == "2":
            os.system("clear")
            print(messageExit)
        else: 
            os.system("clear")
            print(messageDataInvalid)
    
