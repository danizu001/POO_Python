def Sacar_libro(prolibro,libro,cantidad):
        band=False
        for i in range(len(prolibro)):
            if(libro.get("Nombre") == prolibro[i].get('Nombre') and libro.get("Autor") == prolibro[i].get('Autor')):
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
def buscar(busqueda,libro):
    busq=[]
    for i in libro:
        if busqueda == i.get("Nombre"):
            busq.append(i)
        if busqueda == i.get("Autor"):
            busq.append(i)
        if busqueda == i.get("Genero"):
            busq.append(i)
    return busq
                
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
        for i in self.libro:
            if(libro.nombre == i.get('Nombre') and libro.autor == i.get('Autor')):
                i['Cantidad']+=cantidad
                existe=True
        if existe == False:
            libro._cantidad=cantidad
            self.libro.append({"Nombre":libro.nombre,"Autor":libro.autor,"Genero":libro.genero,"Cantidad":libro._cantidad,"Precio":libro.precio,"Etiqueta":len(self.libro)+1})
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
            self.ganancias=(libro.get("Precio")*cantidad)
    def Cuantos_libros(self):
        return len(self.libro)
    def Buscar_libro(self,busqueda):
        busq = []
        busq=buscar(busqueda,self.libro)
        return f'{busq}'
                
    
        