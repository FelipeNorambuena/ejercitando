sw=1
listanotas=[]
while sw==1:
    try:
        print("-------------------------------------------------------------")
        print("1.- Ingresar notas")
        print("2.- Ver promedio de notas")
        print("3.- salir del programa")
        op=int(input("ingrese una opcion "))
        if op>0 and op<4:
            if op==1:
                print("Ingresar notas")
                nota = float(input("Ingresa la nota: "))
                listanotas.append(nota)
            elif op==2:
                print(f"El promedio de las notas es {sum(listanotas)/len(listanotas)}")
            elif op==3:
                print("gracias por utilizar el programa")
                break
    except ValueError:
        print("la opcion ingresada no es correcta")