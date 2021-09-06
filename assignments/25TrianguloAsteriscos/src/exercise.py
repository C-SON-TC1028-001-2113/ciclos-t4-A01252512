
def main():
    lineas = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    for i in range(1,lineas+1):
        print(' '*(lineas-i)+'*'*i)

if __name__=='__main__':
    main()
