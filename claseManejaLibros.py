from claseLibro import Libro
from claseCapitulo import Capitulo
import csv

class ManejaLibros:
    __listaLibros = []

    def __init__(self):
        self.__listaLibros = []
        contLibros = -1
        contCap = 0
        archivo = open("libros.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            if (contCap == 0):       # evalua si es codigo o nombre
                d0 = int(fila[0])  # Codigo o nombre
                d1 = str(fila[1])  # titulo
                d2 = str(fila[2])  # autor
                d3 = str(fila[3])  # editorial
                d4 = int(fila[4])  # isbn
                d5 = int(fila[5])  # cant capitulos
                libro = Libro(d0,d1,d2,d3,d4,d5)
                self.__listaLibros.append(libro)
                contLibros += 1
                contCap = d5
            else:
                d0 = str(fila[0])  # titulo
                d1 = (fila[1])   #cant paginas
                capitulo = Capitulo(d0,d1)
                self.__listaLibros[contLibros].agregarCapitulo(capitulo)
                contCap -= 1
        archivo.close()
    
    def agregarLibro(self, libro):
        self.__listaLibros.append(libro)

    def getLista(self):
        return self.__listaLibros

    def getID(self, i):
        return self.__listaLibros[i].getID()

    