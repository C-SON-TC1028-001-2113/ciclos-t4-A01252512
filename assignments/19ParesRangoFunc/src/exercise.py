def pares(v1, v2):
    cadena = ''
    pares = False

    for i in range(v1,v2+1):
        if i % 2 == 0:
            pares = True
            print(i)
            #if i < v2-1:
                #cadena = cadena + str(i) + '\n'
            #else:
                #cadena = cadena + str(i)
                
    if pares:
        return cadena
    else:
        print('No hay pares')

def main():
    val1 = int(input('Valor 1: '))
    val2 = int(input('Valor 2: '))
    if val2 >= val1:
        (pares(val1,val2))
    else:
        (pares(val2,val1))

if __name__=='__main__':
    main()