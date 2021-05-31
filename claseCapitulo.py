class Capitulo:
    __titulo = 0
    __cantPaginas = 0

    def __init__(self, titulo, cantPaginas):
        self.__titulo = titulo
        self.__cantPaginas = cantPaginas

    def getTitulo(self):
        return self.__titulo

    def getCantPaginas(self):
        return self.__cantPaginas