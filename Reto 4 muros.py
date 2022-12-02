#Reto 4 

def muros (filas,columnas,anchos,largos) :

    world = []
    cont = 0
    colums = 0
    validatorItems = len(filas)

    if validatorItems == len(columnas) and validatorItems  == len(anchos) and validatorItems  == len(largos) :
    
        while cont < len(filas):
            f = filas[cont]
            c = columnas[cont]
            a = anchos[cont]
            l = largos[cont]

            contAnch = 0
            colums = c
            fila = f
            while contAnch < a :
                fila = f
                contAnch = contAnch + 1
                contLarg = 0
                while contLarg < l:
                    world.append(f"{fila},{colums}")
                    fila = fila + 1
                    contLarg = contLarg + 1
                colums = colums + 1
            cont = cont + 1
        return world[:]
    else:
        return world[:]


messageErrorArrayList = "\nTodos las listas deben tener la misma cantidad de elementos"

filas = [0,3,5,6]
columnas = [1,3,11,12]
anchos = [2,9,1,4]
largos = [5,2,2,1]

world = muros(filas,columnas,anchos,largos)

if len(world) > 0 :
    print(world)
else:
    print(messageErrorArrayList)



