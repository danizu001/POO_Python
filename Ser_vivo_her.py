class Ser_viviente:
    def __init__(self,movimiento,comunicacion):
        self.movimiento=movimiento
        self.comunicacion=comunicacion
    def moverse(self,movimiento):
        return f'Me estoy moviendo con los {movimiento}'
    def comunicacion2(self,comunicacion):
        return f'Me estoy comunicando con {comunicacion}'

class Humano(Ser_viviente):
    def __init__(self,movimiento,comunicacion):
        super().__init__(movimiento, comunicacion)
    def Analizar(self):
        print("analizando")
class Pajaro(Ser_viviente):
    def __init__(self,movimiento,comunicacion):
        super().__init__(movimiento, comunicacion)
    def Volar(self):
        print("Estoy volando")
        
paloma=Pajaro("alas","el pico")
hortua=Humano("pies","la boca")