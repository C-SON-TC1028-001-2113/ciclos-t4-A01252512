def pares(v1, v2):
    #cadena = ''
    if v1 == v2:
        print('No hay pares')

    else:
        if v1%2==1:
            v1 += 1

        for i in range(v1,v2+1,2):
            if i % 2 == 0:
                print(i)
                #if i < v2-1:
                    #cadena = cadena + str(i) + '\n'
                #else:
                    #cadena = cadena + str(i)
                
def main():
    val1 = int(input('Valor 1: '))
    val2 = int(input('Valor 2: '))
    if val1 > 0 and val2 > 0:
        if val2 >= val1:
            (pares(val1,val2))
        else:
            (pares(val2,val1))
    else:
        print('Escribe números enteros mayores a 0.')

if __name__=='__main__':
    main()