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
        band=False
        for i in range(len(self.libro)):
            if(libro.nombre == self.libro[i].get('Nombre') and libro.autor == self.libro[i].get('Autor')):
                band=True
                if (self.libro[i].get('Cantidad')-cantidad)>=0:
                    self.libro[i]['Cantidad']-=cantidad
                    print("Se presto"+ str(cantidad))
                else:
                    print("No tenemos el o los libros que necesita")
        if(band==False):
            print("QQQNo tenemos el o los libros que necesita")
                    
    def Vender_libros(self):
        pass 
    def Cuantos_libros(self):
        pass
    def Buscar_libro(self):
        pass
    