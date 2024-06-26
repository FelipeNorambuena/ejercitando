'''' Un menu de usuario
1 agregar pelicula
2 listar peliculas
3 buscar pelicula
4 salir
El 1 tiene que agregar la pelicula en un diccionario
El 2 tiene que mostrar todas las peliculas registradas en el diccionario
El 3 tiene que buscar pelicula por su categoria
4 salir del menu y agregar las peliculas en un archivo de texto (.txt)
Pelicula

Codigo de pelicula 
Nombre de pelicula 
Anio de pelicula 
Categoría de pelicula 
Actores de pelicula (en una lista)
Director
Controlar errores de ingreso de numeros y excepciones'''


pelicula=[]
def menu():
    print("--------------------------------------------------------")
    print("menu de usuario ingrese una de las siguientes opciones")
    print("1.- agregar pelicula")
    print("2.-ver lista de peliculas")
    print("3.- buscar pelicula")
    print("4.- salir del menu")
    print("--------------------------------------------------------")
    op=int(input("ingrese una opcion: "))
    return op   
    if op==1:
        agregar_pelicula()
    elif op==2:
        listar_peliculas()
    elif op==3:
        buscar_pelicula()
    elif op==4:
        print("salir")
    else:
        print("opcion no valida")
        menu()
def agregar_pelicula():
    print("--------------------------------------------------------")
    print("agregar pelicula")
    print("--------------------------------------------------------")
    codigo=int(input("ingrese el codigo de la pelicula: "))
    nombre=input("ingrese el nombre de la pelicula: ")
    anio=int(input("ingrese el anio de la pelicula: "))
    categoria=input("ingrese la categoria de la pelicula: ")
    actores=[]
    n=int(input("ingrese el numero de actores de la pelicula: "))
    for i in range(n):
        actores.append(input("ingrese el nombre del actor: "))
    director=input("ingrese el nombre del director: ")
    pelicula={"codigo":codigo,"nombre":nombre,"anio":anio,"categoria":categoria,"actores":actores,"director":director}
    print("pelicula agregada")
    print(pelicula)
    menu()     
def listar_peliculas():
    print("--------------------------------------------------------")
    print("lista de peliculas")
    print("--------------------------------------------------------")
    print(pelicula)
    menu()
def buscar_pelicula():
    print("--------------------------------------------------------")
    print("buscar pelicula")
    print("--------------------------------------------------------")
    categoria=input("ingrese la categoria de la pelicula: ")
    if categoria in pelicula:
        print(pelicula)
    else:
        print("no se encontro la pelicula")
    menu()
    def salir():
        print("--------------------------------------------------------")
        print("salir")
        print("--------------------------------------------------------")
        archivo=open("peliculas.txt","w")
        archivo.write(pelicula)
        archivo.close()
        print("peliculas guardadas en archivo")
        menu()
