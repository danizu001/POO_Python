class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')

class Terrestre:

    def desplazar(self):
        print('El animal anda')


class Acuatico:

    def desplazar(self):
        print('El animal nada')


class Cocodrilo(Terrestre, Acuatico):
    """Abstracción de cocodrilo. Herencia multiple.
    
    Como Terrestre se encuentra más a la izquierda,
    sería la definición de desplazar de esta clase la
    que prevalecería.
    """
    pass

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()