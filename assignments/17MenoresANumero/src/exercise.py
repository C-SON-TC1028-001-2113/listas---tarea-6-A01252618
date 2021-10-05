#matriz que recibe valores
def menoradiez (x):
    matriz = []
    for i in range (len(x)): 
        for j in range(len(x[i])): 
            if x[i][j]<10 : 
                matriz.append(x[i][j])
    return(matriz)

def main():
    #lista de valores
    lista = []
    #numero filas
    fila = int(input())
    #numero columnas
    columna = int(input())
    for i in range (fila):
        lista.append([])
        for j in range (columna):
            valor = int(input())
            lista[i].append(valor)
    #lista de valores menores a 10
    y = menoradiez (lista)
    print(y)
   

if __name__=='__main__':
    main()
