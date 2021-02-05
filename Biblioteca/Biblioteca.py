def Sacar_libro(prolibro,libro,cantidad):
        band=False
        for i in range(len(prolibro)):
            if(libro.nombre == prolibro[i].get('Nombre') and libro.autor == prolibro[i].get('Autor')):
                band=True
                if (prolibro[i].get('Cantidad')-cantidad)>=0:
                    prolibro[i]['Cantidad']-=cantidad
                    print("Se prestaron: "+ str(cantidad)+" libros")
                else:
                    print("No tenemos el o los libros que necesita")
        if(band==False):
            print("No tenemos el o los libros que necesita")
class biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libro = []
              
    def Agregar_libro(self,libro,cantidad=1):
        existe=False
        for i in range(len(self.libro)):
            if(libro.nombre == self.libro[i].get('Nombre') and libro.autor == self.libro[i].get('Autor')):
                self.libro[i]['Cantidad']+=cantidad
                existe=True
        if existe == False:
            libro._cantidad=cantidad
            self.libro.append({"Nombre":libro.nombre,"Autor":libro.autor,"Genero":libro.genero,"Cantidad":libro._cantidad})
            print(self.libro[-1].values())
    def Prestar_libro(self,libro,cantidad=1):
        Sacar_libro(self.libro,libro,cantidad)
    def Vender_libros(self,libro,cantidad=1):
        Sacar_libro(self.libro,libro,cantidad)
    def Cuantos_libros(self):
        pass
    def Buscar_libro(self):
        pass
    
        