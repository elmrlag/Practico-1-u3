from claseManejaLibros import ManejaLibros
from os import system

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

def opcion1():
    id= int(input("Ingrese el identificador de un libro: "))
    band = False
    i = 0
    lista = Manejador.getLista()
    while band == False:
        if ( id == lista[i].getID()):
            print(f"Titulo libro: {lista[i].getTitulo()}")
            listaCap = lista[i].getCapitulos()
            for cap in listaCap:
                print(f"Capitulo: {cap.getTitulo()}")
                print(f"Cantidad de paginas: {cap.getCantPaginas()}")
            band = True
        i+=1

def opcion2():
    palabra= str(input("Ingrese una palabra: "))
    listaLibros = Manejador.getLista()
    for libro in listaLibros:
        listaTitulo = libro.getTitulo().split(" ")
        band = False
        i = 0
        while band == False and i < len(listaTitulo):
            if listaTitulo[i] != " ":
                if palabra.lower() == listaTitulo[i].lower():
                    print("Se encontro una coinsidencia en el titulo de un libro!")
                    print(f"Titulo: {libro.getTitulo()}")
                    print(f"Autor: {libro.getAutor()}")
                    band = True
                else:
                    i += 1
        
        ####
        
        listaCapitulos = libro.getCapitulos()
        j = 0
        while band == False and j < len(listaCapitulos):
            listaTitulo = listaCapitulos[j].getTitulo().split(" ")
            band2 = False
            k = 0
            while band2 == False and k < len(listaTitulo):
                if listaTitulo[k] != " ":
                    if palabra.lower() == listaTitulo[k].lower():
                        print("Se encontro una coinsidencia en el titulo de un capitulo!")
                        print(f"Titulo: {libro.getTitulo()}")
                        print(f"Autor: {libro.getAutor()}")
                        band = True
                        band2 = True
                    else:
                        k += 1
                j += 1

switcher = {
    1: opcion1,
    2: opcion2
}


if __name__ == "__main__":
    system("cls")
    Manejador = ManejaLibros()
    bandera = False
    while not bandera:
        print("0. Salir")
        print("1. Ingresar el identificador de un libro y mostrar título del libro, nombre de cada uno de sus capítulos y cantidad total de páginas de un libro.")
        print("2. Dada una palabra, mostrar título y autor de los libros que contienen la palabra dada en su título o en el título de alguno de sus capítulos.")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0
    exit()