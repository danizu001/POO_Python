class Automovil:
    
    def __init__(self,modelo,marca,color,cil):
        self.modelo = modelo
        self.marca = marca 
        self.color = color 
        self._estado = 'en_reposo'
        self._motor = Motor(cil)
    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(-6*self._motor.cilindros)
        else: 
            self._motor.inyecta_gasolina(-3*self._motor.cilindros)
        
        self._estado = 'En_movimiento'
    
class Motor:
    def __init__(self,cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self._gasolina = 100
    def inyecta_gasolina(self,cantidad):
        self._gasolina += cantidad 
    
bmw = Automovil("z4","bmw","negro",5) 