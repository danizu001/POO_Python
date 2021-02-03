class Persona:
    
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def saluda(self,otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

#La clase es Persona pero las instancias son nombre y edad    
erika = Persona('erika',30)
david = Persona('david',32)

david.saluda(erika)
