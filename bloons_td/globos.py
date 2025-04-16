# crear la clase Globo
class GloboBase(object):
    def __init__(self, color, damage, vida, velocidad):
        self.__colores = ("Rojo", "Azul", "Verde", "Amarillo")
        self.__color = None
        self.__damage = None
        self.__vida = None
        self.__velocidad = None

        self.color = color
        self.damage = damage
        self.vida = vida
        self.velocidad = velocidad

    # getters y setters
    # colores
    @property
    def colores(self):
        return self.__colores

    # color
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        if color in self.colores:
            self.__color = color

    # damage
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, damage):
        if isinstance(damage, int) and damage > 0:
            self.__damage = damage
        else:
            print("El damage tiene que ser mayor a 0")
    
    # vida
    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        if isinstance(vida, int) and vida >= 0:
            self.__vida = vida
        else:
            print("El vida tiene que ser mayor a 0")

    # velocidad
    @property
    def velocidad(self):
        return self.__velocidad
    
    @velocidad.setter
    def velocidad(self, velocidad):
        if isinstance(velocidad, int) and velocidad > 0:
            self.__velocidad = velocidad
        else:
            print("La velocidad tiene que ser mayor a 0")

    # metodo cambiar color
    def cambiar_color(self):
        index = self.colores.index(self.color)
        if index == 3:
            self.__class__ = GloboVerde
            GloboVerde.__init__(self)
        elif index == 2:
            self.__class__ = GloboAzul
            GloboAzul.__init__(self)
        elif index == 1:
            self.__class__ = GloboRojo
            GloboRojo.__init__(self)

# clase GloboRojo
class GloboRojo(GloboBase):
    def __init__(self):
        super().__init__(color="Rojo", damage=1, vida=1, velocidad=1)

# clase GloboAzul
class GloboAzul(GloboBase):
    def __init__(self):
        super().__init__(color="Azul", damage=2, vida=2, velocidad=2)

# clase GloboVerde
class GloboVerde(GloboBase):
    def __init__(self):
        super().__init__(color="Verde", damage=3, vida=3, velocidad=3)

# clase GloboAmarillo
class GloboAmarillo(GloboBase):
    def __init__(self):
        super().__init__(color="Amarillo", damage=4, vida=4, velocidad=4)
