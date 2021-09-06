
def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    for i in range(1,height+1):
        print(' '*(height-i)+'*'*i)

if __name__=='__main__':
    main()
