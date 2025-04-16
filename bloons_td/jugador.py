# crear la clase Jugador
class Jugador(object):
    def __init__(self, dinero, vidas):
        self.__dinero = None
        self.__vidas = None

        self.dinero = dinero
        self.vidas = vidas

    # getters y setters
    # dinero
    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self, dinero):
        if isinstance(dinero, int) and dinero >= 0:
            self.__dinero = dinero
        else:
            print("El dinero tiene que ser mayor o igual a 0")

    # vidas
    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, vidas):
        if isinstance(vidas, int) and vidas >= 0:
            self.__vidas = vidas
        else:
            print("El vidas tiene que ser mayor o igual a 0")
