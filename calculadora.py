
par=0
try:
    while True:
        print("-------------------------------------------------------------")
        print("1.- Verifica si un numero es primo")
        print("2.- Verifica si un numero es par o impar")
        print("3.- Calcula la suma de los pares ingresados hasta ahora")
        print("4.- salir del programa")
        op=int(input("ingrese una opcion "))
        if op>0 and op<5:
            if op==1:
                
                print("Verifica si un numero es primo")
                numero_ingresado = int(input("Ingresa un número: "))
                es_primo = 1

                if numero_ingresado <= 1:
                    es_primo = 0
                else:
                    for i in range(2, int(numero_ingresado/2) + 1):
                        if numero_ingresado % i == 0:
                            es_primo = 0
                            break

                if es_primo:
                    print(f"{numero_ingresado} es un número primo.")
                else:
                    print(f"{numero_ingresado} no es un número primo.")
                    

            elif op==2:
                print("Verifica si un numero es par o impar")
                num=int(input("ingrese un numero "))
                if num%2==0:
                    print("el numero ingresado es par")
                    par=num+par
                else:
                    print("el numero ingresado es impar")
            

            elif op==3:
                print(f"la suma de los pares es {par}")


            elif op==4:
                print("gracias por utilizar el programa")
                break
except ValueError:
    print("la opcion ingresada no es correcta")
    