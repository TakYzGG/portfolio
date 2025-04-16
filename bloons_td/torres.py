# crear clase TorreBase
class TorreBase(object):
    def __init__(self, nombre, costo, damage, alcance, proyectil, cadencia): # alcance = radio
        self.__torres = ("Dardero", "TiraTachuelas", "Cañon", "Hielo", "SuperMono")
        self.__proyectiles = ("Dardos", "Clavos", "Bombas", "Hielo")
        self.__nombre = None
        self.__costo = None
        self.__damage = None
        self.__alcance = None
        self.__proyectil = None
        self.__cadencia = None

        self.nombre = nombre
        self.costo = costo
        self.damage = damage
        self.alcance = alcance
        self.proyectil = proyectil
        self.cadencia = cadencia

    # getters y setters
    # torres
    @property
    def torres(self):
        return self.__torres

    # proyectiles
    @property
    def proyectiles(self):
        return self.__proyectiles

    # nombre
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre in self.torres:
            self.__nombre = nombre
        else:
            print("Torre no existente")

    # costo
    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, costo):
        if isinstance(costo, int):
            self.__costo = costo
        else:
            print("Torre no existente")

    # damage
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        if isinstance(damage, (int, float)) and damage >= 0:
            self.__damage = damage
        else:
            print("El damage tiene que ser mayor o igual a 0")

    # alcance
    @property
    def alcance(self):
        return self.__alcance

    @alcance.setter
    def alcance(self, alcance):
        if isinstance(alcance, (int, float)) and alcance >= 0:
            self.__alcance = 3.1416 * (alcance ** 2)
        else:
            print("El alcance tiene que ser mayor o igual a 0")

    # proyectil
    @property
    def proyectil(self):
        return self.__proyectil

    @proyectil.setter
    def proyectil(self, proyectil):
        if proyectil in self.proyectiles:
            self.__proyectil = proyectil
        else:
            print("Proyectil no existente")

    # cadencia (la cadencia se mide en ms)
    @property
    def cadencia(self):
        return self.__cadencia

    @cadencia.setter
    def cadencia(self, cadencia):
        if isinstance(cadencia, (int, float)) and cadencia >= 0:
            self.__cadencia = cadencia
        else:
            print("La cadencia debe ser mayor a 0")

    def comprar(self, jugador):
        if jugador.dinero >= self.costo:
            print(f"El jugador compro la torre {self.nombre} por {self.costo}")
            jugador.dinero -= self.costo
        else:
            print(f"No tienes suficiente dinero para comprar la torre {self.nombre}")


    def atacar(self):
        print(f"La torre {self.nombre} a atacado con {self.proyectil}")

# clase Dardero
class Dardero(TorreBase):
    def __init__(self):
        super().__init__(nombre="Dardero", costo=200, damage=1, alcance=3, proyectil="Dardos", cadencia=500)

# clase TiraTachuelas
class TiraTachuelas(TorreBase):
    def __init__(self):
        super().__init__(nombre="TiraTachuelas", costo=350, damage=1, alcance=2, proyectil="Clavos", cadencia=350)

# clase Canon
class Canon(TorreBase):
    def __init__(self):
        super().__init__(nombre="Cañon", costo=450, damage=1, alcance=3, proyectil="Bombas", cadencia=350)

# clase Hielo
class Hielo(TorreBase):
    def __init__(self):
        super().__init__(nombre="Hielo", costo=700, damage=0, alcance=1.5, proyectil="Hielo", cadencia=200)

# clase Supermono
class SuperMono(TorreBase):
    def __init__(self):
        super().__init__(nombre="SuperMono", costo=1500, damage=1, alcance=7, proyectil="Dardos", cadencia=200)
