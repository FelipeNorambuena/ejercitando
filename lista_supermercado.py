sw=1
listasuper=[]
valorsuper: list = []

while True:
    try:
        print("presione 1 para agregar un producto a la lista")
        print("presione 2 para eliminar un producto de la lista")
        print("presione 3 para ver la lista")  
        print("presione 4 para salir")
        op=int(input("ingrese una opcion: "))
        if op>0 or op<5:
            if op==1:
                producto=input("ingrese el producto: ")
                listasuper.append(producto)
                valor=input("ingrese el valor del producto: ")
                valorsuper.append(valor)
            elif op==2:
                producto=input("ingrese el producto a eliminar: ")
                if producto in listasuper:
                    pos=listasuper.index(producto)
                    listasuper.pop(pos)
                    valorsuper.pop(pos)
                else:
                    print("el producto no esta en la lista")
            elif op==3:
                print("lista de productos")
                for i in range(len(listasuper)):
                    print(listasuper[i],valorsuper[i])
            
            elif op==4:
                break
        else:
            print("opcion no valida")
    except ValueError:
        print("opcion ingresada no es valida, favor intentelo")