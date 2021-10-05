def main():
    x = -1
    suma = 0
    a = 1
    b = 1
    lista= []
    #valores menores a 0, solicitar otra vez
    while x <= -1 :
        x = int(input())
    #valor igual a 0, lista vacia
    if x == 0 : 
        print(lista)
    #imprime 0
    elif x == 1: 
        lista.append(0)
        print(lista)
    #imprime 0,1
    elif x == 2: 
        lista.append(0)
        lista.append(1)
        print(lista)
    #imprime 0,1,1
    else:
        lista.append(0)
        lista.append(1)
        lista.append(1)
        #sumar ultimos dos digitos
        for i in range (x-3) :
            suma = a + b
            b = a
            a = suma
            lista.append(suma)
        print(lista)
    
if __name__=='__main__':
    main()
