

class Libro:
    __idLibro = 0
    __titulo = 0
    __author = 0
    __editorial = 0
    __isbn = 0
    __cantCapitulos = 0
    __listaCapitulos = []

    def __init__(self, idLibro, titulo, author, editorial, isbn, cantCapitulos):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__author = author
        self.__editorial = editorial
        self.__isbn = isbn
        self.__cantCapitulos = cantCapitulos
        self.__listaCapitulos = []
    
    def agregarCapitulo(self, capitulo):
        self.__listaCapitulos.append(capitulo)

    def getID(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo

    def getCapitulos(self):
        return self.__listaCapitulos
    
    def getAutor(self):
        return self.__author