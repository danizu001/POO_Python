def Sacar_libro(prolibro,libro,cantidad):
        band=False
        for i in range(len(prolibro)):
            if(libro.nombre == prolibro[i].get('Nombre') and libro.autor == prolibro[i].get('Autor')):
                band=True
                if (prolibro[i].get('Cantidad')-cantidad)>=0:
                    prolibro[i]['Cantidad']-=cantidad
                    print("Se prestaron o vendieron: "+ str(cantidad)+" libros")
                    return True
                else:
                    print("No tenemos el o los libros que necesita")
        if(band==False):
            print("No tenemos el o los libros que necesita")
            return False
class biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libro = []
        self._ganancias=0
    @property
    def ganancias(self):
        return self._ganancias
    @ganancias.setter
    def ganancias(self,Ganancia):
        self._ganancias += Ganancia
        print("La ganancia es de: " + str(self.ganancias))
    def Agregar_libro(self,libro,cantidad=1):
        existe=False
        for i in range(len(self.libro)):
            if(libro.nombre == self.libro[i].get('Nombre') and libro.autor == self.libro[i].get('Autor')):
                self.libro[i]['Cantidad']+=cantidad
                existe=True
        if existe == False:
            libro._cantidad=cantidad
            self.libro.append({"Nombre":libro.nombre,"Autor":libro.autor,"Genero":libro.genero,"Cantidad":libro._cantidad,"Precio":libro.precio})
            print(self.libro[-1].values())
    def Prestar_libro(self,libro,cantidad=1):
        print("Cada alquilada cuesta 5000")
        gan=Sacar_libro(self.libro,libro,cantidad)
        if gan:
            self.ganancias=(5000*cantidad)
            print("Verificando " + str(self.ganancias))
    def Vender_libros(self,libro,cantidad=1):
        gan=Sacar_libro(self.libro,libro,cantidad)
        if gan:
            self.ganancias=(libro.precio*cantidad)
    def Cuantos_libros(self):
        pass
    def Buscar_libro(self):
        pass
    
        